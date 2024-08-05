import win32api
import pyautogui
import keyboard
import time

p = print
toggle = False

p("Welcome to burst Clicker")
p("Type r to activate double clicker")


def check_mouse_click():
    while True:
        if win32api.GetKeyState(0x01) < 0:
            time.sleep(0.2)
            pyautogui.click()
        else:
            pass


while True:
    if keyboard.is_pressed("r"):
        toggle = not toggle
        time.sleep(0.1)
    if toggle:
        check_mouse_click()
