class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def edad(self):
        return self._edad
    
    @edad.setter
    def edad(self, edad):
        if edad < 0:
            raise ValueError("La edad no puede ser negativa")
        self._edad = edad
    
    @property
    def dni(self):
        return self._dni
    
    @dni.setter
    def dni(self, dni):
        if len(dni) != 9:
            raise ValueError("El DNI debe tener 9 caracteres")
        self._dni = dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}")
    
    def es_mayor_de_edad(self):
        return self.edad >= 18