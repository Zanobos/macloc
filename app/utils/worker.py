import threading
import socket
import struct
import json

from app import socketio
from app.models import Record
from app.utils.rabbitmq import Publisher, Receiver

class PublisherThread(threading.Thread):

    #Format string to unpack received message
    FMT = "<IB3x3h1H"

    climb = None
    sock = None
    publisher = None
    canid_holdid_dict = None
    session = None
    db_session = None

    def __init__(self, climb, db_session):
        super(PublisherThread, self).__init__()
        self.stoprequest = threading.Event()
        self.climb = climb
        self.canid_holdid_dict = dict(zip([o.can_id for o in climb.on_wall.holds],
                                          [o.id for o in climb.on_wall.holds]))
        self.publisher = Publisher()
        self.publisher.open_connection()

        self.db_session = db_session
        self.session = db_session()

        print("Publisher connected to RabbitMQ")
#        self.sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
#        self.sock.bind(("can0",))
#        print("can connection opened")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 6000))
        print("UDP mock connection open")

    def run(self):
        while not self.stoprequest.isSet():
            #Receive and unpack message
            try:
                can_pkt = self.sock.recv(16)
            except socket.error:
                print('Exiting can receiver loop')
                self.session.commit()
                self.db_session.remove()
                print("Commiting the session and clearing resources")
                continue
            can_id, length, x, y, z, timestamp = struct.unpack(self.FMT, can_pkt)
            #Mask ID to hide possible flags
            #can_id &= socket.CAN_EFF_MASK
            #Create Record
            hold_id = self.canid_holdid_dict[can_id]
            record = Record(hold_id=hold_id, can_id=can_id, x=x, y=y, z=z,
                            timestamp=timestamp, climb_id=self.climb.id)
            #Send Record to RabbitMQ
            self.publisher.publish(json.dumps(record.to_ws_dict()))
            #Save the Record in db
            self.session.add(record)
            print(record)

    def join(self, timeout=None):
        self.stoprequest.set()
        self.sock.close()
        print("Can connection closed")
        super(PublisherThread, self).join(timeout)
        self.publisher.close_connection()
        print("Publisher closed connection to RabbitMQ")

class ReceiverThread(threading.Thread):

    receiver = None

    def on_rabbitmq_message(self, body):
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
