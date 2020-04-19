"""
    *Reemplazar frase por el número que corresponde cada letra en el abecedario
"""
import unicodedata

def eliminar_acentos(frase):
    frase = frase.replace('ñ','#')
    res = ''.join((x for x in unicodedata.normalize('NFD',frase) if unicodedata.category(x) != 'Mn'))
    return res.replace('#','ñ')

try:
    frase = ""
    fraseNum = ""

    frase = input("Ingresar frase:\n").lower()
    frase = eliminar_acentos(frase) 

    fraseNum = frase.replace('a','1').replace('b','2').replace('c','3').replace('d','4').replace('e','5').replace('f','6').replace('g','7').replace('h','8').replace('i','9').replace('j','10').replace('k','11').replace('l','12').replace('m','13').replace('n','14').replace('ñ','15').replace('o','16').replace('p','17').replace('q','18').replace('r','19').replace('s','20').replace('t','21').replace('u','22').replace('v','23').replace('w','24').replace('x','25').replace('y','26').replace('z','27')

    print("\nFrase modificada por números:",fraseNum)
except ValueError:
    print("\nEl valor ingresado no es válido.")