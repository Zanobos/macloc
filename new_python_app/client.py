"""
Sender
"""
import socket

UDP_IP = "192.168.1.1"
UDP_PORT = 5000
MESSAGE = "Test"
ADDR = (UDP_IP, UDP_PORT)

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("Message:", MESSAGE)

SOCK = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for i in range(2):
    SOCK.sendto(MESSAGE.encode(), ADDR)
    if SOCK.sendto(MESSAGE.encode(), ADDR):
        print("Sending...")
