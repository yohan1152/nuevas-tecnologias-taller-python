"""
    Convertir Años a segundos
"""
try:
    lustro = 5
    anosSegundos = 60*60*24*365

    print("\nSegundos del lustro: {:,}".format((lustro*anosSegundos)).replace(',','.'),"Seg")
except ValueError:
    print("Error.")