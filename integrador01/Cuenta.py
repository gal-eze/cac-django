from Persona import Persona

class Cuenta:
    def __init__(self, titular:Persona, cantidad=0):
        self.__titular = titular
        self.__cantidad = cantidad
    
    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self, nuevo_titular):
        self.__titular = nuevo_titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    def mostrar(self):
        print("Titular:", self.__titular.mostrar())
        print("Cantidad:", self.__cantidad)
        
    def ingresar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad
        
    def retirar(self, cantidad):
        if cantidad > 0:
            self.__cantidad -= cantidad