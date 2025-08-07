precio = float(input("ingrese el precio del producto: "))
des = float(input("ingrese el descuento del producto: "))

descuento = precio * (des / 100) 
preciof = precio - descuento

print(f"el precio final del producto es de: {preciof}")