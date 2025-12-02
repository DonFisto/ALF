import sys

from .filtrado import _get_filtered_data
from .normalizacion import imprimir_normalizado
from interprete.generador import genera_entrada

def interpretar_comando(comando: list[str]):
    """
    Interpreta los argumentos del comando dado (siempre correcto). Hay tres ramas excluyentes del comando:

    - Normalizar: -n <fichero> [<f1> <f2>]>
    - Generar: -generate <fichero> <num_entradas>
    - Filtrar (Se aceptan varios filtros): -sphone <telefono> <fichero> | -snif <NIF> <fichero> |-stime <desde> <hasta> <fichero> | -slocation <desde> <hasta> <fichero>

    :param comando: Array no vacío con las opciones del comando
    """
    if comando[0] == "-n":
        #NORMALIZAR
        input_file = comando[1]
        try:
            file = open(input_file, 'r', encoding='utf-8')
            if len(comando) == 4:
                try:
                    f1 = int(comando[2])
                    f2 = int(comando[3])
                    imprimir_normalizado(file, f1, f2)
                except ValueError:
                    print("Formatos especificados no válidos. Los formatos deben estar en {1, 2, 3}", flush=sys.stderr)
                    sys.exit(1)
            else:
                imprimir_normalizado(file)
        except FileNotFoundError:
            print(f"Archivo {input_file} no encontrado", flush=sys.stderr)
            sys.exit(1)
        except PermissionError:
            print(f"No se tienen permisos para abrir el archivo {input_file}", flush=sys.stderr)
            sys.exit(1)
    elif comando[0] == "-generate":
        #GENERADOR
        fichero = comando[1]
        num_entradas = int(comando[2])
        genera_entrada(fichero, num_entradas)
        print("Entrada generada correctamente")
    else:
        # FILTROS
        try:
            data = _get_filtered_data(comando)
            for entrada in data:
                print(entrada.get_line())
        except ValueError as e:
            print(e)
            sys.exit(1)
