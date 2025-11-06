from argparse import ArgumentError

import regex as re
from math import modf
class Ubicacion:
    F1 = r'([-+]?(?:90|[0-8]\d)\.\d+)\s*,\s*([-+]?(?:90|[0-8]\d)\.\d+)'
    F2 = r'(\d|90|[0-8]\d)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(N|S)\s*,\s*(\d{1,2}|[1][0-7]\d|180)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(W|E)'
    F3 = r'0([0-8]\d|90)([0-5]\d)(\d?\d.\d{4})(N|S)(0\d{1,2}|1[0-7]\d|180)([0-5]\d)(\d?\d.\d{4})(W|E)'
    def __init__(self, latitud, longitud):
        if latitud < -90 or latitud > 90:
            raise ArgumentError("La latitud debe estar en el intervalo [-90, 90]")
        if longitud < -180 or longitud > 180:
            raise ArgumentError("La longitud debe estar en el intervalo [-180, 180]")

        self.latitud = latitud
        self.longitud = longitud
    def formato(self, f = 1):
        if f == 1:
            if int(self.latitud) == self.latitud:
                lat_display = f'{self.latitud:.1f}'
            else:
                lat_display = f'{self.latitud}'
            if int(self.longitud) == self.longitud:
                lon_display = f'{self.longitud:.1f}'
            else:
                lon_display = f'{self.longitud}'
            return f'{lat_display}, {lon_display}'
        elif f == 2:
            lat_sexagesimal = (abs(int(self.latitud)), modf(self.latitud) * 60, modf(modf(self.latitud) * 60) * 60)
            lat_direccion = 'N' if self.latitud >= 0 else 'S'
            lon_sexagesimal = (abs(int(self.longitud)), modf(self.longitud) * 60, modf(modf(self.longitud) * 60) * 60)
            lon_direccion = 'E' if self.longitud >= 0 else 'W'

            return f'{lat_sexagesimal[0]}° {lat_sexagesimal[1]}\' {lat_sexagesimal[2]}" {lat_direccion}, {lon_sexagesimal[0]}° {lon_sexagesimal[1]}\' {lon_sexagesimal[2]}" {lon_direccion}'
        elif f == 3:

            return ""


    def get_latitud(self):
        return self.latitud
    def get_longitud(self):
        return self.longitud