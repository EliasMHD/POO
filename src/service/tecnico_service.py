class Tecnicos:
    def puede_atender(self, tipo):
        return tipo == "Tecnicos"

    def realizar_atencion(self):
        print("Hola, buen día. Estás hablando con soporte técnico, ¿en qué puedo colaborarte?")
