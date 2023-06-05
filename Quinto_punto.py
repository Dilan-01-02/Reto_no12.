'''
Cantidad de mensajes enviados por cada día

'''
def mensajesPorDia(archivo:str):
    """Función que obtiene la cantidad de mensajes recibidos por día de un archivo de texto recibido como parámetro.  

    Args:
        archivo (str): Primer parámetro.
            Archivo de texto.
    """
    archivo  = archivo.lower() # Conversión todas las letras a minúsculas
    palabras = archivo.split() # Uso de la función .split() para obtener las palabras del texto separadas por espacios y saltos de línea 
    bloque = [] # Lista vacia que obtendrá bloques de texto delimitados por las palabras "received:" y "-0500" ó "(gmt)" 
    nMensajes = {} # Diccionario vacio que obtendrá el número de mensajes recibidos por día 
    bandera = False # Variable bandera que permitirá el guardado de palabras en la lista bloque 

    for i in range(len(palabras)): # Ciclo for que cambia el valor de la variable bandera al pasar por las palabras "received:" (True) y "-0500" ó "(gmt)" (False)
        if palabras[i] == "received:":
            bandera = True
        elif palabras[i] == "-0500" or i == "(gmt)":
            bandera = False
        if bandera == True:
            bloque.append(palabras[i])

    for i in range(len(bloque)): # Ciclo for que inicializa la cantidad de mensajes recibidos por día del diccinario en 0
        if bloque[i] == "jan":
            nMensajes[int(bloque[i-1])] = 0
    
    for i in range(len(bloque)): # Ciclo for que obtiene los días que se recibieron mensajes y aumenta en uno la cantidad de mensajes recibidos cada día
        if bloque[i] == "jan":
            nMensajes[int(bloque[i-1])] += 1 

    for i in range(len(nMensajes)): print("El día {} de enero del 2008 se recibieron {} mensajes".format(list(nMensajes.keys())[i],list(nMensajes.values())[i])) # Impresión del resultado usando el metodo .format y accediendo a las llaves del diccionario (día en el que se recibieron mensajes) y a los valores del diccionario (cantidad de mensajes recibidos cada día)

if __name__ == "__main__":
    with open('C:/Users/Dilan Torres Muñoz/OneDrive/Documentos/Dilan Torres/Universidad Nacional de Colombia/Ingenieria Electrica/Semestre 1/Programación de computadores/Retos/Reto 12/mbox-short.txt', 'r') as file_object: # Acceso al archivo de texto 
        leer = file_object.read()
        mensajesPorDia(leer) # Llamada de la función mensajesPorDia y envío del parámetro leer