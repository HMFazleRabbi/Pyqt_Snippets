
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QStyleFactory, QVBoxLayout, QLabel, QComboBox, QPushButton, QCheckBox

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()        
        combo = QComboBox(self)
        combo.addItem("Apple")
        combo.addItem("Pear")
        combo.addItem("Lemon")
        combo.activated[str].connect(self.onChanged)      
        self.layout.addWidget(combo)

        self.qlabel = QLabel(self)
        self.layout.addWidget(self.qlabel)


        cb2 = QCheckBox('Music', self)
        self.layout.addWidget(cb2)
        cb2.toggle()

        self.setLayout(self.layout)
        self.setGeometry(50,50,320,200)
        self.setWindowTitle("QLineEdit Example")
        print(QStyleFactory.keys())
        self.show()

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())