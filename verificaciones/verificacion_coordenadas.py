import regex as re

from clases.ubicacion import Ubicacion

def coordenadas_validas(coordenadas):
    return formato1_valido(coordenadas) or formato2_valido(coordenadas) or formato3_valido(coordenadas)
def coordenadas_correctas(lat, long):
    if lat < -90 or lat > 90 or long < -180 or long > 180:
        return False
    else:
        return True
def formato1_valido(coordenadas):
    valido = re.fullmatch(Ubicacion.F1, coordenadas)
    if not valido:
        return False
    latitud = float(valido.group(1))
    longitud = float(valido.group(2))
    return coordenadas_correctas(latitud, longitud)
def formato2_valido(coordenadas):
    valido = re.fullmatch(Ubicacion.F2, coordenadas)
    if not valido:
        return False
    latitud = (float(valido.group(1)) + float(valido.group(2)) / 60 + float(valido.group(3)) / 3600) * (-1 if valido.group(4) == 'S' else 1)
    longitud = (float(valido.group(5)) + float(valido.group(6)) / 60 + float(valido.group(7)) / 3600) * (-1 if valido.group(8) == 'W' else 1)
    return coordenadas_correctas(latitud, longitud)
def formato3_valido(coordenadas):
    valido = re.fullmatch(Ubicacion.F3, coordenadas)
    if not valido:
        return False
    latitud = (float(valido.group(1)) + float(valido.group(2)) / 60 + float(valido.group(3)) / 3600) * (-1 if valido.group(4) == 'S' else 1)
    longitud = float(valido.group(5)) + float(valido.group(6)) / 60 + float(valido.group(7)) / 3600 * (-1 if valido.group(8) == 'W' else 1)
    return coordenadas_correctas(latitud, longitud)