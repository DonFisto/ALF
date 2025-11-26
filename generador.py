import random
import random as rn
from math import trunc, floor

import verificaciones.verificacion_fecha as vf
def genera_tlf():
    numero = ""
    if rn.randint(0, 1):
       numero += "+" + str(rn.randint(1, 99))
    for i in range(9):
        numero += str(rn.randint(0, 9))
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
        if vf.bisiesto(int(anio)):
            dia = rn.randint(1, 29)
        else:
            dia = rn.randint(1, 28)
    hora = rn.randint(0,23)
    minuto = rn.randint(0,59)
    segundo = rn.randint(0,59)
    if formato == 1:
        anio_str = ""
        i = 10
        for j in range(4):
            anio_str = str(int((anio % i - anio % (i/10))/(i/10))) + anio_str
            i = i*10
        mes_str = str(mes)
        if mes < 10: mes_str = "0" + mes_str
        dia_str = str(dia)
        if dia < 10: dia_str = "0" + dia_str
        hora_str = str(hora)
        if hora < 10: hora_str = "0" + hora_str
        minuto_str = str(minuto)
        if minuto < 10: minuto_str = "0" + minuto_str
        
        output = output + anio_str + "-" + mes_str + "-" + dia_str + " " + hora_str + ":" + minuto_str
    elif formato == 2:
        anio_str = str(anio)

        mes_str = vf.numero_a_mes(mes)
        dia_str = str(dia)
        if hora < 12:
            hora_str = str(hora)
            ext = "AM"
        else:
            hora_str = str(hora - 12)
            ext = "PM"
        minuto_str = str(minuto)
        if minuto < 10: minuto_str = "0" + minuto_str

        output = mes_str + " " + dia_str + ", " + anio_str + " " + hora_str + ":" + minuto_str + " " + ext
    elif formato == 3:
        anio_str = ""
        i = 10
        for j in range(4):
            anio_str = str(int((anio % i - anio % (i / 10)) / (i / 10))) + anio_str
            i = i * 10
        mes_str = str(mes)
        if mes < 10: mes_str = "0" + mes_str
        dia_str = str(dia)
        if int(dia) < 10: dia_str = "0" + dia_str
        hora_str = str(hora)
        if hora < 10: hora_str = "0" + hora_str
        minuto_str = str(minuto)
        if minuto < 10: minuto_str = "0" + minuto_str
        segundo_str = str(segundo)
        if segundo < 10: segundo_str = "0" + segundo_str


        output = hora_str + ":" + minuto_str + ":" + segundo_str + " " + dia_str + "/" + mes_str + "/" + anio_str
    return output
def genera_coordenadas(formato = 1):
    output = ""
    latitud = rn.random()*180.0 - 90.0
    longitud = rn.random()*360.0 - 180.0
    if formato == 1:
        output += str (latitud) + ", " + str(longitud)
    if formato == 2:
        tmplat = abs(latitud)
        gradoslat = int(tmplat)
        tmplat -= gradoslat
        tmplat *= 100
        minutoslat = int(tmplat % 60)
        tmplat -= minutoslat
        if tmplat/60 > 1:
            gradoslat += 1
            tmplat -= 60
        tmplat *= 100
        segundoslat = round(tmplat % 60, 4)
        tmplong = abs(longitud)
        gradoslong = int(tmplong)
        tmplong -= gradoslong
        tmplong *= 100
        minutoslong = int(tmplong % 60)
        tmplong -= minutoslong
        if tmplong / 60 > 1:
            gradoslong += 1
            tmplong -= 60
        tmplong *= 100
        segundoslong = round(tmplong % 60, 4)
        output += str(gradoslat) + chr(176) + genera_espacios(10) + str(minutoslat) + "\'" + genera_espacios(10) + f'{segundoslat:02.04f}' + "\" "
        if latitud > 0: output += "N,"
        else: output += "S,"
        output += genera_espacios(10) + str(gradoslong) + chr(176) + genera_espacios(10) + str(minutoslong) + "\'" + genera_espacios(10) + f'{segundoslong:02.04f}' + "\" "
        if longitud > 0: output += "E"
        else: output += "W"
    if formato == 3:
        tmplat = abs(latitud)
        gradoslat = int(tmplat)
        tmplat -= gradoslat
        tmplat *= 100
        minutoslat = int(tmplat % 60)
        tmplat -= minutoslat
        if tmplat / 60 > 1:
            gradoslat += 1
            tmplat -= 60
        tmplat *= 100
        segundoslat = round(tmplat % 60, 4)
        tmplong = abs(longitud)
        gradoslong = int(tmplong)
        tmplong -= gradoslong
        tmplong *= 100
        minutoslong = int(tmplong % 60)
        tmplong -= minutoslong
        if tmplong / 60 > 1:
            gradoslong += 1
            tmplong -= 60
        tmplong *= 100
        segundoslong = round(tmplong % 60, 4)
        output += f"{gradoslat:03d}{minutoslat:02d}{segundoslat:02.04f}"
        if latitud > 0: output += "N"
        else: output += "S"
        output += f"{gradoslong:03d}{minutoslong:02d}{segundoslong:02.04f}"
        if longitud > 0: output += "E"
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

#genera_entrada("prueba1", 100)