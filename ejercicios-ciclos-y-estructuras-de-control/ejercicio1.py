"""
    Dado un diccionario, el cual almacena las calificaciones de un
    alumno, siendo las llaves los nombres de las materia y los valores
    las calificación, mostrar en pantalla el promedio del alumno.

    Ejemplo: calificaciones = {calculo:10, dibujo:5}

    * A partir del diccionario del ejercicio anterior, mostrar en pantalla
    la materia con mejor promedio.
"""

try:
    calificaciones = {"Calculo":10, "Dibujo":5}
    promedio = 0
    mejorPromedio = 0

    promedio = (calificaciones["calculo"] + calificaciones ["dibujo"])/len(calificaciones)
    mejorPromedio = max(calificaciones, key=calificaciones.get)
    print("\nPromedio alumno: ",promedio)
    print("\nLa materia con mejor promedio es: ", mejorPromedio)

except ValueError:
    print("\nError.")