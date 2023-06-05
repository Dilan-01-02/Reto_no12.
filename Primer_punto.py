'''
Cantidad de vocales
'''
def cantidadDeVocales(archivo:str):
    """Función que obtiene la cantidad de vocales que hay en un archivo de texto recibido como parámetro. 

    Args:
        archivo (str): Primer parámetro.
            Archivo de texto.
    """
    archivo = archivo.lower() # Conversión todas las letras a minúsculas 
    vocales = ["a","e","i","o","u"] # Lista con las vocales
    cantVocales = {} # Diccionario vacio que obtendrá la cantidad de vocales del texto

    for i in vocales: cantVocales[i] = 0 # Ciclo for que inicializa la cantidad de vocales del texto en el diccionario como 0 

    for i in archivo: # Ciclo for que obtiene las vocales del texto y aumenta en uno el valor de apariciones de las mismas 
        if i in vocales:
            cantVocales[i] += 1
    
    for i in range(len(cantVocales)): print("La vocal {} esta {} veces en el texto".format(list(cantVocales.keys())[i],list(cantVocales.values())[i])) # Impresión del resultado usando el metodo .format y accediendo a las llaves del diccionario (vocales) y a los valores del diccionario (cantidad de apariciones de la vocal)

if __name__ == "__main__":
    with open('C:/Users/Dilan Torres Muñoz/OneDrive/Documentos/Dilan Torres/Universidad Nacional de Colombia/Ingenieria Electrica/Semestre 1/Programación de computadores/Retos/Reto 12/mbox-short.txt', 'r') as file_object: # Acceso al archivo de texto 
        leer = file_object.read()
        cantidadDeVocales(leer) # Llamada de la función cantidadDeVocales y envío del parámetro leer