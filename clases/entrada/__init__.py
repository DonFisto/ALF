from clases.tiempo import Tiempo
from clases.ubicacion import Ubicacion
from verificaciones.verificaciones_basicas import tlf_valido, nif_valido, descripcion_valida, precio_valido


class Entrada:
    """
    Clase que representa una entrada de datos con los atributos propuestos.
    """

    def __init__(self, line: str):
        """
        Constructor de la clase Entrada. Utiliza la línea de entrada para inicializar los atributos, la cual tiene este formato.
        Los atributos van separados por ';', y van en el siguiente orden:

        - Teléfono
        - Fecha
        - Ubicación
        - Descripción
        - Precio

        :param line: Línea de entrada.
        :raise ValueError: Si la línea de entrada no tiene los atributos estrictamente necesarios, o alguno de los argumentos no cumple con sus posibles formatos.
        """
        self.line = line.strip()
        args = self.line.split(";")
        if len(args) < 6:
            raise ValueError("Faltan argumentos en la línea")
        elif len(args) > 6:
            raise ValueError("Demasiados argumentos en la línea")

        telefono, nif, fecha, ubicacion, descripcion, precio = [arg.strip() for arg in args]

        if tlf_valido(telefono):
            self.tlf = telefono
        else:
            raise ValueError("Teléfono no válido")

        if nif_valido(nif):
            self.nif = nif
        else:
            raise ValueError("NIF no válido")

        try:
            self.fecha = Tiempo.from_string(fecha)
        except ValueError:
            raise ValueError("Fecha no válida")

        try:
            self.ubicacion = Ubicacion.from_string(ubicacion)
        except ValueError:
            raise ValueError("Ubicación no válida")

        if descripcion_valida(descripcion):
            self.descripcion = descripcion
        else:
            raise ValueError("Descripción no válida")

        if precio_valido(precio):
            self.precio = precio
        else:
            raise ValueError("Precio no válido")

    def get_tlf(self) -> str:
        """
        Obtiene el teléfono de la entrada.
        :return: Teléfono de la entrada.
        """
        return self.tlf

    def get_nif(self) -> str:
        """
        Obtiene el NIF de la entrada.
        :return: NIF de la entrada
        """
        return self.nif

    def get_fecha(self) -> Tiempo:
        """
        Obtiene la fecha de la entrada.
        :return: Fecha de la entrada
        """
        return self.fecha

    def get_ubicacion(self):
        """
        Obtiene la ubicación de la entrada.
        :return: Ubicación de la entrada
        """
        return self.ubicacion

    def get_descripcion(self):
        """
        Obtiene la descripción de la entrada.
        :return: Descripción de la entrada
        """
        return self.descripcion

    def get_precio(self):
        """
        Obtiene el precio de la entrada.
        :return: Precio de la entrada
        """
        return self.precio

    def normalizar(self, f1=1, f2=2):
        """
        Normaliza la entrada de acuerdo a los formatos indicados
        :param f1: Formato de la fecha {1, 2, 3}
        :param f2: Formato del
        :return:
        """
        tlf = _normalizar_tlf(self.tlf)
        fecha = self.fecha.formatear(f1)
        ubicacion = self.ubicacion.formatear(f2)
        return f'{tlf} ; {self.nif} ; {fecha} ; {ubicacion} ; {self.descripcion} ; {self.precio}'

    def get_line(self):
        """
        Obtiene la línea de entrada original
        :return: Línea de entrada original
        """
        return self.line


def _normalizar_tlf(tlf: str) -> str:
    """
    Noramliza el teléfono dado, pasandolo de formato "español" a "internacional
    :param tlf: Teléfono a normalizar
    :return: Teléfono en formato internacional
    """
    output = tlf
    if tlf[0] != '+':
        output = "+34" + output
    output = output.replace(" ", "")
    return output
