from argparse import ArgumentError

from clases.entrada import Entrada
from verificaciones import verificacion_fecha as vf, verificaciones_basicas as vb, verificacion_coordenadas as vc


def data_segregation(input_text):
    lines = input_text.readlines()
    clean_lines = []
    for line in lines:
        args = line.split(";")
        tlf = args[0].strip()
        nif = args[1].strip()
        date = args[2].strip()
        coords = args[3].strip()
        desc = args[4].strip()
        price = args[5].strip()
        clean_args = [tlf, nif, date, coords, desc, price]
        clean_lines.append(clean_args)
    return clean_lines

def verificacion_datos(datos):
    datos_correctos = []
    for lista in datos:
        try:
            entrada = Entrada(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
            datos_correctos.append(entrada)
        except(ArgumentError):
            print("Formato de entrada incorrecto")



    return datos_correctos
