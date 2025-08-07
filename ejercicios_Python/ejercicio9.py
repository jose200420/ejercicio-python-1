import random

while True:
    opcion = int(input("quieres lanzar el dado (1=SI  2=(NO)): "))
    if opcion == 1:
        dado = random.randint(1, 6)
        print(f"el dado cayó en: {dado}")
        
    else:
        print("lanzá el gran hijueputa dado")
        


