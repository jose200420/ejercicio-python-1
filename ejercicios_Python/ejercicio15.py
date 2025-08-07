#15. Desarrolla un algoritmo que reste los gastos de un presupuesto mensual y muestre el saldo restante.

def calcular_saldo_restante(presupuesto_inicial, gastos):
    saldo = presupuesto_inicial - sum(gastos)
    return saldo

# Interacción con el usuario
presupuesto = float(input("Introduce el presupuesto mensual: "))
gastos = []

print("Introduce los gastos (escribe 'fin' para terminar):")
while True:
    gasto = input("Gasto: ")
    if gasto.lower() == 'fin':
        break
    gastos.append(float(gasto))

saldo_restante = calcular_saldo_restante(presupuesto, gastos)
print(f"\nSaldo restante: {saldo_restante}")