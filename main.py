import sys
import input_formatting as form
from verificaciones.verificacion_comando import comando_valido
from interprete.interpretar_comando import interpretar_comando
if __name__ == '__main__':
    if len(sys.argv) < 2 or not comando_valido(" ".join(sys.argv[1:])):
        print("python main.py -n <fichero> [<f1> <f2>]| -sphone <telefono> <fichero> | -snif <NIF> <fichero> |-stime <desde> <hasta> <fichero> | -slocation <desde> <hasta> <fichero>")
        sys.exit(1)
    input_file = sys.argv[2]
    file = open(input_file, 'r', encoding='utf-8')
    """datos = form.data_segregation(file)
    print(form.verificacion_datos(datos))"""
    interpretar_comando(sys.argv[1:])
