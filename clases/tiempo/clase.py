from functools import total_ordering

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

from .verificacion import _hora_correcta, _fecha_correcta, _es_bisiesto


@total_ordering  # Generar automáticamente el resto de funciones de relación de orden
class Tiempo:
    """
    Clase que representa un instante de tiempo
    """

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
        if _hora_correcta(hora, minutos, segundos) and _fecha_correcta(anyo, mes, dia):
            self._dia = dia
            self._mes = mes
            self._anyo = anyo
            self._hora = hora
            self._minutos = minutos
            self._segundos = segundos
        else:
            raise ValueError("Fecha incorrecta")

    def __eq__(self, other):
        return (self._anyo, self._mes, self._dia, self._hora, self._minutos, self._segundos) == (other.get_anyo(),
                                                                                                 other.get_mes(),
                                                                                                 other.get_dia(),
                                                                                                 other.get_hora(),
                                                                                                 other.get_minuto(),
                                                                                                 other.get_segundo())

    def __lt__(self, other):
        if self._anyo < other.get_anyo():
            return True
        elif self._anyo == other.get_anyo() and self._mes < other.get_mes():
            return True
        elif self._anyo == other.get_anyo() and self._mes == other.get_mes() and self._dia < other.get_dia():
            return True
        elif self._anyo == other.get_anyo() and self._mes == other.get_mes() and self._dia == other.get_dia() and self._hora < other.get_hora():
            return True
        elif self._anyo == other.get_anyo() and self._mes == other.get_mes() and self._dia == other.get_dia() and self._hora == other.get_hora() and self._minutos < other.get_minutos():
            return True
        elif self._anyo == other.get_anyo() and self._mes == other.get_mes() and self._dia == other.get_dia() and self._hora == other.get_hora() and self._minutos == other.get_minutos() and self._segundos < other.get_segundos():
            return True
        else:
            return False

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
            num_mes = _NOMBRE_MES_A_NUMERO[mes]
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
        return _NUM_MES_A_NOMBRE[mes - 1]

    @staticmethod
    def from_string(string: str, f: int = 0):
        """
        Obtiene un tiempo a partir de una cadena en un formato determinado. Extensión pública de la función protegida `tiempo_por_cadena`
        :param string: Cadena de texto con el tiempo
        :param f: Formato en el que se encuentra la cadena {1, 2, 3}. Si vale 0, buscará todos los formatos (formato automático)
        :return: Tiempo correspondiente a la cadena
        :raise ValueError: Si la cadena no cumple con ningún formato, o si el formato dado no está en {0, 1, 2, 3}
        """
        from .formato import _tiempo_por_cadena
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
            return f'{self._anyo:04}-{self._mes:02}-{self._dia:02} {self._hora:02}:{self._minutos:02}'
        elif f == 2:
            if self._hora == 0:
                hora_en_12 = [12, 'AM']
            elif self._hora > 12:
                hora_en_12 = [self._hora % 12, 'PM']
            else:
                hora_en_12 = [self._hora, 'AM']
            return f'{_NUM_MES_A_NOMBRE[self._mes - 1]} {self._dia}, {self._anyo} {hora_en_12[0]:02}:{self._minutos:02} {hora_en_12[1]}'
        elif f == 3:
            return f'{self._hora:02}:{self._minutos:02}:{self._segundos:02} {self._dia:02}/{self._mes:02}/{self._anyo:04}'
        else:
            raise ValueError("Formato incorrecto")

    @staticmethod
    def bisiesto(anio):
        return _es_bisiesto(anio)

    def get_dia(self):
        return self._dia

    def get_mes(self):
        return self._mes

    def get_anyo(self):
        return self._anyo

    def get_hora(self):
        return self._hora

    def get_minutos(self):
        return self._minutos

    def get_segundos(self):
        return self._segundos
