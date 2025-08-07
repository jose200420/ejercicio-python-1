#2. Crea un algoritmo que convierta de dólares a euros.


dolares = float(input("Ingrese la cantidad en dólares: "))
tasa_cambio = 0.86

euros = dolares * tasa_cambio
print(f"La cantidad en euros es: {euros:.2f}")
