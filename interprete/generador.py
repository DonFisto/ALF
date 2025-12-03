import random as rn
from random import randint

from clases.tiempo import Tiempo


def genera_tlf():
    numero = ""
    if rn.randint(0, 1):
        #formato internacional
       numero += "+" + str(rn.randint(1, 999999999999))
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
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    nif = ""
    for i in range(8):
        nif += str(rn.randint(0, 9))
    idx = int(nif) % 23
    nif += letras_dni[idx]
    return nif

def genera_fecha(formato = 1):
    output = " "
    anio = rn.randint(1,9999)
    mes = rn.randint(1,12)
    if mes in {1,3,5,7,8,10,12}:
        dia = rn.randint(1,31)
    elif not mes == 2:
        dia = rn.randint(1, 30)
    else:
        if Tiempo.bisiesto(int(anio)):
            dia = rn.randint(1, 29)
        else:
            dia = rn.randint(1, 28)
    hora = rn.randint(0,23)
    minuto = rn.randint(0,59)
    segundo = rn.randint(0,59)
    if formato == 1:
        output += f"{anio:04d}-{mes:02d}-{dia:02d} {hora:02d}:{minuto:02d}"
    elif formato == 2:
        output += f"{Tiempo.numero_mes_to_nombre(mes)} {dia}, {anio} {hora:02d}:{minuto:02d}"
    elif formato == 3:
        output += f"{hora:02d}:{minuto:02d}:{segundo:02d} {dia:02d}/{mes:02d}/{anio:04d}"
    return output
def genera_coordenadas(formato = 1):
    output = ""

    if formato == 1:
        latitud = rn.random() * 180.0 - 90.0
        longitud = rn.random() * 360.0 - 180.0
        output += f"{str(latitud)}, {str(longitud)}"
    if formato == 2 or formato == 3:
        gradoslat = rn.randint(-90,90)
        if abs(gradoslat) == 90:
            minutoslat = 0
            segundoslat = 0
        else:
            minutoslat = rn.randint(0,59)
            segundoslat = rn.randint(0,590000)/10000.0

        gradoslong = rn.randint(-180, 180)
        if abs(gradoslong) == 180:
            minutoslong = 0
            segundoslong = 0
        else:
            minutoslong = rn.randint(0, 59)
            segundoslong = rn.randint(0,590000)/10000.0
        if formato == 2:
            output += f"{str(abs(gradoslat))}{chr(176)}{genera_espacios(10)}{str(minutoslat)}\'{genera_espacios(10)}{segundoslat:02.04f}\" "
            if gradoslat > 0: output += "N,"
            else: output += "S,"
            output += f"{str(abs(gradoslong))}{chr(176)}{genera_espacios(10)}{str(minutoslong)}\'{genera_espacios(10)}{segundoslong:02.04f}\" "
            if gradoslong > 0: output += "E"
            else: output += "W"
        else:
            output += f"{abs(gradoslat):03d}{minutoslat:02d}{segundoslat:02.04f}"
            if gradoslat > 0: output += "N"
            else: output += "S"
            output += f"{abs(gradoslong):03d}{minutoslong:02d}{segundoslong:02.04f}"
            if gradoslong > 0: output += "E"
            else: output += "W"

    return output

def genera_descripcion(longitud = 100):
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz "
    output = ""
    for i in range(longitud):
        idx = rn.randint(0,53)
        output += caracteres[idx]
    return output

def genera_precio(max, maxdecimales):
    parte_entera = rn.randint(0, max)
    ndecimales = rn.randint(0, maxdecimales)
    parte_decimal = rn.randint(0,10**ndecimales)
    euro_dolar = rn.randint(0, 1)
    output = str(parte_entera)
    if ndecimales > 0:
        output += f".{parte_decimal:0{ndecimales}d}"
    if euro_dolar == 0: output += "€"
    else: output += "$"
    return output

def genera_espacios(max):
    output = ""
    for i in range(rn.randint(1,max)):
        output += " "
    return output

def genera_linea():
    ffecha = rn.randint(1,3)
    fcoord = rn.randint(1, 3)
    output = genera_tlf() + ";" + genera_nif() + ";" + genera_fecha(ffecha) + ";" + genera_coordenadas(fcoord) + ";" + genera_descripcion() + ";" + genera_precio(4000, 6)
    return output


def genera_entrada(nombre_fichero, num_entradas):
    file = open(nombre_fichero, "w", encoding='utf-8')
    for i in range(num_entradas):
        file.write(genera_linea() + "\n")

#genera_entrada("prueba1", 1000)