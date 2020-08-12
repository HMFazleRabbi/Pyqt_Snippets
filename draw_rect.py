from PyQt5 import QtCore, QtGui, QtWidgets
from selection_rect import Rectangle 


app = QtWidgets.QApplication([])
rect = Rectangle()
rect.show()
app.exec_()

