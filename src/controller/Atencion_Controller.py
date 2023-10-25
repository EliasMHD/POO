from service.celular_service import CelularService

celular_service = CelularService()

class AtencionController:
    @staticmethod
    def atender(tipo):
        celular_service.atender(tipo)
