import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QPushButton
import mouseinputhandler as mh
import calculations


def run():
    app=QApplication([])

    window = QWidget()
    window.setWindowTitle("ChessFEN Helper")
    window.setGeometry(1200, 400, 280, 200)
    helloMsg = QLabel("<h1>Hello, World!</h1>", parent=window)
    helloMsg.move(60, 15)

    button = QPushButton("Greet",parent=window)
    button.move(30,0)
    button.move(0,50)
    button.clicked.connect(calculations.scanrook)

    TLcoordButton = QPushButton("Top-Left Selection", parent=window)

    TLcoordButton.clicked.connect(mh.topleftcoord)
    #TLcoordButton.hide()
    TLcoordButton.setText("Abc")

    extrasButton = QPushButton("Scan Extras", parent=window)
    extrasButton.move(0,30)
    extrasButton.clicked.connect(mh.extrasScreenshots)


    window.show()



    sys.exit(app.exec())