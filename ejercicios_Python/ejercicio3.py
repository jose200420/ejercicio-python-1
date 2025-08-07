#3. Implementa un algoritmo que clasifique a una persona en "Niño"(13),
#"Adolescente"(18), "Adulto" (+18) o "Adulto mayor" (65) según su edad.

edad = int(input("Ingrese su edad: "))
if edad <= 13:
    print("Niño")
elif edad <= 18:
    print("Adolescente")
elif edad < 65:
    print("Adulto")
else:
    print("Adulto mayor")
    