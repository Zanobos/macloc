import threading
import socket
import struct
import json

from app import socketio
from app.models import Record

class SocketConnectedThread(threading.Thread):

    #Format string to unpack received message
    FMT = "<IB3x3h1H"
    sock = None

    def __init__(self):
        super(SocketConnectedThread, self).__init__()
        self.stoprequest = threading.Event()

#        self.sock = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
#        self.sock.bind(("can0",))
#        print("can connection opened")

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("127.0.0.1", 6000))
        print("UDP mock connection open")

    def join(self, timeout=None):
        self.stoprequest.set()
        self.sock.close()
        print("UDP mock connection closed")
#        print("Can connection closed")
        super(SocketConnectedThread, self).join(timeout)

class PublisherThread(SocketConnectedThread):

    climb = None
    canid_holdid_dict = None
    session = None
    db_session = None

    def __init__(self, climb, db_session):
        super(PublisherThread, self).__init__()
        self.climb = climb
        self.canid_holdid_dict = dict(zip([o.can_id for o in climb.on_wall.holds],
                                          [o.id for o in climb.on_wall.holds]))
        self.db_session = db_session
        self.session = db_session()

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
            if hold_id is None:
                continue
            record = Record(hold_id=hold_id, can_id=can_id, x=x, y=y, z=z,
                            timestamp=timestamp, climb_id=self.climb.id)
            #Send Record to WS
            socketio.emit('json', json.dumps(record.to_ws_dict()), namespace='/api/climbs')
            #Save the Record in db
            self.session.add(record)
            print(record)
