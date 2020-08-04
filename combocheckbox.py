
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel, QComboBox, QPushButton, QCheckBox

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()        
        combo = QComboBox(self)
        combo.addItem("Apple")
        combo.addItem("Pear")
        combo.addItem("Lemon")

        combo.move(50, 10)
        self.grid.addWidget(combo, 0,0)

        self.qlabel = QLabel(self)
        self.grid.addWidget(self.qlabel, 1,0)

        combo.activated[str].connect(self.onChanged)      

        cb2 = QCheckBox('Music', self)
        self.grid.addWidget(cb2, 2,0)
        cb2.toggle()

        self.setLayout(self.grid)
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QLineEdit Example")
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())