import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import sys
import mouseinputhandler as mh
from pynput.mouse import Listener
#installed requires pyqt6, pyautogui, pillow, opencv, pynput
#maybe i DO need the images to be in the same folder.
#next steps: compile to exe? 

#try-except to handle imagenotfoundexception, maybe to indicate recalibration needed.#
#https://www.w3schools.com/python/python_try_except.asp


#instead of time.sleep, can use a gui to start the process.
#don't even need to calculate coords. once images are located, can just sort them.
#screenshots of each piece have an error, so the coordinates given by pyautogui will be a little skew
#error tolerance

#https://stackoverflow.com/questions/69864949/how-to-detect-an-image-and-click-it-with-pyautogui
#could even have quicksetup at beginning of a match to autodetect pieces.

#possibly have it make new screenshot files so user doesn't have to make new presets every time.
#have a default FEN in analysis, with instructions so machine captures one of each piece on each colour.

def scanrook():
    img="newrook.PNG"

    try:
        a= pyautogui.locateAllOnScreen(img,grayscale=True,confidence=0.95)
        for x in a:
            print(x)

    except:
        print("Not found")
    else:

        pass #does what happens if except odesn't run, 
    #cannot put the for x in a here because will reference a again.
    
    finally: 
        pyautogui.moveTo(100, 150)
        #https://stackoverflow.com/questions/1181464/controlling-mouse-with-python
        print(pyautogui.position()[0])
        print("Woohoo!")



    #so should work even with another window over the one you want to look at. so directly 
    #analyzes screen, as it should.



app=QApplication([])

window = QWidget()
window.setWindowTitle("ChessFEN Helper")
window.setGeometry(1200, 400, 280, 200)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

button = QPushButton("Greet",parent=window)
button.move(30,0)
button.clicked.connect(scanrook)

TLcoordButton = QPushButton("Top-Left Selection", parent=window)
button.move(0,50)
TLcoordButton.clicked.connect(mh.topleftcoord)




with Listener(on_click=mh.is_clicked) as listener:
    listener.join()
#will wait for it to return false to end this listener block.
    #meaning, whenever needed, can call this listener block when the button is pressed
    #need to return false to continue the code.
window.show()


sys.exit(app.exec())















#NOTES
#https://stackoverflow.com/questions/39235454/how-to-know-if-the-left-mouse-click-is-pressed
#(PyautoGUI can't detect keystrokes)