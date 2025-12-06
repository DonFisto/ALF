import sys
from verificaciones.verificacion_comando import comando_valido
from interprete import interpretar_comando, salida_error

if __name__ == '__main__':
    if len(sys.argv) < 2 or not comando_valido(" ".join(sys.argv[1:])):
        salida_error(1)
    interpretar_comando(sys.argv[1:])
