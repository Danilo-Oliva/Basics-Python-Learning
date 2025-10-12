from PySide6.QtCore import *
from PySide6.QtWidgets import *

class Menu(QMainWindow):
  def setupUi(self):
    self.size = QSize(450, 500)
    self.setStyleSheet("background-color: white;")
    
    self.root_layout = QVBoxLayout()
    
    self.fr_titulo = QFrame()
    self.fr_titulo.setStyleSheet("background-color : gray;")
    self.fr_inputs = QFrame()
    self.fr_inputs.setStyleSheet("background-color : gray;")
    
    self.root_layout.addWidget(self.fr_titulo, 30)
    self.root_layout.addWidget(self.fr_inputs, 70)
    
    self.widget = QWidget()
    self.widget.setLayout(self.root_layout)
    
    self.setCentralWidget(self.widget)
    self.setup_inputs_frame()
    self.setup_title_trame()
    
  def setup_title_trame(self):
    self.title = QLabel("TIC TAC TOE", alignment= Qt.AlignCenter)
    
    self.title_layout = QVBoxLayout()
    self.title_layout.addWidget(self.title)
    
    self.fr_titulo.setLayout(self.title_layout)
    
  def setup_inputs_frame(self):
    self.input_title = QLabel("Ingrese le nombre de los jugadores", alignment= Qt.AlignCenter)
    self.player_1 = QLineEdit()
    self.player_2 = QLineEdit()
    self.play_button = QPushButton()
    
    self.inputs_layouts = QVBoxLayout()
    self.inputs_layouts.addWidget(self.input_title)
    self.inputs_layouts.addWidget(self.player_1)
    self.inputs_layouts.addWidget(self.player_2)
    self.inputs_layouts.addWidget(self.play_button)
    self.inputs_layouts.addStretch()
    
    self.fr_inputs.setLayout(self.inputs_layouts)
  
#ejecutar aplicacion
import sys
app = QApplication(sys.argv)

menu = Menu()
menu.setupUi()
menu.show()

sys.exit(app.exec())