from .formato import _ubicacion_por_cadena


def coordenadas_validas(coordenadas: str) -> bool:
    """
    Determina si las coordenadas dadas son válidas.
    :param coordenadas: Cadena con las coordenadas
    :return: Si son válidas o no
    """
    return _ubicacion_por_cadena(coordenadas, 0) is not None
