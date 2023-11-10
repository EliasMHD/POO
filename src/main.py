from service.celular_service import CelularService



def main():
    service = CelularService()

    while True:
        tipo = input("Elija el tipo de atención (Tecnicos/Comercial): ")
        service.atender(tipo)
        break

if __name__ == "__main__":
    main()





