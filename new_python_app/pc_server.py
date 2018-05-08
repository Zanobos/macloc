"""
Server
"""
import socket

UDP_IP = "192.168.1.1"
UDP_PORT = 5000
print(UDP_IP, UDP_PORT)
SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SOCK.bind((UDP_IP, UDP_PORT))

while True:
    DATA = SOCK.recvfrom(1024)
    print("Message:", DATA)
    if DATA:
        print("Receiving...")
