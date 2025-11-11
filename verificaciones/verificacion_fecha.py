import re


def tiempo_valido(fecha):
    return formato1_valido(fecha) or formato2_valido(fecha) or formato3_valido(fecha)
def formato1_valido(fecha):
    valido = re.fullmatch(r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})', fecha)
    if not valido:
        return False
    anio = int(valido.group(1))
    mes = int(valido.group(2))
    dia = int(valido.group(3))
    hora = int(valido.group(4))
    minuto = int(valido.group(5))
    valido = fecha_correcta(anio, mes, dia) and hora_correcta(hora, minuto)
    return bool(valido)
def formato2_valido(fecha):
    #TODO MESES EN MINUSCULA/MAYUSCULA VALIDOS
    # TODO: Recomendación de Javi: usa `Tiempo.num_mes_to_nombre`
    valido = re.fullmatch(r'(january|february|march|april|may|june|july|august|september|october|november|december) \d{1,2}, \d{4} \d{1,2}:\d{2}(am|pm)', fecha, re.IGNORECASE)
    if not valido:
        return False
    anio = int(valido.group(3))
    mes = valido.group(1).lower()
    mes = int(mes_a_numero(mes))
    dia = int(valido.group(2))
    hora = int(valido.group(4))
    if hora < 12: hora += 12
    minuto = int(valido.group(5))
    valido = fecha_correcta(anio, mes, dia) and hora_correcta(hora, minuto)
    return bool(valido)
def formato3_valido(fecha):
    valido = re.fullmatch(r'(\d{2}):(\d{2}):(\d{2}) (\d{2})/(\d{2})/(\d{4})', fecha)
    if not valido:
        return False
    anio = int(valido.group(6))
    mes = int(valido.group(5))
    dia = int(valido.group(4))
    hora = int(valido.group(1))
    minuto = int(valido.group(2))
    segundos = int(valido.group(3))
    valido = fecha_correcta(anio, mes, dia) and hora_correcta(hora, minuto, segundos)
    return bool(valido)
def bisiesto(anio):
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False

def fecha_correcta(anio, mes=9, dia=9):
    if anio < 0 or mes < 0 or dia < 0:
        return False
    if dia > 31:
        return False
    if mes > 12:
        return False
    if not (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes ==12):
       if dia > 30:
           return False
       elif (mes == 2):
           if bisiesto(anio) and dia > 29:
               return False
           elif dia > 28:
               return False
    return True
def hora_correcta(hora, minutos, segundos=0):
    if hora > 23 or hora < 0:
        return False
    if minutos > 59 or minutos < 0:
        return False
    if segundos > 59 or segundos < 0:
        return False
    return True
def mes_a_numero(mes):
    meses = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    return meses.index(mes)+1
def numero_a_mes(mes):
    meses = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    return meses[mes-1]