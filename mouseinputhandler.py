#can rename later, mouse+buttons handler
import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys
from pynput.mouse import Listener
import calculations

global clickedOnce,topleft,bottomright
global gametopleft,gamebottomright
global file

#for setting screenshot coords.
def is_clicked(x, y, button, pressed):
    #pressed as opposed to released
    global file
    global clickedOnce
    if pressed and clickedOnce:
        global bottomright
        bottomright=(x,y)
        file.writelines(str(bottomright[0])+"\n")
        file.writelines(str(bottomright[1])+"\n")
        print(bottomright)
        
        return False #in your case, you can move it to some other pos
        # to stop the thread after click
    elif pressed:
        global topleft
        topleft=(x,y)
        clickedOnce=True
        file=open("presets.txt","r+")
        file.writelines(str(topleft[0])+"\n")
        file.writelines(str(topleft[1])+"\n")
        print(topleft)

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

#MIGHT NEED A SEPARATE CLICKEDONCE BOOL
def isgameboardclicked(x, y, button, pressed):
    global clickedOnce
    global file
    
    if pressed and clickedOnce:
        global gamebottomright
        gamebottomright=(x,y)
    
        file.writelines(str(gamebottomright[0])+"\n")
        file.writelines(str(gamebottomright[1])+"\n")
        print(gamebottomright)
        file.close()
        return False 
    
    elif pressed:
        global gametopleft
        gametopleft=(x,y)
        clickedOnce=True
      
        file.writelines(str(gametopleft[0])+"\n")
        file.writelines(str(gametopleft[1])+"\n")
        print(gametopleft)
       
def setGameBoardCoords():
    global clickedOnce
    clickedOnce=False
    with Listener(on_click=isgameboardclicked) as listener:
        listener.join()
   
def startCalc():
    file=open("presets.txt","r+")
    a=file.readlines()
    global topleft,bottomright
    topleft=(int(a[4]),int(a[5]))
    bottomright=(int(a[6]),int(a[7]))
    calculations.locateAll(topleft,bottomright)
    #have some default run, if topleft,bottomright are both null, do something 

def extrasScreenshots():
    #can only be used after these have been defined.
    calculations.extrasScreenshots(topleft,bottomright)