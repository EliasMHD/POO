from domain.celular_builder import celular_service

while True:
    seccion = input("¿Qué sección prefieres, 'Tecnica' o 'Comercial'? (Escribe 'salir' para terminar): ").strip()

    if seccion.lower() == 'salir':
        break

    if seccion.lower() == 'tecnica':
        celular_service.atender("Tecnicos")
    elif seccion.lower() == 'comercial':
        celular_service.atender("Comercial")
    else:
        print("Selección no válida. Por favor, elige 'Tecnicos' o 'Comercial'.")




