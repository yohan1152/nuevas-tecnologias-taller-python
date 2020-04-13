"""
    Calcular vueltas de una llanta en 1 km. Todo se pasa a cm
"""
try:
    diametro = 50
    radio = diametro/2
    longitud = 1*(1000/1)*(100/1)
    n = 0

    n = longitud/(2*radio)

    print("\nNúmero vueltas llanta: {:,}".format(n).replace(',','.'))
except ValueError:
    print("Error.")