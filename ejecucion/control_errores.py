import sys

CODIGO_ERROR_MAL_USO = 1
CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO = 2
CODIGO_ERROR_PERMISOS_ARCHIVO = 3
CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS = 4
CODIGO_ERROR_ARCHIVO_ES_DIRECTORIO = 5
CODIGO_ERROR_DE_SISTEMA_GENERICO = 6


def salida_error(codigo: int, mensaje: str = ""):
    """
    Provoca una salida del programa, con un determinado error, los cuales son los siguientes:

    - {CODIGO_ERROR_MAL_USO}: Mal uso del programa. El mensaje corresponde a la explicación.
    - {CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO}: Archivo no encontrado. El mensaje corresponde al nombre del archivo.
    - {CODIGO_ERROR_PERMISOS_ARCHIVO}: Error de permisos de lectura del archivo. El mensaje corresponde al nombre del archivo.
    - {CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS}: Error en los argumentos del comando. El mensaje corresponde a la explicación
    - {CODIGO_ERROR_ARCHIVO_ES_DIRECTORIO}: El archivo especificado es un directorio. El mensaje corresponde al nombre del directorio.
    - {CODIGO_ERROR_DE_SISTEMA_GENERICO}: Error desconocido (distinto al resto) del sistema operativo. El mensaje corresponde al error.
    :param codigo: Código de error de salida del programa.
    :param mensaje: Mensaje que complementa al error.
    """
    if codigo == CODIGO_ERROR_MAL_USO:
        print(f"Mal uso. {mensaje}", file=sys.stderr)
        print(f"Uso correcto:", file=sys.stderr)
        print(f"- Normalizar: python {sys.argv[0]} -n <archivo> [<f1> <f2>]", file=sys.stderr)
        print(f"- Generar: python {sys.argv[0]} -generate <archivo> <num_entradas>", file=sys.stderr)
        print(
            f"- Filtrar: python {sys.argv[0]} (-sphone <telefono> | -snif <NIF> | -stime <desde> <hasta> | -slocation <desde> <hasta>) <fichero>",
            file=sys.stderr)
    elif codigo == CODIGO_ERROR_ARCHIVO_NO_ENCONTRADO:
        print(f"El archivo {mensaje} no existe", file=sys.stderr)
    elif codigo == CODIGO_ERROR_PERMISOS_ARCHIVO:
        print(f"No se tienen permisos sobre el archivo {mensaje}", file=sys.stderr)
    elif codigo == CODIGO_ERROR_ARGUMENTOS_NO_VALIDOS:
        print(f"Argumentos no válidos: {mensaje}", file=sys.stderr)
    elif codigo == CODIGO_ERROR_ARCHIVO_ES_DIRECTORIO:
        print(f"El archivo {mensaje} es un directorio", file=sys.stderr)
    elif codigo == CODIGO_ERROR_DE_SISTEMA_GENERICO:
        print(f"Error desconocido del sistema operativo: {mensaje}", file=sys.stderr)
    else:
        print(f"Error desconocido: {codigo}", file=sys.stderr)
    sys.exit(codigo)
