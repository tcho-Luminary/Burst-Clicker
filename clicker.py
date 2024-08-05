import pyautogui
import time

def double_click():
while True:
if win32api.GetKeyState(0x01) < 0:
time.sleep(0.2)
pyautogui.doubleClick()
else:
pass
