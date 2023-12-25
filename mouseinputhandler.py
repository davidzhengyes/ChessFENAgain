import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys

def is_clicked(x, y, button, pressed):
    if pressed:
        print('Clicked ! ')
        return False #in your case, you can move it to some other pos
        # to stop the thread after click

def topleftcoord():
    #need bool to set if mouse clicked or whatever
    tlX,tlY=pyautogui.position()
    print(tlX,tlY)
    print("hi")

