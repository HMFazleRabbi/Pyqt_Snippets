import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
import cv2


class _Rectangle(QtWidgets.QLabel):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding
        )

        self._bar_solid_percent = 0.8
        self._background_color = QtGui.QColor('black')
        self._padding = 4.0  # n-pixel gap around edge.
        
        
        self.x0 = 0
        self.y0 = 0
        self.x1 = 0
        self.y1 = 0
        self.flag = False
        

    def sizeHint(self):
        return QtCore.QSize(40,120)
        
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QtGui.QPainter(self.pixmap())
        brush = painter.brush()
        brush.setColor(self._background_color)
        brush.setStyle(Qt.SolidPattern)


        rect = QtCore.QRect(self.x0, self.y0, abs(self.x1-self.x0), abs(self.y1-self.y0))
        painter.setPen(QtGui.QPen(QtGui.QColor('green'), 3, Qt.SolidLine))
        painter.drawRect(rect)
        brush.setColor(QtGui.QColor('blue'))
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)
        painter.fillRect(rect, brush)
        print("x0, y0, x1, y1:\t", self.x0, self.y0, self.x1, self.y1);
        painter.end()
        

    def mouseMoveEvent(self, e):
        if (self.flag):
            self.x1, self.y1 = e.x(), e.y()
            self.update()

    def mousePressEvent(self, e):
        self.x0, self.y0 = e.x(), e.y()
        self.flag = True
        self.setCursor(Qt.CrossCursor)

    def mouseReleaseEvent(self, e):
        self.flag = False
        

        
    def __getattr__(self, name):
        if name in self.__dict__:
            return self[name]

        return getattr(self._dial, name)
    

class Rectangle(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label = _Rectangle()

        # Read image
        img = cv2.imread('C:/Users/V510/Desktop/AutoML/BlackLittleBoardT-BlackLittleBoardT_1_2_2-187.jpg')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QtGui.QImage(img.data, width, height, bytesPerLine,QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(QImg)

        # Read Pixmap
        self.label.setPixmap(pixmap)
        layout = QtWidgets.QVBoxLayout()
        
        layout.addWidget(self.label)       
        self.setLayout(layout)
        

