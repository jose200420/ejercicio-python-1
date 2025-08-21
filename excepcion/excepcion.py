#ZeroDivisionError
try:
    resultado = 100/0
except ZeroDivisionError:
    print("Error: No se pede dividir por cero")

#IndexError
try:
    lista = [1,2,4,6,8,10] 
    print(lista[5])
except IndexError:
    print("Error: Numero no esta en la lista")

try:
    print(c)
except NameError:
    print("Error: La variable c, no esta definida")

#TypeError
try:
    multiplicar = 10 + "Manuel"
except TypeError:
    print("Error: No soporta tipo con candena de texto")

#ModuleNotFoundError
try:
    import mathe
except ModuleNotFoundError:
    print("Error: El modulo no se llama mathe")

#OverFlowError
try:
    resultado = 6.999 ** 99999
except OverflowError:
    print("Error: el resultado es demasiado grande")

# KeyError
try:
    producto ={"Papa": 12, "Sandia": 45}
    print(producto["Pera"])
except KeyError:
    print("Error: llave erronea, Pera no existe")


#Excepcionesmultiples
try:
    numero_str = 'no es un numero'
    numero = int(numero_str)  # Esto causará un ValueError
    
    divisor = 0
    resultado = 10 / divisor # Esto causaría un ZeroDivisionError si lo de arriba no falla
    
except ValueError:
    print('Error: no se puede convertir el texto a un numero')
except ZeroDivisionError:
    print('Error: no se puede dividir por cero')
finally:
    print('El bloque finally se ejecuta al final, sin importar si hubo un error o no.')


#ExcepcionPersonalizada
class ErrorDeValidacion(Exception):
    def __init__(self, mensaje, campo_invalido):
        super().__init__(mensaje)
        self.campo_invalido = campo_invalido

def validar_edad(edad):
    if not isinstance(edad, (int, float)):
        raise TypeError("La edad debe ser un numero")
    if edad < 0:
        raise ErrorDeValidacion("La edad no puede ser negativa", "edad")
    return edad

try:
    mi_edad = -5
    validar_edad(mi_edad)
except ErrorDeValidacion as e:
    print(f"Error en el campo '{e.campo_invalido}': {e}")
except TypeError as e:
    print(f"Error de tipo: {e}")