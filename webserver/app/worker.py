import threading
import socket
import struct
import json
from collections import defaultdict
from math import sqrt

from app import socketio
from app.models import Record, Hold

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


class PublisherThread(SocketConnectedThread):

    climb = None
    canid_holdid_dict = None
    session = None
    db_session = None

    def __init__(self, climb, db_session):
        super(PublisherThread, self).__init__()
        self.climb = climb
        # Holds id is from actual, not historic wall, because if I have to replay
        # some events, I access the db, not the CAN bus
        self.canid_holdid_dict = dict(zip([o.can_id for o in climb.going_on.holds],
                                          [o.id for o in climb.going_on.holds]))
        self.db_session = db_session
        self.session = self.db_session()

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

    def join(self, timeout=None):
        self.stoprequest.set()
        self.sock.close()
        print("UDP mock connection closed")
#        print("Can connection closed")
        super(PublisherThread, self).join(timeout)


class CalibrationThread(SocketConnectedThread):

    db_session = None
    session = None
    canid_values_dict = None
    hold_info = None

    def __init__(self, db_session, hold_info):
        super(CalibrationThread, self).__init__()
        self.db_session = db_session
        self.session = db_session()
        self.canid_values_dict = defaultdict(list)
        self.hold_info = hold_info

    def run(self):
        while not self.stoprequest.isSet():
            #Receive and unpack message
            try:
                can_pkt = self.sock.recv(16)
            except socket.error:
                socketio.emit('message', 'timeout', namespace='/api/holds')
                self.db_session.remove()
                print("Went to timeout!")
                continue
            can_id, length, x, y, z, timestamp = struct.unpack(self.FMT, can_pkt)
            #Mask ID to hide possible flags
            #can_id &= socket.CAN_EFF_MASK
            magnitude = sqrt(x**2 + y**2 + z**2)
            print(magnitude)
            self.canid_values_dict[can_id].append(magnitude)
            found_a_device = self.search_trough_records(can_id)
            if found_a_device is True:
                socketio.emit('message', 'ok', namespace='/api/holds')
                if self.hold_info.save_result is True:
                    hold = Hold.query.get(self.hold_info.hold_id)
                    hold.can_id = can_id
                    self.session.commit()
                #Beware! in any case, db_session.remove()
                self.db_session.remove()
            else:
                continue

    def join(self, timeout=60):
        super(CalibrationThread, self).join(timeout)
        self.stoprequest.set()
        self.sock.close()
        print("UDP mock connection closed")
#        print("Can connection closed")

    def search_trough_records(self, can_id):
        NUMBER_OF_SAMPLES = 10
        if self.canid_values_dict[can_id].length % NUMBER_OF_SAMPLES is not 0:
            pass
