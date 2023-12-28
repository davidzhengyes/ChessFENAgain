from PyQt6 import uic
from PyQt6.QtWidgets import QApplication

def prpr():
    print("signal yes")

Form, Window = uic.loadUiType("untitled.ui")
print("hi")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()