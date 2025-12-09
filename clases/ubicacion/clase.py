from math import asin, sqrt, sin, cos, radians, modf

# Radio de la Tierra expresado en kilómetros.
_RADIO_TIERRA = 6367.45


class Ubicacion:
    """
    Clase que representa una ubicación en el mapa, con sus coordenadas.
    """

    def __init__(self, latitud: float, longitud: float):
        """
        Constructor de la clase Ubicación
        :param latitud: Latitud de la ubicación (En [-90, 90])
        :param longitud: Longitud de la ubicación (En [-180, 180])
        :raises ValueError: Si la latitud o la longitud se encuentran en intervalos erróneos.
        """
        if latitud < -90 or latitud > 90:
            raise ValueError("La latitud debe estar en el intervalo [-90, 90]")
        if longitud < -180 or longitud > 180:
            raise ValueError("La longitud debe estar en el intervalo [-180, 180]")

        self._latitud = latitud
        self._longitud = longitud

    @staticmethod
    def from_string(string, f=0):
        """
        Obtiene una ubicación por una cadena bien formateada.
        :param string: Cadena formateada de la que obtener la ubicación
        :param f: Formato de la cadena. Si es 0, intentará hacerlo para todos los formatos.
        :return: Ubicación
        :raises: ValueError: Si la cadena no cumple con el formato dado
        """
        from .formato import _ubicacion_por_cadena

        ubicacion = _ubicacion_por_cadena(string, f)
        if ubicacion is not None:
            return ubicacion
        else:
            raise ValueError("La cadena no cumple con ningún formato")

    @staticmethod
    def distancia_geografica(lat1, lon1, lat2, lon2):
        """
        Determina la distancia geográfica entre dos puntos dadas sus coordenadas en la tierra.
        :param lat1: Latitud del primer punto.
        :param lon1: Longitud del primer punto.
        :param lat2: Latitud del segundo punto.
        :param lon2: Longitud del segundo punto.
        :return: Distancia geográfica en kilómetros.
        """
        return 2 * _RADIO_TIERRA * asin(
            sqrt(sin((lat1 - lat2) / 2) ** 2 + cos(lat1) * cos(lat2) * (sin((lon1 - lon2) / 2) ** 2)))

    def distancia_con(self, rhs):
        """
        Calcula la distancia en kilómetros con otra ubicación.
        :param rhs: Otra ubicación
        :return: Distancia entre las dos ubicaciones.
        :raises ValueError: Si `rhs` no es una Ubicación.
        """
        if not isinstance(rhs, Ubicacion):
            raise ValueError("La ubicación debe ser válida")
        lat1 = radians(self._latitud)
        lon1 = radians(self._longitud)
        lat2 = radians(rhs.get_latitud())
        lon2 = radians(rhs.get_longitud())
        return Ubicacion.distancia_geografica(lat1, lon1, lat2, lon2)

    def formatear(self, f=1) -> str:
        """
        Formatea la ubicación a una cadena.
        :param f: Formato de la cadena (Por defecto es el 1)
        :return: Cadena de la ubicación formateada
        """
        if f == 1:
            if int(self._latitud) == self._latitud:
                lat_display = f'{self._latitud:.1f}'
            else:
                lat_display = f'{self._latitud}'
            if int(self._longitud) == self._longitud:
                lon_display = f'{self._longitud:.1f}'
            else:
                lon_display = f'{self._longitud}'
            output = f'{lat_display}, {lon_display}'
        elif f == 2 or f == 3:
            lat_sexagesimal = (abs(int(self._latitud)), abs(int(modf(self._latitud)[0] * 60)),
                               abs(modf(modf(self._latitud)[0] * 60)[0] * 60))
            lat_direccion = 'N' if self._latitud >= 0 else 'S'
            lon_sexagesimal = (abs(int(self._longitud)), abs(int(modf(self._longitud)[0] * 60)),
                               abs(modf(modf(self._longitud)[0] * 60)[0] * 60))
            lon_direccion = 'E' if self._longitud >= 0 else 'W'
            if f == 2:
                output = f'{lat_sexagesimal[0]}° {lat_sexagesimal[1]}\' {lat_sexagesimal[2]:.04f}" {lat_direccion}, {lon_sexagesimal[0]}° {lon_sexagesimal[1]}\' {lon_sexagesimal[2]:.4f}" {lon_direccion}'
            else:  # f == 3
                output = f'{lat_sexagesimal[0]:03}{lat_sexagesimal[1]:02}{lat_sexagesimal[2]:02.4f}{lat_direccion}{lon_sexagesimal[0]:03}{lon_sexagesimal[1]:02}{lon_sexagesimal[2]:02.4f}{lon_direccion}'
        else:
            raise ValueError("El formato debe ser 1, 2 o 3")
        return output

    def get_latitud(self) -> float:
        """
        Obtiene la latitud
        :return: latitud de la ubicación
        """
        return self._latitud

    def get_longitud(self) -> float:
        """
        Obtiene la longitud
        :return: longitud de la ubicación
        """
        return self._longitud
