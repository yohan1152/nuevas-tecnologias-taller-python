"""
    Calcular área de triángulo
"""
try:
    base = 0
    altura = 0
    area = 0

    base = float(input("Ingresar base del triángulo:\n"))
    altura = float(input("Ingresar altura del triángulo:\n"))

    area = (base*altura)/2

    print("\nEl área del triángulo es: ",area)
except ValueError:
    print("El valor ingeresado no es válido.")