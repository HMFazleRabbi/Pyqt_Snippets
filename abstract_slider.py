from PyQt5 import QtCore, QtGui, QtWidgets
from power_bar_flex import PowerBar 


app = QtWidgets.QApplication([])
volume = PowerBar(steps=10)
volume.show()
app.exec_()