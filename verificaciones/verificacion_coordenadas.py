from argparse import ArgumentError

import regex as re

from clases.ubicacion import Ubicacion


def coordenadas_validas(coordenadas) -> Ubicacion:
    """
    Determina si las coordenadas dadas son válidas.
    :param coordenadas:
    :return:
    """
    return ubicacion_por_cadena(coordenadas, 0) is not None


def ubicacion_por_cadena(coordenadas: str, formato: int) -> Ubicacion:
    """
    Obtiene la ubicación de una cadena, si está bien formateada en el formato dado.
    :param coordenadas: Cadena de texto de las coordenadas
    :param formato: Formato de la cadena (1, 2 o 3). Si es igual a cero, probará con todos los formatos (automático)
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    :raises: ArgumentError: Si el formato dado no está en {0, 1, 2, 3}
    """
    if formato == 0:
        return ubicacion_por_cadena(coordenadas, 1) or ubicacion_por_cadena(coordenadas, 2) or ubicacion_por_cadena(coordenadas, 3)
    elif formato == 1:
        return formato1(coordenadas)
    elif formato == 2:
        return formato2(coordenadas)
    elif formato == 3:
        return formato3(coordenadas)
    else:
        raise ArgumentError("El formato debe ser 1, 2, 3 o 0 (automático)")


def formato1(coordenadas: str) -> Ubicacion:
    """
    Obtiene la ubicación dadas las coordenadas en formato 1.
    :param coordenadas: Cadena de texto de las coordenadas
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    """
    valido = re.fullmatch(Ubicacion.F1, coordenadas)
    if not valido:
        return None
    latitud = float(valido.group(1))
    longitud = float(valido.group(2))
    try:
        return Ubicacion(latitud, longitud)
    except ArgumentError:
        return None


def formato2(coordenadas: str) -> Ubicacion:
    """
    Obtiene la ubicación dadas las coordenadas en formato 2.
    :param coordenadas: Cadena de texto de las coordenadas
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    """
    return formato_hex(coordenadas, Ubicacion.F2)


def formato3(coordenadas: str) -> Ubicacion:
    """
    Obtiene la ubicación dadas las coordenadas en formato 3.
    :param coordenadas: Cadena de texto de las coordenadas
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    """
    return formato_hex(coordenadas, Ubicacion.F3)


def formato_hex(coordenadas: str, expr: str) -> Ubicacion:
    """
    Obtiene la ubicación dadas las coordenadas en formatos hexadecimales. Existe para evitar duplicados de código.
    :param coordenadas: Cadena de texto de las coordenadas
    :param expr: Expresión regular a utilizar.
    :return:
    """
    valido = re.fullmatch(expr, coordenadas)
    if not valido:
        return None
    latitud = (float(valido.group(1)) + float(valido.group(2)) / 60 + float(valido.group(3)) / 3600) * (-1 if valido.group(4) == 'S' else 1)
    longitud = float(valido.group(5)) + float(valido.group(6)) / 60 + float(valido.group(7)) / 3600 * (-1 if valido.group(8) == 'W' else 1)
    try:
        return Ubicacion(latitud, longitud)
    except ArgumentError:
        return None
