import threading
import socket
import struct

from app import db
from app.models import Record
from app.utils.rabbitmq import Publisher

class WorkerThread(threading.Thread):

    #Format string to unpack received message
    FMT = "<IB3x3h1H"

    climb_id = None
    socket = None
    publisher = None

    def __init__(self, climb_id):
        super(WorkerThread, self).__init__()
        self.stoprequest = threading.Event()
        self.climb_id = climb_id
        self.publisher = Publisher()
        self.publisher.open_connection()
        print("connected to RabbitMQ")
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
            record = Record(can_id=can_id, x=x, y=y, z=z,
                            timestamp=timestamp, climb_id=self.climb_id)
            #Send Record to RabbitMQ
            self.publisher.publish(record.to_dict)
            #Save the Record in db
            db.session.add(record)
            print(record)

    def join(self, timeout=None):
        self.stoprequest.set()
        super(WorkerThread, self).join(timeout)
        self.publisher.close_connection()
        print("closed connection to RabbitMQ")
        db.session.commit()
        self.socket.close()
        print("can connection closed")
