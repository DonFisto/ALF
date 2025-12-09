def _es_bisiesto(anio: int) -> bool:
    """
    Determina si un año es bisiesto.
    :param anio: Año a comprobar
    :return: Si es bisiesto o no
    """
    if anio % 400 == 0:
        bisiesto = True
    elif anio % 100 == 0:
        bisiesto = False
    elif anio % 4 == 0:
        bisiesto = True
    else:
        bisiesto = False
    return bisiesto


def _fecha_correcta(anio: int, mes: int, dia: int) -> bool:
    """
    Determina si la terna dada forma una fecha válida.
    :param anio: Año de la fecha
    :param mes: Número del mes de la fecha
    :param dia: Día del mes de la fecha
    :return: Si es correcta o no
    """
    valido = True
    if anio < 0 or mes < 0 or dia < 0:
        valido = False
    elif dia > 31:
        valido = False
    elif mes > 12:
        valido = False
    elif not (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
        if dia > 30:
            valido = False
        elif mes == 2:
            es_bisiesto = _es_bisiesto(anio)
            if es_bisiesto and dia > 29:
                valido = False
            elif not es_bisiesto and dia > 28:
                valido = False
    return valido


def _hora_correcta(hora: int, minutos: int, segundos: int = 0) -> bool:
    """
    Determina si la terna dada constituye una hora con minutos y segundos válidos.
    :param hora:
    :param minutos:
    :param segundos:
    :return: Si la hora dada es válida o no
    """
    valido = True
    if hora > 23 or hora < 0:
        valido = False
    if minutos > 59 or minutos < 0:
        valido = False
    if segundos > 59 or segundos < 0:
        valido = False
    return valido
