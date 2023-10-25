from abc import ABC, abstractmethod

class Celular():
    def __init__(self, builder):
        self.modelo = builder.modelo
        self.marca = builder.marca
        self.color = builder.color
        self.numero = builder.numero

    
    def _str_(self):
        return f"Celular =  marca: {self.marca} | modelo: {self.modelo} | color:{self.color}"