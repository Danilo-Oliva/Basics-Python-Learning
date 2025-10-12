from PySide6.QtWidgets import *
from PySide6.QtCore import *

class myFirstWindow(QMainWindow):
  def setupUi(self):
    self.setFixedSize(500, 330)
    
    self.fr_titulo = QFrame(self)
    self.fr_titulo.setGeometry(10, 10, 480, 100)
    self.fr_titulo.setStyleSheet("background-color: #0CA8AC;")
    
    #texto del titulo
    self.titulo = QLabel(self.fr_titulo)
    self.titulo.setText("Hola")
    self.titulo.setGeometry(QRect(0, 20, 480, 20))
    self.titulo.setAlignment(Qt.AlignCenter)
    self.titulo.setStyleSheet('''
      color : White;
      font-size: 25px;
      font-weight: bold;
                              ''')
    
    self.fr_inputs = QFrame(self)
    self.fr_inputs.setGeometry(10, 120, 480, 200)
    self.fr_inputs.setStyleSheet("background-color: #0CA8AC;")
    
    #texto del input
    self.header = QLabel(self.fr_inputs)
    self.header.setText("Ingresa tu nombre")
    self.header.setGeometry(QRect(0, 20, 480, 35))
    self.header.setAlignment(Qt.AlignCenter)
    self.header.setStyleSheet(
      '''
        color: White;
        font-size: 25px;
        font-weight: bold;
      '''
    )
    
    #input
    self.input = QLineEdit(self.fr_inputs)
    self.input.setGeometry(QRect(10, 70, 460, 45))
    self.input.setAlignment(Qt.AlignCenter)
    self.input.setStyleSheet(
      '''
      color: black;
      font-weight: bold;
      background-color: white;
      '''
    )
    
    #boton
    self.boton = QPushButton(self.fr_inputs)
    self.boton.setText("Click me!")
    self.boton.clicked.connect(self.obtenerTexto)
    self.boton.setGeometry(QRect(10, 125, 460, 45))
    self.boton.setStyleSheet(
      '''
      color: black;
      font-weight: bold;
      '''
    )
    
    #cuadro de dialogo
    self.dialogo = QDialog(self)
    self.dialogo.setFixedSize(300, 300)
    
    #frames del dialogo
    self.fr_titulo_dialogos = QFrame(self.dialogo)
    self.fr_titulo_dialogos.setGeometry(QRect(10, 10, 280, 100))
    self.fr_titulo_dialogos.setStyleSheet("background-color: #0CA8AC")
    
    #texto del dialogo
    self.titulo_dialogo = QLabel(self.fr_titulo_dialogos)
    self.titulo_dialogo.setGeometry(QRect(0, 0, 280, 100))
    self.titulo_dialogo.setAlignment(Qt.AlignCenter)
    self.titulo_dialogo.setStyleSheet(
      '''
      color: white;
      font-size: 25px;
      font-weight:bold;
      '''
    )
    
    #frame de imagen
    self.fr_img = QFrame(self.dialogo)
    self.fr_img.setGeometry(QRect(10, 120, 280, 170))
    self.fr_img.setStyleSheet("background: url(PySide6/image.png)")

  def obtenerTexto(self):
    self.titulo_dialogo.setText(f"Bienvenido {self.input.text()}!")
    self.dialogo.show()
    print(self.input.text())    

import sys
app = QApplication(sys.argv)

window = myFirstWindow()
window.setupUi()
window.show()

sys.exit(app.exec())#Para que no se cierre automaticamente