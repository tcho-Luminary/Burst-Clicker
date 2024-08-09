import pyautogui
import keyboard
import time
import random
from pynput.mouse import Listener

print("Welcome to burst Clicker!")
print("Type 'R' to activate double clicker")
print("Write 'Clicker' to activate clicker and write your cps eg; 12-18")

def get_cps_input():
    cps_range = input("Enter CPS range (eg; 12-18): ")
    cps_range = cps_range.split("-")
    return int(cps_range[0]), int(cps_range[1])

def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        if keyboard.read_key() == "u":
            pyautogui.click()

def autoclick(cps_range):
    cps_min, cps_max = cps_range
    while True:
        if keyboard.is_pressed("r"):
            break


def main():
    while True:
        command = input("Enter command: ")
        if command == "r":
            autoclick(get_cps_input())
        elif command == "clicker":
            autoclick(get_cps_input())
        else:
            print("Invalid command. Try again!")

if __name__ == "__main__":
    main()

###


