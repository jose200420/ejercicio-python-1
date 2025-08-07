#5. Desarrolla un algoritmo que permita agregar, eliminar y mostrar una lista de compras.  
lista_compras = []
while True:
    print("\nOpciones:")
    print("1. Agregar artículo")
    print("2. Eliminar articulo")
    print("3. Mostrar lista de compras")
    print("4. Salir")
    opcion = input("Seleccione una opción (1-4): ")
    if opcion == '1':
        articulo = input("Ingrese el artículo a agregar: ")
        lista_compras.append(articulo)
        print(f"{articulo} ha sido agregado a la lista.")
    elif opcion == '2':
        articulo = input("Ingrese el artículo a eliminar: ")
        if articulo in lista_compras:
            lista_compras.remove(articulo)
            print(f"{articulo} ha sido eliminado de la lista.")
        else:
            print(f"{articulo} no se encuentra en la lista.")
    elif opcion == '3':
        print("Lista de compras:")
        for item in lista_compras:
            print(f"- {item}")
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
        