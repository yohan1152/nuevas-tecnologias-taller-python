"""
    1. Se requiere un algoritmo para obtener la edad promedio de un grupo de N alumnos. Si algún
    alumno tiene más de 18 años, se muestra el promedio que se lleva sin contar el alumno de 18
    años. EL usuario decide si desea cerrar el programa o vuelve a ejecutarlo.
"""
try:
    contarAlumnos = 0
    edad = 0
    sumarEdad = 0
    continuar = "si"

    while continuar == "si":
        edad = int(input("Ingrese edad del alumno:\n"))
        if edad > 18: 
            break   
        sumarEdad += edad
        contarAlumnos += 1
        continuar = input("¿Desea continuar ingresando edades de alumnos? si/no:\n").lower()

    print("\nEdad promedio: ", sumarEdad/contarAlumnos)
except ValueError:
    print("El valor ingeresado no es una edad válida.")