import random as rn
from random import randint

from clases.tiempo import Tiempo
from clases.ubicacion import Ubicacion


def genera_tlf():
    """
    Genera un número de teléfono aleatorio sea en formato español o internacional y lo devuelve como cadena de texto.
    :return: Número de telefono generado.
    """
    numero = ""
    if rn.randint(0, 1):
        #formato internacional
        numero = "+"
        for i in range(randint(10, 15)):
            numero += str(rn.randint(0, 9))
    else:
        #formato español
        for i in range(3):
            for _ in range(3):
                # Añadir tres números
                numero += str(rn.randint(0, 9))
            #Añadir espacio de separación, salvo si es el último.
            if i != 2:
                numero += " "
    return numero

def genera_nif():
    """
    Genera un nif/nie válido y lo devuelve como cadena de texto.
    :return: nif/nie generado.
    """
    #listas de letras validas para nie/dni
    letras_nie = "XYZ"
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    nif = ""
    #generación de 8 dígitos aleatorios
    for i in range(8):
        nif += str(rn.randint(0, 9))
    #asignación de la letra correcta
    idx = int(nif) % 23
    nif += letras_dni[idx]
    #si empieza por 0, 1 o 2 se determina de forma aleatoria si se convierte en nie
    if nif[0] in "012":
        extranjero_rnd = rn.randint(0,1)
        #en caso de ser nie, se cambia el primer dígito (0, 1, 2) por X, Y, Z respectivamente
        if extranjero_rnd:
            nif = letras_nie[int(nif[0])] + nif[1:]
    return nif

def genera_fecha(formato = 1):
    """
    Genera una fecha válida y la devuelve como cadena de texto con el formato indicado.
    :param formato: valor entero entre 1 y 3 que toma por defecto el valor 1 e indica el formato con el que se devuelve la fecha generada
    :return: fecha generada expresada en el formato indicado.
    """
    anio = rn.randint(1,9999)
    mes = rn.randint(1,12)
    if mes in {1,3,5,7,8,10,12}:
        dia = rn.randint(1,31)
    elif mes != 2:
        dia = rn.randint(1, 30)
    else:
        if Tiempo.bisiesto(int(anio)):
            dia = rn.randint(1, 29)
        else:
            dia = rn.randint(1, 28)
    hora = rn.randint(0,23)
    minuto = rn.randint(0,59)
    segundo = rn.randint(0,59)
    tiempo = Tiempo(dia, mes, anio, hora, minuto, segundo)
    return tiempo.formatear(formato)

def genera_coordenadas(formato = 1):
    """
    Genera una ubicación válida y la devuelve como cadena de texto con el formato indicado.
    :param formato: valor entero entre 1 y 3 que toma por defecto el valor 1 e indica el formato con el que se devuelve la ubicación generada
    :return: ubicación generada en el formato indicado.
    """
    latitud = rn.random() * 180.0 - 90.0
    longitud = rn.random() * 360.0 - 180.0
    coordenadas = Ubicacion(latitud, longitud)
    return coordenadas.formatear(formato)

def genera_descripcion(longitud = 100):
    """
    Genera una descripción de la longitud indicada formada por caracteres aleatorios y la devuelve como cadena de texto.
    :param longitud: valor entero que indica longitud de la descripcion generada. Toma por defecto el valor 100
    :return: descripción generada.
    """
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz "
    output = ""
    for i in range(longitud):
        idx = rn.randint(0,53)
        output += caracteres[idx]
    return output

def genera_precio():
    """
    Genera un precio aleatorio para un item en euros o en dolares y lo devuelve como cadena de texto.
    :return: precio generado.
    """
    precio = rn.random() * (10 ** (randint(0, 6))) # Número aleatorio en [0, 1), y corremos la coma un número aleatorio de posiciones
    euro_dolar = rn.randint(0, 1)
    min_decimales = rn.randint(1, 10)
    output = f"{precio:.{min_decimales}f}"
    if euro_dolar == 0:
        output += "€"
    else:
        output += "$"
    return output

def genera_espacios(max_espacios):
    """
    Genera un número aleatorio de espacios entre 1 y el máximo indicado y lo devuelve como cadena de texto.
    :param max_espacios: valor entero que indica el número máximo de espacios que se pueden generar
    :return: cadena de texto con tantos espacios en blanco como se hayan generado de forma aleatoria.
    """
    output = ""
    for i in range(rn.randint(1, max_espacios)):
        output += " "
    return output

def genera_linea():
    """
    Genera una linea aleatoria que consta de un número de telefono, un nif/nie, una fecha, una ubicación, una descripción y un precio y la devuelve como cadena de texto con los valores separados por ;
    :return: linea generada.
    """
    ffecha = rn.randint(1,3)
    fcoord = rn.randint(1, 3)
    output = genera_tlf() + ";" + genera_nif() + ";" + genera_fecha(ffecha) + ";" + genera_coordenadas(fcoord) + ";" + genera_descripcion() + ";" + genera_precio()
    return output


def genera_entrada(nombre_fichero, num_entradas):
    """
    Genera tantas lineas aleatorias como se indique y las almacena el archivo indicado.
    :param nombre_fichero: fichero en el que se almacena la entrada generada
    :param num_entradas: número de lineas en la entrada
    :return: no se devuelve ningún valor.
    """
    file = open(nombre_fichero, "w", encoding='utf-8')
    for i in range(num_entradas):
        file.write(genera_linea() + "\n")
    return

genera_entrada("prueba1", 1000)