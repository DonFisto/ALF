import regex as re

# Mapa que asigna a cada opción el número de argumentos que debe tener.
_NUM_ARGUMENTOS = {'n': [1, 3], 'sphone': [2], 'snif': [2], 'stime': [2], 'slocation': [3], 'generate': [2]}
# Array con las opciones válidas para el comando
_OPCIONES_VALIDAS = _NUM_ARGUMENTOS.keys()
# Expresión regular para validar el comando
_ER_COMANDO = R"(-\w+(?: +.+)* *)"

def combinacion_valida(opt1, opt2) -> bool:
    if opt2 is None or opt1 is None:
        # Si alguna es nula, entonces es válida la combinación.
        return True
    if opt1 == opt2:
        # No se puede repetir la misma opción dos veces
        return False
    elif opt1 == "n" or opt2 == "n":
        # La opción de normalizar no es compatible con otras opciones
        return False
    elif opt1 == "generate" or opt2 == "generate":
        # La opción de generar no es compatible con otras opciones
        return False
    else:
        return True

def comando_valido(comando: list[str]) -> bool:
    """
    Determina si el comando dado es válido.
    :param comando: Cadena de texto del comando
    :return: Si es válido o no
    """
    opciones = re.findall(_ER_COMANDO, " ".join(comando))

    for i, opcion in enumerate(opciones):
        desglose = opcion.split()
        # Ejemplo de desglose: '-n', 'fichero.txt'
        comando_extraido = desglose.pop(0)
        if comando_extraido[1:] not in _OPCIONES_VALIDAS:
            # Si lo que acompaña al guión no es una opción reconocida, el comando no es válido
            return False

        indice_comando = comando.index(comando_extraido)
        desglose = []
        j = 1
        while j < len(comando) and not comando[indice_comando + j].startswith("-"):
            if j != 0: # No nos interesa el primer argumento, el cual es la opción
                desglose.append(comando[indice_comando + j])
            j += 1
        next_option = None
        if j < len(comando):
            next_option = comando[indice_comando + j][1:] # Escapamos el guión
            if not combinacion_valida(comando_extraido[1:], next_option):
                # Si la siguiente opción es incompatible con esta, entonces el comando no es válido.
                return False

        if len(desglose) not in _NUM_ARGUMENTOS[comando_extraido[1:]] and next_option is not None and len(desglose) + 1 != _NUM_ARGUMENTOS[comando_extraido[1:]][0]:
            return False
        elif len(desglose) not in _NUM_ARGUMENTOS[comando_extraido[1:]] and next_option is None:
            return False

    return True