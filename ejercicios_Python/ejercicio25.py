
entrada = input("Ingresa una lista de números separados por coma: ")


numeros = [int(x) for x in entrada.split(",")]


numeros.sort()

print("Lista ordenada de menor a mayor:", numeros)
