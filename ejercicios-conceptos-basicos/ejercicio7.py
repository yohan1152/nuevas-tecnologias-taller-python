"""
    Longitud de la sombra de un edificio
"""
import math
 
try:
    altura = 20
    angulo = math.radians(22)
    longSombra = 0

    longSombra = altura/math.tan(angulo)
    
    print("\nLa longitud de la sombra que proyecta el edificio es: {:,}".format(longSombra).replace(',','.'),"m")
except ValueError:
    print("\nError.")