import regex as re

# Mapa que asigna a cada opción el número de argumentos que debe tener.
_NUM_ARGUMENTOS = {'n': [1, 3], 'sphone': [2], 'snif': [2], 'stime': [2], 'slocation': [3], 'generate': [2]}
# Array con las opciones válidas para el comando
_OPCIONES_VALIDAS = _NUM_ARGUMENTOS.keys()
# Expresión regular para validar el comando
_ER_COMANDO = R"(-\w+(?: +.+)* *)"


def comando_valido(comando: str) -> bool:
    """
    Determina si el comando dado es válido.
    :param comando: Cadena de texto del comando
    :return: Si es válido o no
    """
    opciones = re.findall(_ER_COMANDO, comando)
    for i, opcion in enumerate(opciones):
        desglose = opcion.split()
        # Ejemplo de desglose: '-n', 'fichero.txt'
        # TODO: Hacer expresiones regulares para la captura de -slocation, -stime, -sphone correctamente
        comando = desglose.pop(0)[1:]
        if comando not in _OPCIONES_VALIDAS:
            # Si lo que acompaña al guión no es una opción reconocida, el comando no es válido
            return False
        if (len(opciones) == 1 or len(opciones) - 1 == i) and len(desglose) not in _NUM_ARGUMENTOS[comando]:
            # Si el número de argumentos no cuadra con los que tienen que ser, el comando no es válido.
            # Si el comando es de varios filtros, esta comprobación solo se realiza para el último filtro (por el argumento del fichero)
            return False
        if len(opciones) - 1 != i and len(desglose) not in [n - 1 for n in _NUM_ARGUMENTOS[comando]]:
            # Esta comprobación solo se realiza en comandos de varios filtros. Se comprueba si los argumentos de
            # la opción son exactamente los esperados menos uno (le quitamos el fichero). Si no, el comando no es válido
            return False
    return True
