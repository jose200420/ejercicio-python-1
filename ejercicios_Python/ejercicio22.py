numeros = []

for i in range (3):
    num = float(input("ingrese un numero {i+1}: "))
    numeros.append(num)

suma = sum(numeros)
promedio = suma / len(numeros)

print(f"el promedio de los 3 numeros es: {promedio}")
