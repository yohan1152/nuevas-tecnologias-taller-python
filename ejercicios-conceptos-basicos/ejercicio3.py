"""
    Convertir grados centígrados a fahrenheit
"""
try:
    gradosCentigrados = 0
    gradosFahrenheit = 0

    gradosCentigrados = float(input("Ingresar Grados Centígrados:\n"))
    gradosFahrenheit = gradosCentigrados*(9/5) + 32

    print("\nGrados Fahrenheit: ", gradosFahrenheit)
except ValueError:
    print("El valor ingeresado no es válido.")