from clases.entrada import Entrada

def leer_datos(fichero) -> list[Entrada]:
    datos = []
    for line in fichero:
        try:
            datos.append(Entrada(line))
        except ValueError:
            continue

    return datos