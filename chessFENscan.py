
import mouseinputhandler as mh
from pynput.mouse import Listener
import timeit
import gui
import apptester
#installed requires pyqt6, pyautogui, pillow, opencv, pynput
#maybe i DO need the images to be in the same folder.
#note that analysis board is shifted relative to the game board bc analysis bar
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





    #so should work even with another window over the one you want to look at. so directly 
    #analyzes screen, as it should.


apptester.run()
















#NOTES
#https://stackoverflow.com/questions/39235454/how-to-know-if-the-left-mouse-click-is-pressed
#(PyautoGUI can't detect keystrokes)