"""
    Edad ingresada por usuarios es la misma True o False
"""
try:
    edad1 = 0
    edad2 = 0

    edad1 = int(input("Ingresar edad del primer usuario: \n"))
    edad2 = int(input("Ingresar edad del segundo usuario: \n"))

    if edad1 == edad2:
        print("\nLas edades son las mismas: ", True)
    else:
        print("\nLas edades no son las mismas: ", False)
except ValueError:
    print("\nValores ingresados no válidos.")