import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import cv2, statistics 



def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   grid = QGridLayout()

   button1 = QPushButton("Threshold")
   button1.clicked.connect(load)
   grid.addWidget(button1, 2,1)

   widget.setLayout(grid)
   widget.setGeometry(50,50,200,200)
   widget.setWindowTitle("PyQt5 Example")
   widget.show()
   sys.exit(app.exec_())
   cv2.destroyAllWindows()

def load():
   img = cv2.imread("D:/FZ_WS/JyNB/Yolo_Pad_WS/Yolo_Pad_00/data/dataset/A-Dataset-01/Pad Detection/Dataset/Good Dataset/49043BottomPackage/49043Bottom_6_3_2.jpg")
   bordersize=5
   img= cv2.copyMakeBorder(
    img,
    top=bordersize,
    bottom=bordersize,
    left=bordersize,
    right=bordersize,
    borderType=cv2.BORDER_CONSTANT,
    value=[0, 0, 0]
   )
   ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

   # Grayscale 
   gray = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY) 

   # Find Canny edges 
   edged = cv2.Canny(gray, 30, 200)  
   cv2.imshow("edged", edged)

   # Finding Contours 
   # Use a copy of the image e.g. edged.copy() 
   # since findContours alters the image 
   contours, hierarchy = cv2.findContours(edged,  
   cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
   print("Number of contours:\t", len(contours))

   # Boundary boxes
   sorted_contours = sorted( contours, key=cv2.contourArea, reverse=True)

   # Draw all contours 
   # -1 signifies drawing all contours 
   for c in sorted_contours:
      x,y,w,h = cv2.boundingRect(c)
      if (w > 10 and h >10):
         cv2.rectangle(img,(x,y),(x+w,y+h),(100,0,200),5)
         cv2.drawContours(img, [c], -1, (0, 255, 0), 2) 


   cv2.imshow("Original", img)
   cv2.imshow("THRESH_BINARY", thresh1)



if __name__ == '__main__':
   window()