import regex as re

def coordenadas_validas(coordenadas):
    return formato1_valido(coordenadas) or formato2_valido(coordenadas) or formato3_valido(coordenadas)
def coordenadas_correctas(lat, long):
    if lat < -90 or lat > 90 or long < -180 or long > 180:
        return False
    else:
        return True
def formato1_valido(coordenadas):
    valido = re.fullmatch(r'([-+]?(?:90|[0-8]\d)\.\d+)\s*,\s*([-+]?(?:90|[0-8]\d)\.\d+)', coordenadas)
    if not valido:
        return False
    latitud = float(valido.group(1))
    longitud = float(valido.group(2))
    return coordenadas_correctas(latitud, longitud)
def formato2_valido(coordenadas):
    valido = re.fullmatch(r'(\d|90|[0-8]\d)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(N|S)\s*,\s*(\d{1,2}|[1][0-7]\d|180)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(W|E)', coordenadas)
    if not valido:
        return False
    latitud = (float(valido.group(1)) + float(valido.group(2)) / 60 + float(valido.group(3)) / 3600) * (-1 if valido.group(4) == 'S' else 1)
    longitud = (float(valido.group(5)) + float(valido.group(6)) / 60 + float(valido.group(7)) / 3600) * (-1 if valido.group(8) == 'W' else 1)
    return coordenadas_correctas(latitud, longitud)
def formato3_valido(coordenadas):
    valido = re.fullmatch(r'0([0-8]\d|90)([0-5]\d)(\d?\d.\d{4})(N|S)(0\d{1,2}|1[0-7]\d|180)([0-5]\d)(\d?\d.\d{4})(W|E)', coordenadas)
    if not valido:
        return False
    latitud = (float(valido.group(1)) + float(valido.group(2)) / 60 + float(valido.group(3)) / 3600) * (-1 if valido.group(4) == 'S' else 1)
    longitud = float(valido.group(5)) + float(valido.group(6)) / 60 + float(valido.group(7)) / 3600 * (-1 if valido.group(8) == 'W' else 1)
    return coordenadas_correctas(latitud, longitud)