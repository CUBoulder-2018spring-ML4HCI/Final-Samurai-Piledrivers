import pyautogui
import time
#jks

while(1):
        pyautogui.keyDown('h')
        time.sleep(2)
        pyautogui.keyDown('k')
        pyautogui.keyDown('s')
        pyautogui.keyUp('h')
        pyautogui.keyUp('k')
        pyautogui.keyUp('s')