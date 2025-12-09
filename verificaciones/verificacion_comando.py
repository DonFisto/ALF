import regex as re

# Mapa que asigna a cada opción el número de argumentos que debe tener.
_NUM_ARGUMENTOS = {'n': [1, 3], 'sphone': [2], 'snif': [2], 'stime': [3], 'slocation': [3], 'generate': [2]}
# Array con las opciones válidas para el comando
_OPCIONES_VALIDAS = _NUM_ARGUMENTOS.keys()
# Expresión regular para validar el comando
_ER_COMANDO = R"(-\w+)(?:\s+((?:(?!\s+-\w).)+))?"


def _combinacion_valida(opt1: str, opt2: str | None) -> bool:
    """
    Determina si la combinación de opciones son válidas. Las únicas que se pueden combinar son las de filtrado.
    :param opt1: Primera opción del comando
    :param opt2: Segunda opción del comando. Puede ser None para simbolizar que no hay nada que comparar.
    :return:
    """
    valido = True
    if opt1 == opt2:
        # No se puede repetir la misma opción dos veces
        valido = False
    elif opt1 == "n":
        # La opción de normalizar no es compatible con otras opciones
        valido = opt2 is None
    elif opt1 == "generate":
        # La opción de generar no es compatible con otras opciones
        valido = opt2 is None

    return valido


def comando_valido(comando: list[str]) -> bool:
    """
    Determina si el comando dado es válido.
    :param comando: Lista con los diferentes argumentos del comando.
    :return: Si es válido o no
    """
    # Primero vemos si cuadra con la expresión regular. Guardamos todos los "pedacitos" que cuadran
    opciones = re.findall(_ER_COMANDO, " ".join(comando))

    valido = True

    for i, opcion in enumerate(opciones):
        if valido:
            argumentos = opcion[1]
            # Ejemplo de argumentos: '-n', 'fichero.txt'
            comando_extraido = opcion[0]  # Argumento con el -
            if comando_extraido[1:] not in _OPCIONES_VALIDAS:
                # Si lo que acompaña al guión no es una opción reconocida, el comando no es válido
                valido = False
            else:
                indice_comando = comando.index(comando_extraido)
                argumentos = []
                j = 1
                while indice_comando + j < len(comando) and not comando[indice_comando + j].startswith("-"):
                    if j != 0:  # No nos interesa el primer argumento, el cual es la opción
                        argumentos.append(comando[indice_comando + j])
                    j += 1
                next_option = None

                if indice_comando + j < len(comando):
                    next_option = comando[indice_comando + j][1:]  # Escapamos el guión
                    if not _combinacion_valida(comando_extraido[1:], next_option):
                        # Si la siguiente opción es incompatible con esta, entonces el comando no es válido.
                        valido = False

                if valido:
                    if len(argumentos) in _NUM_ARGUMENTOS[comando_extraido[1:]] and \
                            next_option is not None and \
                            len(argumentos) + 1 != _NUM_ARGUMENTOS[comando_extraido[1:]][0]:
                        valido = False
                    elif len(argumentos) not in _NUM_ARGUMENTOS[comando_extraido[1:]] and next_option is None:
                        valido = False

    return valido
