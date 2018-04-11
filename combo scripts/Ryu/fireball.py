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
        pyautogui.keyDown('k')

        pyautogui.keyUp('j')
        #time.sleep(.0001)
        pyautogui.keyDown('s')
        pyautogui.keyUp('k')
        #time.sleep(.0001)S

        pyautogui.keyUp('s')
        #time.sleep(1)

        '''pyautogui.keyDown('j')
        pyautogui.keyUp('j')
        time.sleep(.001)
        pyautogui.keyDown('k')
        pyautogui.keyUp('k')
        time.sleep(.001)

        pyautogui.keyDown('s')


        #pyautogui.keyDown('right')

        #pyautogui.keyDown('d')
        pyautogui.keyUp('s')
        time.sleep(.01)
        time.sleep(1)

        #pyautogui.hotkey('down', 'right', )
        #pyautogui.typewrite('', interval=0.25)'''
