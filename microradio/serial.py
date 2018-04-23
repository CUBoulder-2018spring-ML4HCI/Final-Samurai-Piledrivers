import serial
import time
import OSC

send_address = '', 6448

PORT=""
BAUD = 115200

c = OSC.OSCClient()
c.connect( send_address )

while True:
    s= serial.Serial(PORT)
    s.baudrate= BAUD
    datax = s.readline()
    intx = datax.split(", ")
    #print(intx)
    if (len(intx)==4):
        try:
            x=float(intx[0])
            y=float(intx[1])
            z=float(intx[2])
            print (x, y, z)
            rNum = OSC.OSCMessage()
            rNum.setAddress("/wek/inputs")# get a random num every loop
            rNum.append(x) #0.0 here is hack to make it float
            rNum.append(y)
            rNum.append(z)
            c.send(rNum)
        except ValueError:
            continue
