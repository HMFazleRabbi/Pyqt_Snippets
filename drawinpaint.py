import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.painter = QtGui.QPainter(self.label.pixmap())
        self.prev=None

        self.drawpaper()
        self.setCentralWidget(self.label)
        

    def drawpaper(self):
        pen = QtGui.QPen()
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('white'))
        brush.setStyle(Qt.Dense1Pattern)
        pen.setWidth(2)
        pen.setColor(QtGui.QColor('green'))
        self.painter.setPen(pen)
        self.painter.setBrush(brush)
        self.painter.drawRect(10,10, 380, 280)


    def mouseMoveEvent(self, e):
        if self.prev is None:
            self.prev = QtCore.QPoint(e.x(), e.y())
            self.painter.drawPoint(e.x(), e.y())
        else:
            self.painter.drawLine(self.prev, QtCore.QPoint(e.x(), e.y()))
            self.prev = QtCore.QPoint(e.x(), e.y())

        self.update()

    def mouseReleaseEvent(self, e):
        self.prev=None

        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()