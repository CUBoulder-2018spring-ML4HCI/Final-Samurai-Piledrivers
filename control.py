import pyautogui
import socket

UDP_IP = "127.0.0.1"
UDP_PORT_SEND = 6448
UDP_PORT_RECE = 12000

sock_RECE = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_RECE.bind((UDP_IP, UDP_PORT_RECE))


while(1):

    #here are the classes, 1,2,3,4,5,6,7,8: up,left,down,right,throw,quick,heavy,dodge
    #listen for the wek, this will be replaced later by an in house ML algo.
    data, addr = sock_RECE.recvfrom(1024)  # buffer size is 1024 bytes
    #print(data, len(data),"/n")
    #print(data[20],data[21])
    if data[20] == 63:
        # class 1
        pyautogui.keyDown('w')
        pyautogui.keyUp('w')
        print("up")

    elif data[20] == 64:
        if data[21] == 0:
            #class 2
            pyautogui.keyDown('a')
            pyautogui.keyUp('a')
            print("left")
        elif data[21] == 64:
            #class 3
            pyautogui.keyDown('s')
            pyautogui.keyUp('s')
            print("down")
        elif data[21] == 128:
            #class 4
            pyautogui.keyDown('d')
            pyautogui.keyUp('d')
            print("right")
        elif data[21] == 160:
            #class 5
            pyautogui.keyDown('h')
            pyautogui.keyUp('h')
            print("throw")
        elif data[21] == 192:
            #class 6
            pyautogui.keyDown('j')
            pyautogui.keyUp('j')
            print("quick")
        elif data[21] == 224:
            #class 7
            pyautogui.keyDown('k')
            pyautogui.keyUp('k')
            print("heavy")

    elif data[20] == 65:
        if data[21] != 16:
            #class 8
            pyautogui.keyDown('l')
            pyautogui.keyUp('l')
            print("dodge")
        elif data[21] == 16:
            # class 9
            print("standby")

