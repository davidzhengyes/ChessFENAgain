import sys
import mouseinputhandler as mh
import calculations

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt6.uic import loadUi

from tester import Ui_MainWindow

def printmeow():
    print("meow")

global win

#need something for radio button onclick as well.
class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def showText(self,text):
        self.plainTextEdit.setPlainText(text)

    def printText(self):
        print(self.plainTextEdit.toPlainText())
        print(self.radioButton.isChecked())
        self.plainTextEdit.setPlainText("Rawr!")
    def setRadioText(self):
        button1pressed=self.radioButton.isChecked()
        if button1pressed:
            self.plainTextEdit.setPlainText("White to Move")
        else:
            self.plainTextEdit.setPlainText("Black to Move")

    def connectSignalsSlots(self):
        self.pushButton_3.clicked.connect(self.printText)
    #     self.action_Exit.triggered.connect(self.close)

        self.subwindow_0.clicked.connect(self.findAndReplace)

        self.radioButton.clicked.connect(self.setRadioText)
        self.radioButton_2.clicked.connect(self.setRadioText)
        self.getFEN.clicked.connect(mh.startCalc)
    #     self.action_About.triggered.connect(self.about)
  
        print(self.radioButton.isChecked())

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.pushButton.clicked.connect(mh.topleftcoord)
        dialog.pushButton_2.clicked.connect(mh.extrasScreenshots)
        dialog.pushButton_3.clicked.connect(mh.setGameBoardCoords)
        dialog.exec()

    def about(self):
        QMessageBox.about(
            self,
            "About Sample Editor",
            "<p>A sample text editor app built with:</p>"
            "<p>- PyQt</p>"
            "<p>- Qt Designer</p>"
            "<p>- Python</p>",
        )

class FindReplaceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi("subwindow.ui", self)

def run():
    global win
    print('run1')
    print(__name__)
    
    print("run2")
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

# print(win.self.plainTextEdit.text())
# print("hi")