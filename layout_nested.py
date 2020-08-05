import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QStackedLayout, QTabWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPalette, QColor


class Color(QWidget):

    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)
        
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")

        layout1 = QHBoxLayout()
        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        layout1.setContentsMargins(50,10,0,0)
        layout1.setSpacing(0)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        layout1.addLayout( layout2 )

        layout1.addWidget(Color('green'))

        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))
        
        layout1.addLayout( layout3 )
        
        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)

class MainWindowStacked (QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindowStacked, self).__init__(*args, **kwargs)
        
        self.setWindowTitle("My Awesome App")


        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.North)
        tabs.setMovable(True)

        for n, color in enumerate(['red','green','blue','yellow']):
            tabs.addTab( Color(color), color)

        self.setCentralWidget(tabs)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindowStacked()
    ex.show()
    sys.exit(app.exec_())
    