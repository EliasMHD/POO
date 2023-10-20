from service.Celular import Celular

class CelularBuilder():
    def withModelo(self, modelo):
        self.modelo = modelo
        return self

    def withMarca(self, marca):
        self.marca = marca
        return self

    def withColor(self, color):
        self.color = color
        return self

    def withNumero(self, numero):
        self.numero = numero
        return self

    def build(self):
        return Celular(self)
