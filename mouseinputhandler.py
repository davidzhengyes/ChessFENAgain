import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys
from pynput.mouse import Listener

def is_clicked(x, y, button, pressed):
    if pressed:
        print('Clicked ! ')
        return False #in your case, you can move it to some other pos
        # to stop the thread after click

def topleftcoord():
    #need bool to set if mouse clicked or whatever
    with Listener(on_click=is_clicked) as listener:
        listener.join()
#will wait for it to return false to end this listener block.
    #meaning, whenever needed, can call this listener block when the button is pressed
    #need to return false to continue the code.
    tlX,tlY=pyautogui.position()
    print(tlX,tlY)
    print("hi")

