#6. Diseña un algoritmo que calcule el costo total de un viaje, sumando el costo del combustible, el peaje y el alojamiento.
costo_combustible = float(input("Ingrese el costo del combustible: "))
costo_peaje = float(input("Ingrese el costo del peaje: "))
costo_alojamiento = float(input("Ingrese el costo del alojamiento: "))
costo_total = costo_combustible + costo_peaje + costo_alojamiento
print(f"El costo total del viaje es: {costo_total:.2f}")
print(f"Desglose de costos:")
print(f"- Combustible: {costo_combustible:.2f}")
print(f"- Peaje: {costo_peaje:.2f}")
print(f"- Alojamiento: {costo_alojamiento:.2f}")