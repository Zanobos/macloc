import threading
import socket
import struct

from app import db, socketio
from app.models import Record
from app.utils.rabbitmq import Publisher, Receiver
from flask import jsonify

class PublisherThread(threading.Thread):

    #Format string to unpack received message
    FMT = "<IB3x3h1H"

    climb = None
    socket = None
    publisher = None
    canid_holdid_dict = None

    def __init__(self, climb):
        super(PublisherThread, self).__init__()
        self.stoprequest = threading.Event()
        self.climb = climb
        self.canid_holdid_dict = dict(zip([o.can_id for o in climb.on_wall.holds],
                                          [o.hold_id for o in climb.on_wall.holds]))
        self.publisher = Publisher()
        self.publisher.open_connection()
        print("Publisher connected to RabbitMQ")
        self.socket = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
        self.socket.bind(("can0",))
        print("can connection opened")

    def run(self):
        while not self.stoprequest.isSet():
            #Receive and unpack message
            can_pkt = socket.recv(16)
            can_id, length, x, y, z, timestamp = struct.unpack(self.FMT, can_pkt)
            #Mask ID to hide possible flags
            can_id &= socket.CAN_EFF_MASK
            #Create Record
            hold_id = self.canid_holdid_dict[can_id]
            record = Record(hold_id=hold_id, can_id=can_id, x=x, y=y, z=z,
                            timestamp=timestamp, climb_id=self.climb.id)
            #Send Record to RabbitMQ
            self.publisher.publish(jsonify(record.to_ws_dict()))
            #Save the Record in db
            db.session.add(record)
            print(record)

    def join(self, timeout=None):
        self.stoprequest.set()
        super(PublisherThread, self).join(timeout)
        self.publisher.close_connection()
        print("Publisher closed connection to RabbitMQ")
        db.session.commit()
        self.socket.close()
        print("can connection closed")

class ReceiverThread(threading.Thread):

    receiver = None

    def on_rabbitmq_message(self, body):
        print('message ', body)
        socketio.emit('json', body, namespace='/api/climbs')

    def __init__(self):
        super(ReceiverThread, self).__init__()
        self.stoprequest = threading.Event()

        self.receiver = Receiver()
        self.receiver.open_connection()
        self.receiver.setup_consumer(self.on_rabbitmq_message)
        print("Receiver connected to RabbitMQ")

    def run(self):
        self.receiver.start_consuming()

    def join(self, timeout=None):
        self.stoprequest.set()
        self.receiver.stop_consuming()
        super(ReceiverThread, self).join(timeout)
        self.receiver.close_connection()
        print("Receiver closed connection to RabbitMQ")
