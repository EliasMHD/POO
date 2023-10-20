from abc import ABC, abstractmethod

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def atender(self, tipo):
        if self.puede_atender(tipo):
            self.realizar_atencion()
        elif self.next_handler:
            self.next_handler.atender(tipo)

    @abstractmethod
    def puede_atender(self, tipo):
        pass

    @abstractmethod
    def realizar_atencion(self):
        pass

class Tecnicos(Handler):
    def puede_atender(self, tipo):
        return tipo == "Tecnicos"

    def realizar_atencion(self):
        print("Hola, buen día. Estás hablando con soporte técnico, ¿en qué puedo colaborarte?")

class Comercial(Handler):
    def puede_atender(self, tipo):
        return tipo == "Comercial"

    def realizar_atencion(self):
        print("Hola, buenas. Habla con la parte comercial, ¿en qué puedo ayudarte?")

class CelularService(metaclass=SingletonMeta):
    def __init__(self):
        self.tecnicos_handler = Tecnicos()
        self.comercial_handler = Comercial(self.tecnicos_handler)

    def atender(self, tipo):
        self.comercial_handler.atender(tipo)


