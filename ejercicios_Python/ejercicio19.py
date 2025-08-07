linea1 = input("Ingrese la primera línea (elementos separados por espacios): ")
linea2 = input("Ingrese la segunda línea (elementos separados por espacios): ")

lista1 = linea1.split()
lista2 = linea2.split()


comunes = set(lista1) & set(lista2)


if comunes:
    print("\nElementos comunes encontrados:")
    for elem in comunes:
        print(f"- {elem}")
else:
    print("No hay elementos comunes.")
