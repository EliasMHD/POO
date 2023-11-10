from service.tecnico_service import Tecnicos
from service.comercial_service import Comercial

class CelularService:
    def __init__(self):
        self.tecnicos_handler = Tecnicos()
        self.comercial_handler = Comercial(self.tecnicos_handler)

    def atender(self, tipo):
        if tipo == "Tecnicos":
            self.tecnicos_handler.realizar_atencion()
        elif tipo == "Comercial":
            self.comercial_handler.atender(tipo)
        else:
            print("Tipo no válido. Intente nuevamente.")
