import keyboard
import time
import clicker

toggle = False

def start():
global toggle
while True:
if keyboard.is_pressed("r"):
toggle = not toggle
if toggle:
print("double clicker activated. Press R again to deactivate.")
else:
print("double clicker deactivated. Press R again to activate.")
time.sleep(0.1)
if toggle:
clicker.double_click()
