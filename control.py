import pyautogui
import time
import socket

#
# if char == 'y':
#     pyautogui.press('down')
#     pyautogui.keydown('down')
#     pyautogui.keydown('right')
#
#     pyautogui.keyup('down')
#     pyautogui.keyup('right')
#     pyautogui.keydown('s')
#     pyautogui.keydown('right')
#
#     pyautogui.keyup('s')
#     pyautogui.keyup('right')
#     print("yes")
#             # press the left arrow key
# elif event.char == 'p':  # OR  event.keycode == 50:
#     pyautogui.press('s')

# socket variables
UDP_IP = "127.0.0.1"
UDP_PORT_SEND = 6448
UDP_PORT_RECE = 12000

sock_RECE = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock_RECE.bind((UDP_IP, UDP_PORT_RECE))




def communicate():
    print("number to send to wekinator")
    text = input("Input number")
    text = text.join([text[:5]] * 2)
    print(text, " , sent.")
    sock_SEND = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock_SEND.sendto(text.encode(), (UDP_IP, UDP_PORT_SEND))

while(1):

    #here are the classes, 1 is right, 2 is d, 3 is right, 4 is d as well
    #communicate()

    #listen for the wek
    data, addr = sock_RECE.recvfrom(1024)  # buffer size is 1024 bytes
    #print(data, len(data),"/n")
    #print(data[20],data[21])
    if data[20] == 64:
        if data[21] == 0:
            #class 2
            pyautogui.keyDown('d')
        elif data[21] == 64:
            #class 3
            pyautogui.keyUp('right')
        elif data[21] == 128:
            #class 4
            pyautogui.keyUp('d')
        elif data[21] == 160:
            #class 5
            print("Action Unassigned, class 5")
        elif data[21] == 192:
            #class 6
            print("action Unassigned, class 6")
        elif data[21] == 224:
            #class 7
            print("action Unassigned, class 7")
    else:
        # class 1
        pyautogui.keyDown('right')


    time.sleep(1)
