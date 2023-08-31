from abc import ABC, abstractmethod

class Telefono(ABC):  
    def __init__(self, siguiente=None):
        self._siguiente = siguiente

    @abstractmethod
    def atender(self, atender):
        pass


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


