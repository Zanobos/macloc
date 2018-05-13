"""
Receiver
"""
import socket
import struct

SOCK = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW)
SOCK.bind(("can0",))

fmt = "<IB3x8s"

while 1:
	can_pkt = SOCK.recv(16)
	can_id, length, data = struct.unpack(fmt, can_pkt)
	can_id &= socket.CAN_EFF_MASK

	print("ID:", format(can_id, '03b'), end="")
	print("\t\tData: ", end="")
	for i in range(length):
		print("", format(data[i], '02X'), end="")
	print("")

	with open("log.txt", "w+") as log:
		print("", format(can_id, '03b'), file=log, end=",")
		for i in range(length):
			print(" ", format(data[i], '02X'), file=log, end="")
		print("", file=log)
