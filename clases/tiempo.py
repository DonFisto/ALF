from argparse import ArgumentError

from verificaciones.verificacion_fecha import fecha_correcta, hora_correcta


class Tiempo:
    """
    Clase que representa un instante de tiempo
    """

    _MESES = [
        "january", "february", "march", "april", "may", "june",
        "july", "august", "september", "october", "november", "december"
    ]
    _NUM_MES = {
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
            num_mes = Tiempo._NUM_MES[mes]
            return num_mes
        except KeyError:
            raise ArgumentError("El mes no existe")

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
