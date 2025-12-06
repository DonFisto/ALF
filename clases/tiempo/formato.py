import regex as re

from .clase import Tiempo

# Expresión regular del formato 1
_F1 = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})'
# Expresión regular del formato 2
_F2 = r'(?i)(january|february|march|april|may|june|july|august|september|october|november|december) (\d{1,2}), (\d{1,4}) (\d{1,2}):(\d{2}) (am|pm)'
# Expresión regular del formato 3
_F3 = r'(\d{2}):(\d{2}):(\d{2}) (\d{2})/(\d{2})/(\d{4})'


def _formato1(cadena: str) -> Tiempo | None:
    """
    Convierte la cadena a un Tiempo siguiendo el formato 1
    :param cadena: Cadena a convertir
    :return: `None` si la cadena no cuadra con el formato 1. Si cuadra devuelve el Tiempo correspondiente
    """
    valido = re.fullmatch(_F1, cadena)
    if not valido:
        return None
    anio = int(valido.group(1))
    mes = int(valido.group(2))
    dia = int(valido.group(3))
    hora = int(valido.group(4))
    minuto = int(valido.group(5))
    try:
        return Tiempo(dia, mes, anio, hora, minuto, 0)
    except ValueError:
        return None


def _formato2(cadena: str) -> Tiempo | None:
    """
    Convierte la cadena a un Tiempo siguiendo el formato 2
    :param cadena: Cadena a convertir
    :return: `None` si la cadena no cuadra con el formato 2. Si cuadra devuelve el Tiempo correspondiente
    """
    valido = re.fullmatch(
        _F2,
        cadena, re.IGNORECASE)
    if not valido:
        return None
    anio = int(valido.group(3))
    mes = valido.group(1).lower()
    mes = Tiempo.nombre_mes_to_numero(mes)
    dia = int(valido.group(2))
    hora = int(valido.group(4))
    if valido.group(6) == "pm" and hora != 12:
        hora += 12
    elif valido.group(6) == "am" and hora == 12:
        hora = 0
    minuto = int(valido.group(5))
    try:
        return Tiempo(dia, mes, anio, hora, minuto, 0)
    except ValueError:
        return None


def _formato3(cadena: str) -> Tiempo | None:
    """
    Convierte la cadena a un Tiempo siguiendo el formato 3
    :param cadena: Cadena a convertir
    :return: `None` si la cadena no cuadra con el formato 3. Si cuadra devuelve el Tiempo correspondiente
    """
    valido = re.fullmatch(_F3, cadena)
    if not valido:
        return None
    anio = int(valido.group(6))
    mes = int(valido.group(5))
    dia = int(valido.group(4))
    hora = int(valido.group(1))
    minuto = int(valido.group(2))
    segundos = int(valido.group(3))
    try:
        return Tiempo(dia, mes, anio, hora, minuto, segundos)
    except ValueError:
        return None


def _tiempo_por_cadena(cadena: str, formato: int) -> Tiempo | None:
    """
    Intenta obtener un tiempo a partir de una cadena en un formato determinado.
    :param cadena: Cadena de texto con el tiempo
    :param formato: Formato en el que se encuentra la cadena {1, 2, 3}. Si vale 0, buscará todos los formatos (formato automático)
    :return: Tiempo correspondiente a la cadena, o ´None´ si la cadena no cuadra con el formato dado.
    """
    if formato == 0:
        return _tiempo_por_cadena(cadena, 1) or _tiempo_por_cadena(cadena, 2) or _tiempo_por_cadena(cadena, 3)
    elif formato == 1:
        return _formato1(cadena)
    elif formato == 2:
        return _formato2(cadena)
    elif formato == 3:
        return _formato3(cadena)
    else:
        raise ValueError("El formato debe ser 1, 2, 3 o 0 (automático)")
