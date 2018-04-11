import pyautogui
import time
#jks

while(1):
        #pyautogui.press(['down', 'right', 's'])
        #time.sleep(1)

        #pyautogui.typewrite('jks', interval=0.25)
        #pyautogui.press('j')
        #time.sleep(.001)
        #pyautogui.press('s')
        #time.sleep(.001)
        pyautogui.keyDown('j')
        pyautogui.keyDown('h')

        pyautogui.keyUp('j')
        #time.sleep(.0001)
        pyautogui.keyDown('d')
        pyautogui.keyUp('h')
        #time.sleep(.0001)S

        pyautogui.keyUp('d')
