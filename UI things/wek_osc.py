import argparse
import random
import time

from pythonosc import osc_message_builder
from pythonosc import udp_client

parser = argparse.ArgumentParser()

parser.add_argument("--ip", default="127.0.0.1",
  help="The ip of the OSC server")
parser.add_argument("--port", type=int, default=6448,
  help="The port the OSC server is listening on")

args = parser.parse_args()

client = udp_client.SimpleUDPClient(args.ip, args.port)

for x in range(10):
    print(x)
    client.send_message("/wekinator/control/startRecording", 1)
    time.sleep(1)
    client.send_message("/wekinator/control/stopRecording", 1)
    time.sleep(1)
