"""
    Calcular dólares a pesos colombianos. Valor del dólar hoy 12-04-2020 = 3.827
"""
try:
    valPeso = 3827
    dolares = 0

    dolares = float(input("Ingresar cantidad de dólares:\n"))

    print("\nEl valor total en pesos colombianos es: ${:,}".format((dolares*valPeso)).replace(',','.'))
except ValueError:
    print("El valor ingeresado no es válido.")