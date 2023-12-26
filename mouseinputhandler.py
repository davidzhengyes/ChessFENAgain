import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys
from pynput.mouse import Listener

global clickedOnce,topleft,bottomright

def is_clicked(x, y, button, pressed):
    #pressed as opposed to released
    global clickedOnce
    if pressed and clickedOnce:
        global bottomright
        bottomright=(x,y)
        return False #in your case, you can move it to some other pos
        # to stop the thread after click
    elif pressed:
        global topleft
        topleft=(x,y)
        clickedOnce=True

def topleftcoord():
    #need bool to set if mouse clicked or whatever
    global clickedOnce
    clickedOnce=False
    with Listener(on_click=is_clicked) as listener:
        listener.join()
#will wait for it to return false to end this listener block.
    #meaning, whenever needed, can call this listener block when the button is pressed
    #need to return false to continue the code.
        
    # tlX,tlY=pyautogui.position()
    # print(tlX,tlY) #probably can't use this as it only gets run after the listener block
        #is finished, the method inside returning false
    print(topleft,bottomright)

