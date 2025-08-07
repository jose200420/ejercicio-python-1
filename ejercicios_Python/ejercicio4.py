#4. Escribe un algoritmo que calcule el IMC de una persona a partir de su peso (kg) y altura (metros).
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / altura**2
print(f"Su IMC es: {imc:.2f}")