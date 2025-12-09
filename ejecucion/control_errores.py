import sys

CODIGO_ERROR_MAL_USO = 1
CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO = 2
CODIGO_ERROR_PERMISOS_LECTURA_ARCHIVO = 3
CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS = 4

def salida_error(codigo: int, mensaje: str = ""):
    f"""
    Provoca una salida del programa, con un determinado error, los cuales son los siguientes:

    - {CODIGO_ERROR_MAL_USO}: Mal uso del programa. El mensaje corresponde a la explicación.
    - {CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO}: Archivo no encontrado. El mensaje corresponde al nombre del archivo.
    - {CODIGO_ERROR_PERMISOS_LECTURA_ARCHIVO}: Error de permisos de lectura del archivo. El mensaje corresponde al nombre del archivo.
    - {CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS}: Error en los argumentos del comando. El mensaje corresponde a la explicación
    :param codigo: Código de error de salida del programa.
    :param mensaje: Mensaje que complementa al error.
    """
    if codigo == CODIGO_ERROR_MAL_USO:
        print(f"Mal uso. {mensaje}", file=sys.stderr)
        print(f"Uso correcto:", file=sys.stderr)
        print(f"- Normalizar: python {sys.argv[0]} -n <archivo> [<f1> <f2>]", file=sys.stderr)
        print(f"- Generar: python {sys.argv[0]} -generate <archivo> <num_entradas>", file=sys.stderr)
        print(f"- Filtrar: python {sys.argv[0]} (-sphone <telefono> | -snif <NIF> | -stime <desde> <hasta> | -slocation <desde> <hasta>) <fichero>", file=sys.stderr)
    elif codigo == CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO:
        print(f"El archivo {mensaje} no existe", file=sys.stderr)
    elif codigo == CODIGO_ERROR_PERMISOS_LECTURA_ARCHIVO:
        print(f"No se tienen permisos de lectura para leer el archivo {mensaje}", file=sys.stderr)
    elif codigo == CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS:
        print(f"Argumentos no válidos: {mensaje}", file=sys.stderr)
    else:
        print(f"Error desconocido: {codigo}", file=sys.stderr)
    sys.exit(codigo)
