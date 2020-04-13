"""
    Promedio Notas estudiante
"""
import math
 
try:
    materias = 5
    notas = 0

    for i in range (materias):
        notas += float(input("Ingresar nota # %s: \n" %(i+1)))

    print("\nEl promedio de notas del alumno es: ", notas/materias)
except ValueError:
    print("\nValores ingresados no válidos.")
    print("\nEl promedio de notas del alumno es: ", notas/materias)