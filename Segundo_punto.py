'''
Cantidad de consonantes
'''
def cantidadDeConsonantes(archivo:str):
    """Función que obtiene la cantidad de consonantes que hay en un archivo de texto recibido como parámetro. 

    Args:
        archivo (str): Primer parámetro.
            Archivo de texto.
    """
    archivo = archivo.lower() # Conversión todas las letras a minúsculas
    vocales = ["a","e","i","o","u"] # Lista con las vocales
    cantConsonantes = {} # Diccionario vacio que obtendrá la cantidad de consontantes del texto

    for i in archivo: # Ciclo for que inicializa la cantidad de consonantes del texto en el diccionario como 0 
        if i.isalpha() and i not in vocales:
            cantConsonantes[i] = 0

    for i in archivo: # Ciclo for que obtiene las consonantes del texto y aumenta en uno el valor de apariciones de las mismas 
        if i.isalpha() and i not in vocales:
            cantConsonantes[i] += 1

    cantConsonantes = dict(sorted(cantConsonantes.items())) # Ordenamiento de las llaves diccionario por orden alfabético 

    for i in range(len(cantConsonantes)): print("La consonante {} esta {} veces en el texto".format(list(cantConsonantes.keys())[i],list(cantConsonantes.values())[i])) # Impresión del resultado usando el metodo .format y accediendo a las llaves del diccionario (consonante) y a los valores del diccionario (cantidad de apariciones de la consonante)

if __name__ == "__main__":
    with open('C:/Users/Dilan Torres Muñoz/OneDrive/Documentos/Dilan Torres/Universidad Nacional de Colombia/Ingenieria Electrica/Semestre 1/Programación de computadores/Retos/Reto 12/mbox-short.txt', 'r') as file_object: # Acceso al archivo de texto 
        leer = file_object.read()
        cantidadDeConsonantes(leer) # Llamada de la función cantidadDeConsonantes y envío del parámetro leer