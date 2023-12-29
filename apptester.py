import sys

from PyQt6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt6.uic import loadUi

from tester import Ui_MainWindow

def printmeow():
    print("meow")

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def printText(self):
        print(self.plainTextEdit.toPlainText())
    def connectSignalsSlots(self):
        self.pushButton_3.clicked.connect(self.printText)
    #     self.action_Exit.triggered.connect(self.close)
        self.subwindow_0.clicked.connect(self.toMoveStatus)
        self.subwindow_0.clicked.connect(self.findAndReplace)
        
    #     self.action_About.triggered.connect(self.about)
    def toMoveStatus(self):
        print(self.radioButton.isChecked())

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.pushButton.clicked.connect(printmeow)
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())

print(win.self.plainTextEdit.text())
print("hi")