#can rename later, mouse+buttons handler
import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys
from pynput.mouse import Listener
import calculations

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

#rename later, this is to take screenshots of pieces
        #add a check, so it can't be clicked twice before the screenshot is taken
        #crashes.
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
    
    #remember to handle negative height $ width
    
    #running this again overwrites the images.
    #remember when taking these screenshots, MIGHT NOT scan exactly back into the browser?
    #not sure. but the pixels should still be exact,, not changing ratio so should be ok
    print("run")
    print(topleft,bottomright)
    calculations.takeGeneralScreenshots(topleft,bottomright)
   

def extrasScreenshots():
    #can only be used after these have been defined.
    calculations.extrasScreenshots(topleft,bottomright)