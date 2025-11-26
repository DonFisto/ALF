from argparse import ArgumentError

from clases.tiempo import Tiempo
from clases.ubicacion import Ubicacion, coordenadas_validas
from verificaciones.verificacion_fecha import tiempo_valido
from verificaciones.verificaciones_basicas import tlf_valido, nif_valido, descripcion_valida, precio_valido


class Entrada:

    def __init__(self, telefono:str, nif:str, fecha:Tiempo, ubicacion:Ubicacion, descripcion:str, precio:str, line: str = None):
        if tlf_valido(telefono):
            self.tlf = telefono
        else:
            raise ArgumentError("Teléfono no válido")
        if nif_valido(nif):
            self.nif = nif
        else:
            raise ArgumentError("NIF no válido")
        if tiempo_valido(fecha):
            self.fecha = fecha
        else:
            raise ArgumentError("Fecha no válida")
        if coordenadas_validas(ubicacion):
            self.ubicacion = ubicacion
        else:
            raise ArgumentError("Ubicación no válida")
        if descripcion_valida(descripcion):
            self.descripcion = descripcion
        else:
            raise ArgumentError("Descripción no válida")
        if precio_valido(precio):
            self.precio = precio
        else:
            raise ArgumentError("Precio no válido")

        self.line = line

    def get_tlf(self):
        return self.tlf
    def set_tlf(self, tlf:str):
        if tlf_valido(tlf):
            self.tlf = tlf
        else:
            raise ArgumentError
    def get_nif(self):
        return self.nif
    def set_nif(self, nif:str):
        if nif_valido(nif):
            self.nif = nif
        else:
            raise ArgumentError
    def get_fecha(self):
        return self.fecha
    def set_fecha(self, fecha:Tiempo):
        if tiempo_valido(fecha):
            self.fecha = fecha
        else:
            raise ArgumentError
    def get_ubicacion(self):
        return self.ubicacion
    def set_ubicacion(self, ubicacion:Ubicacion):
        if coordenadas_validas(ubicacion):
            self.ubicacion = ubicacion
        else:
            raise ArgumentError
    def get_descripcion(self):
        return self.descripcion
    def set_descripcion(self, descripcion:str):
        if descripcion_valida(descripcion):
            self.descripcion = descripcion
        else:
            raise ArgumentError
    def get_precio(self):
        return self.precio
    def set_precio(self, precio:str):
        if precio_valido(precio):
            self.precio = precio
        else:
            raise ArgumentError

    @staticmethod
    def from_line(line:str):
        args = line.split(";")
        if len(args) < 6:
            raise ArgumentError("La línea no tiene suficientes datos")
        return Entrada(*line.split(';'), line)

    @staticmethod
    def normalizar_tlf(tlf:str):
        output = tlf
        if tlf[0] != '+':
            output = "+34" + output
        output = output.replace(" ","")
        return output
    def normalizar(self, f1 = 1, f2 = 2):
        tlf = self.normalizar_tlf(self.tlf)
        fecha = self.fecha.formatear(f1)
        ubicacion = self.ubicacion.formatear(f2)
        return f'{tlf} ; {self.nif} ; {fecha} ; {ubicacion} ; {ubicacion} ; {self.descripcion} ; {self.precio}'

