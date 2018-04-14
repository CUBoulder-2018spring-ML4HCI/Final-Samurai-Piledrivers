import pyautogui
import time
#jks

while(1):
        pyautogui.keyDown('h')
        time.sleep(2)
        pyautogui.keyDown('k')
        pyautogui.keyDown('d')
        pyautogui.keyUp('h')
        pyautogui.keyUp('k')
        pyautogui.keyUp('d')