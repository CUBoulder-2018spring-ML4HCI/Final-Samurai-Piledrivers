import pyautogui
import time
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

while(1):
    pyautogui.keyDown('right')
    pyautogui.keyUp('a')
    pyautogui.keyUp('s')
    pyautogui.keyDown('d')

    time.sleep(1)
