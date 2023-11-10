class Comercial:
    def __init__(self, tecnicos_handler):
        self.tecnicos_handler = tecnicos_handler

    def atender(self, tipo):
        if self.tecnicos_handler.puede_atender(tipo):
            self.tecnicos_handler.realizar_atencion()
        else:
            print("No puedo atender este tipo de solicitud.")

