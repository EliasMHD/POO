class Telefono:
    def __init__(self, siguiente=None):
        self.siguiente = siguiente

    def atender(self, atender):
        if self.siguiente is not None:
            self.siguiente.atender(atender)


class Comercial(Telefono):
    def atender(self, atender):
        if atender == "Comercial":
            print("Hola, buenas. Habla con la parte comercial, ¿en qué puedo ayudarte?")
        else:
            super().atender(atender)


class Tecnicos(Telefono):
    def atender(self, atender):
        if atender == "Tecnicos":
            print("Hola, buen día. Estás hablando con soporte técnico, ¿en qué puedo colaborarte?")
        else:
            super().atender(atender)


tecnicos_handler = Tecnicos()
comercial_handler = Comercial(tecnicos_handler)


comercial_handler.atender("Comercial")
comercial_handler.atender("Tecnicos")

