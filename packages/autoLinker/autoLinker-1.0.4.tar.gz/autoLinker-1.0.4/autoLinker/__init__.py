import pyautogui
import keyboard
name = "example_pkg"
from . import *
def click(direction,interval,key1,key2):
    while True:
        if keyboard.is_pressed(key1) :
            while True:
                if direction=="left":
                    pyautogui.click(interval=interval)
                if direction=="right":
                    pyautogui.rightClick(interval=interval)
                if keyboard.is_pressed(key2) :
                    break
