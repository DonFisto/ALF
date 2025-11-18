from argparse import ArgumentError

from input_formatting import data_segregation
def imprimir_normalizado(archivo, f1=1, f2=2):
    if f1 > 3 or f2 > 3 or f1 < 1 or f2 < 1:
        raise ArgumentError("Formato no válido")
    data = data_segregation(archivo)
    # TODO: Filtrar por no válidos
    for line in data:
        print(line)