from verificaciones import comando_valido
from interprete import *

if __name__ == '__main__':
    if len(sys.argv) < 2 or not comando_valido((sys.argv[1:])):
        salida_error(CODIGO_ERROR_MAL_USO)
    interpretar_comando(sys.argv[1:])
