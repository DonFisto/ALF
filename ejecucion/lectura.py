from clases import Entrada

def leer_datos(fichero) -> list[Entrada]:
    """
    Lee los datos de un fichero de entrada, y devuelve una lista con todas las entradas válidas que encuentre.
    :param fichero: Fichero de entrada
    :return: Lista con las entradas válidas.
    """
    datos = []
    for line in fichero:
        try:
            datos.append(Entrada(line))
        except ValueError:
            # La entrada no es válida porque alguno de los campos tiene un formato incorrecto.
            # Si fuera necesario podríamos capturar la excepción para ver el motivo.
            # Seguimos con el bucle.
            pass
    return datos