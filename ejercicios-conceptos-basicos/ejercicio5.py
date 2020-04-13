"""
    Calcular segundo que le toma viajar a luz del sol a Marte. 
    Distancia 227.940.000 millones de Kms
    Velocidad luz = 299.792 km/s
"""
try:
    distanciaSolMarte = 227940000
    velLuz = 299792

    print("\nSegundos en llegar la luz a Marte: {:,}".format((distanciaSolMarte/velLuz)).replace(',','.'),"Seg")
except ValueError:
    print("Error.")