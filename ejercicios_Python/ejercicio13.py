#13. Diseña un algoritmo que simule el cambio de colores de un semáforo (rojo, amarillo,
#verde).
semaforo = input("¿Desea iniciar el semáforo? (si/no): ")
if semaforo.lower() == "si":
    while True:
        print("Semáforo en Rojo.")
        input("Presione la tecla ENTER para cambiar a Amarillo.")
        print("Semáforo en Amarillo.")
        input("Presione la tecla ENTER para cambiar a Verde.")
        print("Semáforo en Verde.")
        input("Desea seguir? (si/no): ")
        if input().lower() == "no":
            print("Semáforo detenido.")
            break
else:
    print("Semáforo no iniciado. Saliendo del programa.")