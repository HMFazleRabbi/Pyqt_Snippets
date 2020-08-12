import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QtWidgets.QLabel()
        canvas = QtGui.QPixmap(400, 300)
        self.label.setPixmap(canvas)
        self.initialize_painter()
        self.setCentralWidget(self.label)
        self.draw_line()
        self.draw_rect()

    def drawpaper(self):
        pen = QtGui.Pen()
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor('white'))
        brush.setStyle(Qt.Dense1Pattern)
        pen.setWidth(2)
        pen.setColor(QtGui.QColor('green'))
        self.painter.setPen(pen)
        self.painter.drawRect(10,10, 36, 260)


    def initialize_painter(self):
        painter = QtGui.QPainter(self.label.pixmap())
        pen = QtGui.QPen()
        pen.setColor(QtGui.QColor('green'))
        pen.setWidth(3)
        painter.setPen(pen)
        self.painter = painter
        


    def draw_line(self):
        
        pen = self.painter.pen()
        pen.setWidth(5)
        pen.setColor(QtGui.QColor('red'))
        self.painter.setPen(pen)
        self.painter.drawLine(10, 10, 300, 200)
    
    def draw_rect(self):
        
        pen = self.painter.pen()
        brush = QtGui.QBrush()
        brush.setColor(QtGui.QColor("#FFD141"))
        brush.setStyle(Qt.Dense1Pattern)
        pen.setWidth(2)
        pen.setColor(QtGui.QColor('green'))
        self.painter.setPen(pen)
        self.painter.setBrush(brush)
        self.painter.drawRect(50, 50, 100, 100)
        self.painter.drawRect(60, 60, 150, 100)
        self.painter.drawRect(70, 70, 100, 150)
        self.painter.drawRect(80, 80, 150, 100)
        self.painter.drawRect(90, 90, 100, 150)
        self.painter.end()

    def mouseMoveEvent(self, e):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawPoint(e.x(), e.y())

        

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()