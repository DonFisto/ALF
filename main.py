"""
**Autómatas y lenguajes formales, Universidad de Murcia 2025-2026**

Programa de reconocimiento, filtrado y generación de entradas de datos en formato concreto.

Por Javier Albero y Daniel Martínez-Cabeza de Vaca.
"""

from ejecucion import *
from verificaciones import comando_valido

if __name__ == '__main__':
    if len(sys.argv) < 2 or not comando_valido((sys.argv[1:])):
        salida_error(CODIGO_ERROR_MAL_USO)
    interpretar_comando(sys.argv[1:])
