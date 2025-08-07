#8. Crea un algoritmo que calcule el pago mensual de un préstamo, dado el monto, la tasa de interés anual y el número de meses.


monto = float(input("Monto del préstamo: "))
tasa_anual = float(input("Tasa de interés anual (%): "))
meses = int(input("Número de meses: "))


tasa_mensual = tasa_anual / 12 / 100


if tasa_mensual == 0:
    pago_mensual = monto / meses
else:
    pago_mensual = (monto * tasa_mensual) / (1 - (1 + tasa_mensual) ** -meses)

print(f"El pago mensual es: {pago_mensual:.2f}")