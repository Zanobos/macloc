"""
CAN Client
"""
import socket
import struct

SOCK = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
SOCK.bind(("vcan0",))

FMT = "<IB3x8s"
CAN_PKT = struct.pack(FMT, 0x741, len(b"hello"), b"hello")
SOCK.send(CAN_PKT)

CAN_PKT = SOCK.recv(16)
CAN_ID, LENGTH, DATA = struct.unpack(FMT, CAN_PKT)
CAN_ID &= socket.CAN_EFF_MASK
DATA = DATA[:LENGTH]

print("Message:", DATA)
print("Fine")
