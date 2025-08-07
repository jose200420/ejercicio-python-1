#7. Escribe un algoritmo que verifique si hay asientos disponibles en un evento y reserve uno.
asientos_disponibles = int(input("Ingrese el número de asientos disponibles: "))
if asientos_disponibles > 0:
    asientos_disponibles -= 1
    print("Asiento reservado con éxito.")
    print(f"Asientos restantes: {asientos_disponibles}")
else:
    print("No hay asientos disponibles.")
