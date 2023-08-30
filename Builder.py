class Bicicleta():
    def __init__(self, builder):
        self.rodado = builder.rodado
        self.marca = builder.marca
        self.color = builder.color

class BicicletaBuilder():
    def withRodado(self, rodado):
        self.rodado = rodado
        return self
    
    def withMarca(self, marca):
        self.marca = marca
        return self
    
    def withColor(self, color):
        self.color = color
        return self
    
    def build(self):
        return Bicicleta(self)
    
builder = BicicletaBuilder()
bicicleta = builder.withRodado(26).withMarca("MarcaXYZ").withColor("Rojo").build()

print(bicicleta.rodado)  
print(bicicleta.marca)   
print(bicicleta.color)   