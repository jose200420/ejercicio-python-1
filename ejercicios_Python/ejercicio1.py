#""" Desarrolla un algoritmo que calcule la propina y el total a pagar en un restaurante, dado el monto de la cuenta y el porcentaje de propina.

pago = float(input("Ingrese el monto de la cuenta: "))
porcentaje_propina = float(input("Ingrese el porcentaje de propina (ejemplo: 15 para 15%): "))
propina = pago * (porcentaje_propina / 100)
total = pago + propina
print(f"La propina es: {propina:.2f}")
print(f"El total a pagar es: {total:.2f}")


