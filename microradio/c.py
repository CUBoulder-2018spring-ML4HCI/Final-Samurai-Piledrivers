import serial
import time

import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

send_address = '127.0.0.1', 6448

PORT="/dev/cu.usbmodem1412"
BAUD = 115200

parser = argparse.ArgumentParser()

parser.add_argument("--ip", default="127.0.0.1",
  help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=6448,
  help="The port the OSC server is listening on")

args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

while True:
    s= serial.Serial(PORT)
    s.baudrate= BAUD
    datax = s.readline()
    #print(datax)
    intx = datax.decode().split(', ')
    print(intx)
    print(len(intx))
    if (len(intx)==4):
        try:
            x=float(intx[0])
            y=float(intx[1])
            z=float(intx[2])
            print (x, y, z)

            message = []

            message.append(x)
            message.append(y)
            message.append(z)

            # rNum = OSC.OSCMessage()
            # rNum.setAddress("/wek/inputs")# get a random num every loop
            # rNum.append(x) #0.0 here is hack to make it float
            # rNum.append(y)
            # rNum.append(z)

            # c.send(rNum)

            client.send_message("/wek/inputs", message)
        except ValueError:
            continue
