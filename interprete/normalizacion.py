from input_formatting import leer_datos


def imprimir_normalizado(archivo, f1=1, f2=2):
    """
    Imprime los datos válidos normalizados, con los formatos de la fecha y de la ubicación indicados
    :param archivo: Archivo de entrada con los datos
    :param f1: Formato de la fecha (1, 2 o 3)
    :param f2: Formato de la ubicación (1, 2 o 3)
    :raises ValueError: Si alguno de los formatos no son válidos.
    """
    if f1 > 3 or f2 > 3 or f1 < 1 or f2 < 1:
        raise ValueError("Formato no válido")
    data = leer_datos(archivo)
    for entrada in data:
        print(entrada.normalizar(f1, f2))