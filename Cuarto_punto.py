'''
Listado de destinatarios con cantidad de mensajes recibidos

'''
def destinatarios(archivo:str):
    """Función que obtiene los destinatarios y la cantidad de mensajes recibidos por cada uno de un archivo de texto recibido como parámetro. 

    Args:
        archivo (str): Primer parámetro.
            Archivo de texto.
    """
    archivo  = archivo.lower() # Conversión todas las letras a minúsculas
    palabras = archivo.split() # Uso de la función .split() para obtener las palabras del texto separadas por espacios y saltos de línea 
    bloque = [] # Lista vacia que obtendrá bloques de texto delimitados por las palabras "received:" y "-0500" ó "(gmt)" 
    nDestinatarios = {} # Diccionario vacio que obtendrá los destinatarios y el número de mensajes recibidos por cada uno
    bandera = False # Variable bandera que permitirá el guardado de palabras en la lista bloque 
    
    for i in range(len(palabras)): # Ciclo for que cambia el valor de la variable bandera al pasar por las palabras "received:" (True) y "-0500" ó "(gmt)" (False)
        if palabras[i] == "received:":
            bandera = True
        elif palabras[i] == "-0500" or i == "(gmt)":
            bandera = False
        if bandera == True: 
            bloque.append(palabras[i])

    for i in range(len(bloque)): # Ciclo for que inicializa el número de mensajes de un destinatario del diccionario en 0 
        if bloque[i-1] == "by":
            nDestinatarios[bloque[i]] = 0
    
    for i in range(len(bloque)): # Ciclo for que obtiene los destinatarios y aumenta en uno el número de mensajes recibidos por cada uno 
        if bloque[i-1] == "by":
            nDestinatarios[bloque[i]] += 1 

    for i in range(len(nDestinatarios)): print('El destinatario "{}" recibió {} mensajes'.format(list(nDestinatarios.keys())[i],list(nDestinatarios.values())[i])) # Impresión del resultado usando el metodo .format y accediendo a las llaves del diccionario (destinatario) y a los valores del diccionario (cantidad de mensajes que recibe cada destinatario)

if __name__ == "__main__":
    with open('C:/Users/Dilan Torres Muñoz/OneDrive/Documentos/Dilan Torres/Universidad Nacional de Colombia/Ingenieria Electrica/Semestre 1/Programación de computadores/Retos/Reto 12/mbox-short.txt', 'r') as file_object: # Acceso al archivo de texto 
        leer = file_object.read()
        destinatarios(leer) # Llamada de la función destinatarios y envío del parámetro leer