from .control_errores import *

def interpretar_comando(comando: list[str]):
    """
    Interpreta los argumentos del comando dado (siempre correcto). Hay tres ramas excluyentes del comando:

    - Normalizar: -n <fichero> [<f1> <f2>]>
    - Generar: -generate <fichero> <num_entradas>
    - Filtrar (Se aceptan varios filtros): -sphone <telefono> <fichero> | -snif <NIF> <fichero> |-stime <desde> <hasta> <fichero> | -slocation <desde> <hasta> <fichero>

    :param comando: Array no vacío con las opciones del comando
    """
    # Importamos las funciones que usaremos y que no queremos que se expongan
    from .filtrado import _get_filtered_data
    from .generador import genera_entrada
    from .normalizacion import imprimir_normalizado
    # Borramos espacios innecesarios del comando.
    comando = [e.strip() for e in comando]
    if comando[0] == "-n":
        # NORMALIZAR
        input_file = comando[1]
        try:
            file = open(input_file, 'r', encoding='utf-8')
            if len(comando) == 4:
                try:
                    f1 = int(comando[2])
                    f2 = int(comando[3])
                    imprimir_normalizado(file, f1, f2)
                except ValueError:
                    salida_error(CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS,
                                 "Formatos especificados no válidos. Los formatos deben estar en {1, 2, 3}")
            else:
                imprimir_normalizado(file)
        except FileNotFoundError:
            salida_error(CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO, input_file)
        except PermissionError:
            salida_error(CODIGO_ERROR_PERMISOS_LECTURA_ARCHIVO, input_file)
    elif comando[0] == "-generate":
        # GENERADOR
        fichero = comando[1]
        try:
            num_entradas = int(comando[2])
            if num_entradas <= 0:
                salida_error(CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS, "El número de entradas debe ser positivo")
            genera_entrada(fichero, num_entradas)
            print("Entrada generada correctamente")
        except ValueError:
            salida_error(CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS, "El número de entradas no es válido")
    else:
        # FILTROS
        nombre_archivo = comando.pop()
        try:
            data = _get_filtered_data(nombre_archivo, comando)
            for entrada in data:
                print(entrada.get_line())

        except ValueError as e:
            salida_error(CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS, str(e))
        except FileNotFoundError:
            salida_error(CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO, nombre_archivo)
        except PermissionError:
            salida_error(CODIGO_ERROR_PERMISOS_LECTURA_ARCHIVO, nombre_archivo)