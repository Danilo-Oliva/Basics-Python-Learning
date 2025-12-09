from PySide6.QtWidgets import *

class myFirstWindow(QMainWindow):
  def setupUi(self):
    self.setFixedSize(500, 500)
    
##ejecutar app
import sys 
app = QApplication(sys.argv)

window = myFirstWindow()
window.setupUi()
window.show()

sys.exit(app.exec_())