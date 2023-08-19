class Auto:
    cantidadCreados = 0
    def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # Array de asientos []
        self.marca = marca
        self.motor = motor  # Atributo de referencia de Motor
        self.registro = registro
    
    def cantidadAsientos(self):
        cantidad = 0
        for i in self.asientos:
            if i != None:
                cantidad += 1
        return cantidad
    
    def verificarIntegridad(self):
        verificacion = True
        for i in self.asientos:
            if i != None:
                if i.registro != self.registro:
                    verificacion = False
        if self.motor.registro == self.registro and verificacion:
            print("Auto original")
        else:
            print("Las piezas no son originales")

class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self,color):
        permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in permitidos:
            self.color = color

class Motor:
    def __init__(self,numeroCilindros,tipo,registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self,registro):
        self.registro = registro
        
    def asignarTipo(self,tipo):
        posibles = ["electrico","gasolina"]
        if tipo in posibles:
            self.tipo = tipo