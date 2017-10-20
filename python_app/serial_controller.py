import time
import serial
print("Starting program - controller")
SER = serial.Serial('/dev/ttyS0', baudrate=4800, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
#CHAR = ["!", "@", "#", "$", "%"]
CHAR = ["#"]
i = 0
try:
    while True:
        print(CHAR[i])
        SER.write(CHAR[i])
        i = i + 1
        i = i % len(CHAR)
        time.sleep(2.0)
except KeyboardInterrupt:
    print("Exiting Program")

finally:
    SER.close()
