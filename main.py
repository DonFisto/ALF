import sys
import input_formatting as form
import re
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("python main.py -n <fichero> [<f1> <f2>]| -sphone <telefono> <fichero> | -snif <NIF> <fichero> |-stime <desde> <hasta> <fichero> | -slocation <desde> <hasta> <fichero>")
        sys.exit(1)
    input_file = sys.argv[1]
    file = open(input_file, 'r', encoding='utf-8')
    datos = form.data_segregation(file)
    print(form.verificacion_datos(datos))
