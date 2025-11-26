from argparse import ArgumentError
import regex as re
from verificaciones.verificacion_fecha import fecha_correcta, hora_correcta


class Tiempo:
    """
    Clase que representa un instante de tiempo
    """

    F1 = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})'
    F2 = r'(january|february|march|april|may|june|july|august|september|october|november|december) (\d{1,2}), (\d{4}) (\d{1,2}):(\d{2}) (am|pm)'
    F3 = r'(\d{2}):(\d{2}):(\d{2}) (\d{2})/(\d{2})/(\d{4})'

    _MESES = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    NUM_MES = {
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
        :raises ArgumentError: Si los valores de la fecha no son válidos.
        """
        if hora_correcta(hora, minutos, segundos) and fecha_correcta(dia, mes, anyo):
            self.dia = dia
            self.mes = mes
            self.anyo = anyo
            self.hora = hora
            self.minutos = minutos
            self.segundos = segundos
        else:
            raise ArgumentError("Fecha incorrecta")

    @staticmethod
    def numero_mes_to_nombre(mes):
        """
        Devuelve el número del mes dado.
        :param mes: Nombre del mes en inglés. Las mayúsculas y minúsculas son indiferentes.
        :return: Número del mes correspondiente
        :raises ArgumentError: Si el mes no existe
        """
        mes = mes.lower()
        try:
            num_mes = Tiempo.NUM_MES[mes]
            return num_mes
        except KeyError:
            raise ArgumentError("El mes no existe")

    @staticmethod
    def from_string(string : str, f: int = 0):
        tiempo = Tiempo.tiempo_por_cadena(string, f)
        if tiempo is not None:
            return tiempo
        else:
            raise ArgumentError("La cadena no cumple con ningún formato")

    @staticmethod
    def tiempo_por_cadena(cadena: str, formato: int):
        if formato == 0:
            return Tiempo.tiempo_por_cadena(cadena, 1) or Tiempo.tiempo_por_cadena(cadena, 2) or Tiempo.tiempo_por_cadena(
                cadena, 3)
        elif formato == 1:
            return Tiempo.formato1(cadena)
        elif formato == 2:
            return Tiempo.formato2(cadena)
        elif formato == 3:
            return Tiempo.formato3(cadena)
        else:
            raise ArgumentError("El formato debe ser 1, 2, 3 o 0 (automático)")
    @staticmethod
    def formato1(cadena):
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
        except ArgumentError:
            return None
    @staticmethod
    def formato2(cadena):
        valido = re.fullmatch(
            Tiempo.F2,
            cadena, re.IGNORECASE)
        if not valido:
            return False
        anio = int(valido.group(3))
        mes = valido.group(1).lower()
        mes = Tiempo.NUM_MES[mes]
        dia = int(valido.group(2))
        hora = int(valido.group(4))
        if valido.group(6) == "pm" and hora != 12:
            hora += 12
        elif valido.group(6) == "am" and hora == 12:
            hora = 0
        minuto = int(valido.group(5))
        try:
            return Tiempo(anio, mes, dia, hora, minuto, 0)
        except ArgumentError:
            return None

    @staticmethod
    def formato3(cadena):
        valido = re.fullmatch(Tiempo.F3, cadena)
        if not valido:
            return False
        anio = int(valido.group(6))
        mes = int(valido.group(5))
        dia = int(valido.group(4))
        hora = int(valido.group(1))
        minuto = int(valido.group(2))
        segundos = int(valido.group(3))
        try:
            return Tiempo(anio, mes, dia, hora, minuto, segundos)
        except ArgumentError:
            return None

    def formatear(self, f=1) -> str:
        """
        Formatea el instante temporal a una cadena.
        :param f: Formato al que formatear el instante temporal
        :return: Cadena del instante temporal formateado.
        :raises ArgumentError: Si el formato no está en {1, 2, 3}
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
            return f'{Tiempo._MESES[self.mes - 1]:02} {self.dia}, {self.anyo} {hora_en_12[0]:02}:{self.minutos:02} {hora_en_12[1]}'
        elif f == 3:
            return f'{self.hora:02}:{self.minutos:02}:{self.segundos:02} {self.dia:02}/{self.mes:02}/{self.anyo:04}'
        else:
            raise ArgumentError("Formato incorrecto")
