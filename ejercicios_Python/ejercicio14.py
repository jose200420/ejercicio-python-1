#14. Escribe un algoritmo que tome una lista de canciones y devuelva una lista de reproducción en orden aleatorio.

import random

def crear_lista_reproduccion(canciones):
    canciones_aleatorias = canciones[:]  # Copia para no modificar la original
    random.shuffle(canciones_aleatorias)
    return canciones_aleatorias

# Interacción con el usuario
canciones = []
print("Introduce los nombres de las canciones (escribe 'fin' para terminar):")
while True:
    cancion = input("Canción: ")
    if cancion.lower() == 'fin':
        break
    canciones.append(cancion)

lista_aleatoria = crear_lista_reproduccion(canciones)
print("\nLista de reproducción en orden aleatorio:")
for idx, cancion in enumerate(lista_aleatoria, 1):
    print(f"{idx}. {cancion}")