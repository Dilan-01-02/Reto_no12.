'''
Listado de las 50 palabras que más se repiten

'''
def palabrasRepetidas(archivo:str):
    """Función que obtiene las 50 palabras mas repetidas de un archivo de texto recibido como parámetro. 

    Args:
        archivo (str): Primer parámetro.
            Archivo de texto.
    """
    archivo = archivo.lower() # Conversión todas las letras a minúsculas
    nPalabras = {} # Diccionario vacio que obtendrá las palabras repetidas y la cantidad de apariciones de esta en el texto

    for i in archivo: # Ciclo for que convierte todos los simbolos que no hacen parte del alfabeto en espacios
        if not i.isalpha() and i != " ":
            archivo =  archivo.replace(i, " ")

    narchivo = archivo.split() # Uso de la función .split() para obtener las palabras del texto separadas por espacios y saltos de línea 

    for i in narchivo: nPalabras[i] = 0 # Ciclo for que inicializa las palabras repetidas del texto en el diccionario en 0
    for i in narchivo: nPalabras[i] += 1 # Ciclo for que obtiene las palabras repetidas y aumenta en uno la cantidad de apariciones de la misma en el texto

    for i in sorted(nPalabras, reverse=True, key= lambda i: nPalabras[i])[:51]: # Ciclo for que ordena los valores del diccionario (cantidad de apariciones de una palabra) de forma descendente, y obitien las 50 palabras mas repetidas
        print("La palabra {} se repite {} veces en el texto".format(i, nPalabras[i]))  # Impresión del resultado usando el metodo .format y accediendo a las llaves del diccionario (palabra repetida) y a los valores del diccionario (cantidad de apariciones de la palabra)
 
if __name__ == "__main__":
    with open('C:/Users/Dilan Torres Muñoz/OneDrive/Documentos/Dilan Torres/Universidad Nacional de Colombia/Ingenieria Electrica/Semestre 1/Programación de computadores/Retos/Reto 12/mbox-short.txt', 'r') as file_object: # Acceso al archivo de texto 
        leer = file_object.read()
        palabrasRepetidas(leer) # Llamada de la función palabrasRepetidas y envío del parámetro leer