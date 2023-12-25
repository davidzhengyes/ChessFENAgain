import pyautogui
import time
import math
from PyQt6.QtWidgets import QApplication, QLabel, QWidget
import sys
#maybe i DO need the images to be in the same folder.

#instead of time.sleep, can use a gui to start the process.
#don't even need to calculate coords. once images are located, can just sort them.
#screenshots of each piece have an error, so the coordinates given by pyautogui will be a little skew
#error tolerance

#https://stackoverflow.com/questions/69864949/how-to-detect-an-image-and-click-it-with-pyautogui
#could even have quicksetup at beginning of a match to autodetect pieces.

#possibly have it make new screenshot files so user doesn't have to make new presets every time.
#have a default FEN in analysis, with instructions so machine captures one of each piece on each colour.


time.sleep(5)
img="newrook.PNG"
a= pyautogui.locateAllOnScreen(img,grayscale=True,confidence=0.9)
for x in a:
    print(x)


    #so should work even with another window over the one you want to look at. so directly 
    #analyzes screen, as it should.


app=QApplication([])

window = QWidget()
window.setWindowTitle("PyQt App")
window.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
helloMsg.move(60, 15)

window.show()
sys.exit(app.exec())