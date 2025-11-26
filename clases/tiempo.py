import regex as re


class Tiempo:
    """
    Clase que representa un instante de tiempo
    """

    # Expresión regular del formato 1
    F1 = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})'
    # Expresión regular del formato 2
    F2 = r'(january|february|march|april|may|june|july|august|september|october|november|december) (\d{1,2}), (\d{1,4}) (\d{1,2}):(\d{2}) (am|pm)'
    # Expresión regular del formato 3
    F3 = r'(\d{2}):(\d{2}):(\d{2}) (\d{2})/(\d{2})/(\d{4})'

    # Array que relaciona el número del mes con su nombre en inglés
    _NUM_MES_A_NOMBRE = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    # Mapa que relaciona el nombre del mes con su número
    _NOMBRE_MES_A_NUMERO = {
        "january": 1,
        "february": 2,
        "march": 3,
        "april": 4,
        "may": 5,
        "june": 6,
        "july": 7,
        "august": 8,
        "september": 9,
        "october": 10,
        "november": 11,
        "december": 12
    }

    def __init__(self, dia: int, mes: int, anyo: int, hora: int, minutos: int, segundos: int):
        """
        Constructor de la clase Tiempo
        :param dia: Día del instante temporal
        :param mes: Mes del instante temporal
        :param anyo: Año del instante temporal
        :param hora: Hora del instante temporal
        :param minutos: Minutos del instante temporal
        :param segundos: Segundos del instante temporal
        :raises ValueError: Si los valores de la fecha no son válidos.
        """
        if Tiempo._hora_correcta(hora, minutos, segundos) and Tiempo._fecha_correcta(dia, mes, anyo):
            self.dia = dia
            self.mes = mes
            self.anyo = anyo
            self.hora = hora
            self.minutos = minutos
            self.segundos = segundos
        else:
            raise ValueError("Fecha incorrecta")

    @staticmethod
    def nombre_mes_to_numero(mes: str):
        """
        Devuelve el número del mes dado.
        :param mes: Nombre del mes en inglés. Las mayúsculas y minúsculas son indiferentes.
        :return: Número del mes correspondiente
        :raises ValueError: Si el mes no existe
        """
        mes = mes.lower()
        try:
            num_mes = Tiempo._NOMBRE_MES_A_NUMERO[mes]
            return num_mes
        except KeyError:
            raise ValueError("El mes no existe")

    @staticmethod
    def numero_mes_to_nombre(mes: int):
        """
        Devuelve el nombre del mes en inglés, dado su número.
        :param mes: Número del mes
        :return: Nombre en inglés del mes
        :raises ValueError: Si el mes no existe
        """
        if mes < 1 or mes > 12:
            raise ValueError("El mes no existe")
        return Tiempo._NUM_MES_A_NOMBRE[mes - 1]

    @staticmethod
    def from_string(string: str, f: int = 0):
        """
        Obtiene un tiempo a partir de una cadena en un formato determinado. Extensión pública de la función protegida `tiempo_por_cadena`
        :param string: Cadena de texto con el tiempo
        :param f: Formato en el que se encuentra la cadena {1, 2, 3}. Si vale 0, buscará todos los formatos (formato automático)
        :return: Tiempo correspondiente a la cadena
        :raise ValueError: Si la cadena no cumple con ningún formato, o si el formato dado no está en {0, 1, 2, 3}
        """
        tiempo = _tiempo_por_cadena(string, f)
        if tiempo is not None:
            return tiempo
        else:
            raise ValueError("La cadena no cumple con ningún formato")

    def formatear(self, f=1) -> str:
        """
        Formatea el instante temporal a una cadena.
        :param f: Formato al que formatear el instante temporal
        :return: Cadena del instante temporal formateado.
        :raises ValueError: Si el formato no está en {1, 2, 3}
        """
        if f == 1:
            return f'{self.anyo:04}-{self.mes:02}-{self.dia:02} {self.hora:02}:{self.minutos:02}'
        elif f == 2:
            if self.hora == 0:
                hora_en_12 = [12, 'AM']
            elif self.hora > 12:
                hora_en_12 = [self.hora % 12, 'PM']
            else:
                hora_en_12 = [self.hora, 'AM']
            return f'{Tiempo._NUM_MES_A_NOMBRE[self.mes - 1]:02} {self.dia}, {self.anyo} {hora_en_12[0]:02}:{self.minutos:02} {hora_en_12[1]}'
        elif f == 3:
            return f'{self.hora:02}:{self.minutos:02}:{self.segundos:02} {self.dia:02}/{self.mes:02}/{self.anyo:04}'
        else:
            raise ValueError("Formato incorrecto")

    @staticmethod
    def bisiesto(anio):
        if anio % 400 == 0:
            return True
        elif anio % 100 == 0:
            return False
        elif anio % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def _fecha_correcta(anio, mes, dia) -> bool:
        if anio < 0 or mes < 0 or dia < 0:
            return False
        if dia > 31:
            return False
        if mes > 12:
            return False
        if not (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
            if dia > 30:
                return False
            elif mes == 2:
                if Tiempo.bisiesto(anio) and dia > 29:
                    return False
                elif dia > 28:
                    return False
        return True

    @staticmethod
    def _hora_correcta(hora, minutos, segundos=0) -> bool:
        if hora > 23 or hora < 0:
            return False
        if minutos > 59 or minutos < 0:
            return False
        if segundos > 59 or segundos < 0:
            return False
        return True

def _tiempo_por_cadena(cadena: str, formato: int) -> Tiempo | None:
    """
    Intenta obtener un tiempo a partir de una cadena en un formato determinado.
    :param cadena: Cadena de texto con el tiempo
    :param formato: Formato en el que se encuentra la cadena {1, 2, 3}. Si vale 0, buscará todos los formatos (formato automático)
    :return: Tiempo correspondiente a la cadena, o ´None´ si la cadena no cuadra con el formato dado.
    """
    if formato == 0:
        return _tiempo_por_cadena(cadena, 1) or _tiempo_por_cadena(cadena,2) or _tiempo_por_cadena(cadena, 3)
    elif formato == 1:
        return _formato1(cadena)
    elif formato == 2:
        return _formato2(cadena)
    elif formato == 3:
        return _formato3(cadena)
    else:
        raise ValueError("El formato debe ser 1, 2, 3 o 0 (automático)")


def _formato1(cadena) -> Tiempo | None:
    valido = re.fullmatch(Tiempo.F1, cadena)
    if not valido:
        return None
    anio = int(valido.group(1))
    mes = int(valido.group(2))
    dia = int(valido.group(3))
    hora = int(valido.group(4))
    minuto = int(valido.group(5))
    try:
        return Tiempo(anio, mes, dia, hora, minuto, 0)
    except ValueError:
        return None


def _formato2(cadena) -> Tiempo | None:
    valido = re.fullmatch(
        Tiempo.F2,
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
        return Tiempo(anio, mes, dia, hora, minuto, 0)
    except ValueError:
        return None

def _formato3(cadena) -> Tiempo | None:
    valido = re.fullmatch(Tiempo.F3, cadena)
    if not valido:
        return None
    anio = int(valido.group(6))
    mes = int(valido.group(5))
    dia = int(valido.group(4))
    hora = int(valido.group(1))
    minuto = int(valido.group(2))
    segundos = int(valido.group(3))
    try:
        return Tiempo(anio, mes, dia, hora, minuto, segundos)
    except ValueError:
        return None
