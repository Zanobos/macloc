import json
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import serial

k = 13.0

def build_data(holdid, xaxis, yaxis, zaxis):
    return {"wallId" : "wall1",
            "holdId" : holdid,
            "xaxis" : round(float(xaxis)/k, 3),
            "yaxis" : round(float(yaxis)/k, 3),
            "zaxis" : round(float(zaxis)/k, 3)}

DICT = {"!": "hold1", "@":"hold2", "#":"hold3",
        "$":"hold4", "%": "hold5"}
print("Starting program - reader")
SER = serial.Serial('/dev/ttyS0', baudrate=4800, parity=serial.PARITY_NONE, 
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
try:
    while True:
        readings = SER.readline()
        forces = readings.split("/")
        trimmed = False
        x = forces[0]
        id
        while not trimmed:
            id = x[0]
            x = x[1:len(x)]
            try:
                int(x)
                trimmed = True
            except:
                trimmed = False
        y = forces[1]
        z = forces[2]
        print(DICT[id])
        print(x)
        print(y)
        print(z)
        req = urllib2.Request("http://macloc-165115.appspot.com/rest/forcesService/upload")
        req.add_header("Content-Type","application/json")
        data = json.dumps(build_data(DICT[id],x,y,z))
        response = urllib2.urlopen(req,data)
except KeyboardInterrupt:
    print("Exiting Program")
finally:
    SER.close()
