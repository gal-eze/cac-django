from datetime import date
from Cuenta import Cuenta
from Persona import Persona


class CuentaJoven(Cuenta):
    def __init__(self, titular: Persona, cantidad: float = 0, bonificacion: float = 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion
    
    @property
    def bonificacion(self):
        return self._bonificacion
    
    @bonificacion.setter
    def bonificacion(self, value):
        if value < 0:
            raise ValueError("La bonificación debe ser un número positivo")
        self._bonificacion = value
    
    def es_titular_valido(self):
        return self.titular.es_mayor_de_edad() and self.titular.edad < 25
    
    def retirar(self, cantidad: float):
        if not self.es_titular_valido():
            print("El titular no es válido para retirar dinero")
            return
        super().retirar(cantidad)
    
    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self.titular}\nBonificación: {self.bonificacion}"