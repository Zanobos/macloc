import socket
import struct

UDP_IP = "127.0.0.1"
UDP_PORT = 6000

FMT = "<IB3x3h1H"
MESSAGE = struct.pack(FMT, 41, 100, 100, 77, 87, 1200)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
