"""
Receiver
"""
import socket
import struct

SOCK = socket.socket(socket.PF_CAN, socket.SOCK_RAW, socket.CAN_RAW) 		#Create CAN compatible socket	
SOCK.bind(("can0",))			#Bind socket to CAN interface
	
fmt = "<IB3x3h1b"				#Format string to unpack received message

while 1:				#Start cycle to receive messages
    can_pkt = SOCK.recv(16)			#Receive message
    can_id, length, data1, data2, data3, data4 = struct.unpack(fmt, can_pkt) #Unpack message
    can_id &= socket.CAN_EFF_MASK			#Mask ID to hide possible flags

    print("Packet received from ID:", format(can_id, '04d'), end=".   ")								#Prints ID and values received, unmodified and in hex

    print("Data: ", data1, ", ", data2, ", ", data3, ", ", data4)


    data_f = []			#List for true values


    with open("log.txt", "a+") as log:					#Write ID and values to text file
        print("", format(can_id, '04d'), file=log, end=",")
        print("\t", data1, "\t", data2, "\t", data3, "\t", data4, file=log)

		
