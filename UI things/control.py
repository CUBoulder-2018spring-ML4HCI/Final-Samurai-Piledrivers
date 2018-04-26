import pyautogui
import socket
import time
from microbit import *

UDP_IP = "127.0.0.1"
UDP_PORT_SEND = 6448
UDP_PORT_RECE = 12000

sock_RECE = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_RECE.bind((UDP_IP, UDP_PORT_RECE))
outlist= [0]*9

def checkhighest(outlist):
    i=0
    highest = 0
    index = 0
    while i < len(outlist):
        if outlist[i] > highest:
            highest = outlist[i]
            index = i
        i+=1
    return index


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
def DragonPunch():
    pyautogui.keyDown('k')
    pyautogui.keyUp('k')
    pyautogui.keyDown('j')
    pyautogui.keyDown('k')
    pyautogui.keyDown('s')
    pyautogui.keyUp('j')
    pyautogui.keyUp('k')
    pyautogui.keyUp('s')

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

def SomersaultThrow():
    pyautogui.keyDown('h')
    pyautogui.keyDown('j')
    pyautogui.keyUp('h')
    pyautogui.keyDown('k')
    pyautogui.keyUp('j')
    pyautogui.keyDown('d')
    pyautogui.keyUp('k')
    pyautogui.keyUp('d')

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

def control(character):

    def comboInterp(charac, x):

        #ryu first
        if charac == 1:
            if x == 1:
                DragonPunch()
            if x == 2:
                Fireball()
            if x == 3:
                FlyingKick()
            if x == 4:
                SomersaultThrow()

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
        data, addr = sock_RECE.recvfrom(1024)  # buffer size is 1024 bytes
        print(data, len(data),"/n")
        print(data[30],data[31],data[32],data[33],data[34],data[35],data[26],data[27],data[28],data[29])

        data9 = [data[30],data[31],data[32],data[33],data[34],data[35],data[26],data[27],data[28]]
        index = checkhighest(data9)

        if index == 0:
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

        

        #
        # if data[20] == 63:
        #     # class 1
        #     pyautogui.keyDown('w')
        #     pyautogui.keyUp('w')
        #     print("up")
        #
        # elif data[20] == 64:
        #     if data[21] == 0:
        #         # class 2
        #         pyautogui.keyDown('a')
        #         pyautogui.keyUp('a')
        #         print("left")
        #     elif data[21] == 64:
        #         # class 3
        #         pyautogui.keyDown('s')
        #         pyautogui.keyUp('s')
        #         print("down")
        #     elif data[21] == 128:
        #         # class 4
        #         pyautogui.keyDown('d')
        #         pyautogui.keyUp('d')
        #         print("right")
        #     elif data[21] == 160:
        #         # class 5
        #         pyautogui.keyDown('h')
        #         pyautogui.keyUp('h')
        #         print("throw")
        #     elif data[21] == 192:
        #         # class 6
        #         pyautogui.keyDown('j')
        #         pyautogui.keyUp('j')
        #         print("quick")
        #     elif data[21] == 224:
        #         # class 7
        #         comboInterp(character, 1)
        #
        # elif data[20] == 65:
        #     if data[21] != 16:
        #         # class 8
        #         comboInterp(character, 2)
        #     elif data[21] == 16:
        #         # class 9
        #         print("standby")