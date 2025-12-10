import regex as re

from .clase import Ubicacion

_F1 = re.compile(r'([-+]?(?:90|[0-8]\d|\d)\.\d+)\s*,\s*([-+]?(?:180|1[0-7]\d|\d{1,2})\.\d+)')
_F2 = re.compile(r'(\d|90|[0-8]\d)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(N|S)\s*,\s*(\d{1,2}|[1][0-7]\d|180)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(W|E)')
_F3 = re.compile(r'0([0-8]\d|90)([0-5]\d)(\d?\d.\d{4})(N|S)(0\d{1,2}|1[0-7]\d|180)([0-5]\d)(\d?\d.\d{4})(W|E)')


def _ubicacion_por_cadena(coordenadas: str, formato: int) -> Ubicacion:
    """
    Obtiene la ubicación de una cadena, si está bien formateada en el formato dado.
    :param coordenadas: Cadena de texto de las coordenadas
    :param formato: Formato de la cadena (1, 2 o 3). Si es igual a cero, probará con todos los formatos (automático)
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    :raises: ValueError: Si el formato dado no está en {0, 1, 2, 3}
    """
    output = None
    if formato == 1 or formato == 0:
        output = _formato1(coordenadas)
    if formato == 2 or (formato == 0 and output is None):
        output = _formato2(coordenadas)
    if formato == 3 or (formato == 0 and output is None):
        output = _formato3(coordenadas)
    elif 0 > formato or formato > 3:
        raise ValueError("El formato debe ser 1, 2, 3 o 0 (automático)")
    return output


def _formato1(coordenadas: str) -> Ubicacion | None:
    """
    Obtiene la ubicación dadas las coordenadas en formato 1.
    :param coordenadas: Cadena de texto de las coordenadas
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    """
    valido = _F1.fullmatch(coordenadas)
    if not valido:
        output = None
    else:
        latitud = float(valido.group(1))
        longitud = float(valido.group(2))
        try:
            output = Ubicacion(latitud, longitud)
        except ValueError:
            output = None
    return output


def _formato2(coordenadas: str) -> Ubicacion | None:
    """
    Obtiene la ubicación dadas las coordenadas en formato 2.
    :param coordenadas: Cadena de texto de las coordenadas
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    """
    return _formato_hex(coordenadas, _F2)


def _formato3(coordenadas: str) -> Ubicacion | None:
    """
    Obtiene la ubicación dadas las coordenadas en formato 3.
    :param coordenadas: Cadena de texto de las coordenadas
    :return: La ubicación correspondiente, o `None` si la cadena no cuadra con dicho formato.
    """
    return _formato_hex(coordenadas, _F3)


def _formato_hex(coordenadas: str, expr: re.Pattern) -> Ubicacion | None:
    """
    Obtiene la ubicación dadas las coordenadas en formatos hexadecimales. Existe para evitar duplicados de código.
    :param coordenadas: Cadena de texto de las coordenadas
    :param expr: Expresión regular a utilizar.
    :return:
    """
    valido = expr.fullmatch(coordenadas)
    if not valido:
        output = None
    else:
        latitud = (float(valido.group(1)) + float(valido.group(2)) / 60 + float(valido.group(3)) / 3600) * (
            -1 if valido.group(4) == 'S' else 1)
        longitud = (float(valido.group(5)) + float(valido.group(6)) / 60 + float(valido.group(7)) / 3600) * (
            -1 if valido.group(8) == 'W' else 1)
        try:
            output = Ubicacion(latitud, longitud)
        except ValueError:
            output = None
    return output
