import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import cv2, statistics 

class MainPage(QWidget):
    
    def __init__(self):
        super().__init__()

        self.grid = QGridLayout()

        self.lineEntry = QLineEdit(self)
        self.lineEntry.resize(200,40)
        self.qlabel = QLabel(self)
        self.lineEntry.textChanged.connect(self.onChanged)
        self.grid.addWidget(self.lineEntry, 1, 0)
        self.grid.addWidget(self.qlabel, 3, 0)

        self.setLayout(self.grid)
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainPage()
    sys.exit(app.exec_())