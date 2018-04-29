import argparse
import math
from pythonosc import dispatcher
from pythonosc import osc_server

import pyautogui
import socket
import time



def print_volume_handler(unused_addr, args, volume):
    print("[{0}] ~ {1}".format(args[0], volume))
    print("not here")

def print_compute_handler(unused_addr, args, volume):
    try:
        print("[{0}] ~ {1}".format(args[0], args[1](volume)))
        print("here?")
    except ValueError:
        pass


lemonade= [0]*9
def checkhighest(lemonade):
    i=0
    highest = 0
    index = 0
    while i < len(outlist):
        if outlist[i] > highest:
            highest = outlist[i]
            index = i
        i+=1
    return index

def control(character):

    def comboInterp(charac, x):

        #ryu first
        if charac == 1:
            if x == 1:
                Fireball()
            if x == 2:
                FlyingKick()

        #next is Sagat
        elif charac == 2:
            if x == 1:
                HighTigerShot()
            else:
                LowTigerShot()

        #last is M. Bison
        else:
            if x == 1:
                PsychoCrusher()
            else:
                ScissorKick()


    while 1:
        # here are the classes, 1,2,3,4,,6,7,8: up,left,down,right,throw,quick,heavy,dodge
        # listen for the wek, this will be replaced later by an in house ML algo.

        index = checkhighest(lemonade)

        if index == 0:
            if character == Ryu:
                Fireball()
            if character == Sagat:
                HighTigerShot()
            if character == Bison:
                PsychoCrusher()
            pass
        elif index == 1:
            pass
        elif index == 2:
            pass
        elif index == 3:
            pass
        elif index == 4:
            pass
        elif index == 5:
            pass
        elif index == 6:
            pass
        elif index == 7:
            pass
        elif index == 8:
            pass


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

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
