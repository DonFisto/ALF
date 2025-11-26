import input_formatting
from interprete.normalizacion import imprimir_normalizado
from generador import genera_entrada


def interpretar_comando(comando: list):
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
        file = open(input_file, 'r', encoding='utf-8')
        if len(comando) == 4:
            f1 = comando[2]
            f2 = comando[3]
            imprimir_normalizado(file, f1, f2)
        else:
            imprimir_normalizado(file)
    elif comando[0] == "-generate":
        #GENERADOR
        fichero = comando[1]
        num_entradas = int(comando[2])
        genera_entrada(fichero, num_entradas)
        print("Entrada generada correctamente")
    else:
        # FILTROS
        get_filtered_data(comando)

def get_filtered_data(comando: list):
    file = open(comando.pop(), 'r', encoding='utf-8').readlines()
    data = input_formatting.data_segregation(file)
    while len(comando) > 0:
        if comando[0] == "-sphone":
            telefono = comando[1]

        elif comando[0] == "-snif":
            raise NotImplementedError
            #FILTRO POR NIF
        elif comando[0] == "-stime":
            raise NotImplementedError
            #FILTRO POR HORA
        elif comando[0] == "-slocation":
            raise NotImplementedError
            #FILTRO POR LUGAR
