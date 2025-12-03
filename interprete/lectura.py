from clases.entrada import Entrada

def leer_datos(fichero) -> list[Entrada]:
    """
    Lee los datos de un fichero de entrada, y devuelve una lista con todas las entradas válidas que encuentre.
    :param fichero: Fichero de entrada
    :return: Lista con las entradas válidas.
    """
    datos = []
    datos_incorrectos = []
    for line in fichero:
        try:
            datos.append(Entrada(line))
        except ValueError:
            # La entrada no es válida porque alguno de los campos tiene un formato incorrecto. Seguimos con el bucle.
            raise ValueError(f"Error en datos encontrado: {line}")
            datos_incorrectos.append(line)
            continue
    print("Los datos incorrectos son:\n", *datos_incorrectos, sep="\n")
    return datos