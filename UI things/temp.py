import argparse
import math
from pythonosc import dispatcher
from pythonosc import osc_server
import sys

import pyautogui
import time

character = 0
lemonade= [0]*9

def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))
    print("not here")

def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
        print("here?")
    except ValueError:
        pass

def checkhighest(lemonade):
    i=0
    highest = 0
    index = 0
    while i < len(lemonade):
        if lemonade[i] > highest:
            highest = lemonade[i]
            index = i
        i+=1
    return index

def control(lemonade):
    index = checkhighest(lemonade)

    #first is Ryu
    if character == 1:
        if index == 1:
            Fireball()
        if index == 2:
            FlyingKick()

    #next is Sagat
    elif character == 2:
        if index == 1:
            HighTigerShot()
        else:
            LowTigerShot()

    #last is M. Bison
    else:
        if index == 1:
            PsychoCrusher()
        else:
            ScissorKick()


#M. Bison
def PsychoCrusher():
    pyautogui.keyDown('h')
    time.sleep(2)
    pyautogui.keyDown('k')
    pyautogui.keyDown('s')
    pyautogui.keyUp('h')
    pyautogui.keyUp('k')
    pyautogui.keyUp('s')

def ScissorKick():
    pyautogui.keyDown('h')
    time.sleep(2)
    pyautogui.keyDown('k')
    pyautogui.keyDown('d')
    pyautogui.keyUp('h')
    pyautogui.keyUp('k')
    pyautogui.keyUp('d')

#Ryu
def Fireball():
    pyautogui.keyDown('k')
    pyautogui.keyUp('k')
    pyautogui.keyDown('j')
    pyautogui.keyDown('k')
    pyautogui.keyDown('s')
    pyautogui.keyUp('j')
    pyautogui.keyUp('k')
    pyautogui.keyUp('s')

def FlyingKick():
    pyautogui.keyDown('k')
    pyautogui.keyUp('k')
    pyautogui.keyDown('j')
    pyautogui.keyDown('k')
    pyautogui.keyDown('s')
    pyautogui.keyUp('j')
    pyautogui.keyUp('k')
    pyautogui.keyUp('s')


#Sagat
def HighTigerShot():
    pyautogui.keyDown('j')
    pyautogui.keyDown('k')
    pyautogui.keyUp('j')
    pyautogui.keyDown('s')
    pyautogui.keyUp('k')
    pyautogui.keyUp('s')

def LowTigerShot():
    pyautogui.keyDown('j')
    pyautogui.keyDown('k')
    pyautogui.keyUp('j')
    pyautogui.keyDown('c')
    pyautogui.keyUp('k')
    pyautogui.keyUp('c')


if __name__ == "__main__":

    character = sys.argv[1]

    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
                        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
                        type=int, default=12000, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/wek/outputs", lemonade)
    dispatcher.map("/volume", print_volume_handler, "Volume")
    dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)
    control(lemonade)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
