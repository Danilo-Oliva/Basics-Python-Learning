class Vehiculo:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
  
  def mostrarInfo(self):
    return f"Vehiculo: {self.marca} {self.modelo}"

class Auto(Vehiculo):
  def __init__(self, marca, modelo, puertas):
    super().__init__(marca, modelo)
    self.puertas = puertas
    
  def mostrarInfo(self):
    return f"Auto: {self.marca} {self.modelo} {self.puertas} puertas"

class Moto(Vehiculo):
  def __init__(self, marca, modelo, cilindrada):
    super().__init__(marca, modelo)
    self.cilindrada = cilindrada
  
  def mostrarInfo(self):
    return f"Moto: {self.marca} {self.modelo} {self.cilindrada}cc"