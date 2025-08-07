cumpleaneros = {}

orden_meses = [
    "Enero", "Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre",
    "Ocubre","Noviembre","Diciembre"
]

while True:
    nombre = input("Nombre (escribe (fin) para salir)")
    if nombre.lower() == "fin":
        break

    mes = input("mes de cumpleaños(eje: enero,febrero)").capitalize()
    if mes not in cumpleaneros:
        cumpleaneros[mes] = []

    cumpleaneros[mes].append(nombre)
        

print("cumpleaños por mes")
for mes in orden_meses:
    if mes in cumpleaneros:
        print(f"{mes}: {', '.join(cumpleaneros[mes])}")