from PySide6.QtWidgets import *

class myFirstWindow(QMainWindow):
  def setupUi(self):
    self.setFixedSize(500, 330)
    
    self.frame1 = QFrame(self)
    self.frame1.setGeometry(10, 10, 480, 100)
    self.frame1.setStyleSheet("background-color: #0CA8AC;")
    
    self.frame2 = QFrame(self)
    self.frame2.setGeometry(10, 120, 480, 200)
    self.frame2.setStyleSheet("background-color: #0CA8AC;")
    
    
import sys
app = QApplication(sys.argv)

window = myFirstWindow()
window.setupUi()
window.show()

sys.exit(app.exec_())#Para que no se cierre automaticamente