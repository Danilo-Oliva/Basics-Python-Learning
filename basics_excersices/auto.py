class Vehiculo:
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    
  def mostrarInfo(self):
    print(f"El vehiculo es de marca: {self.marca} y modelo: {self.modelo}")
    
class Auto(Vehiculo):
  def __init__(self, marca, modelo, puertas):
    super().__init__(marca, modelo)
    self.puertas = puertas
    
  def mostrarInfo(self):
    super().mostrarInfo()
    print(f"Cantidad de puertas: {self.puertas}")
    
moto = Vehiculo("Yamaha", "wave")
auto = Auto("Koenigsegg","Jesko", 4)

moto.mostrarInfo()
auto.mostrarInfo()