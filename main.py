import sys
from verificaciones.verificacion_comando import comando_valido
from interprete import interpretar_comando

if __name__ == '__main__':
    if len(sys.argv) < 2 or not comando_valido(" ".join(sys.argv[1:])):
        print("python main.py -n <fichero> [<f1> <f2>]| -sphone <telefono> <fichero> | -snif <NIF> <fichero> |-stime <desde> <hasta> <fichero> | -slocation <desde> <hasta> <fichero>")
        sys.exit(1)
    interpretar_comando(sys.argv[1:])
