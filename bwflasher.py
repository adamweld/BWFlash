from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle("BWFlasher")
        self.UiComponents()
        self.show()

    def UiComponents(self):
        button = QPushButton("", self)
        button.setGeometry(0, 0, 1280, 720)
        button.setStyleSheet("QPushButton"
                             "{"
                             "background-color : black;"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : white;"
                             "}"
                             )
        button.clicked.connect(self.clickme)
        self.showFullScreen()
  
    def clickme(self):
        print("pressed")

 
app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
