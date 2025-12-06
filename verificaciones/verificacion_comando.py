import regex as re

# Mapa que asigna a cada opción el número de argumentos que debe tener.
_NUM_ARGUMENTOS = {'n': [1, 3], 'sphone': [2], 'snif': [2], 'stime': [2], 'slocation': [3], 'generate': [2]}
# Array con las opciones válidas para el comando
_OPCIONES_VALIDAS = _NUM_ARGUMENTOS.keys()
# Expresión regular para validar el comando
_ER_COMANDO = R"(-\w+(?: +.+)* *)"
_ER_SPHONE = R"-sphone (\d{3}\s*\d{3}\s*\d{3}|\+(?:\d\s?){10,15})"
_ER_SNIF = R"-snif ((\d{8}|[XYZ]\d{7})([A-Z]))"
_ER_STIME = R"-stime ((\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2})|(?i)(january|february|march|april|may|june|july|august|september|october|november|december) (\d{1,2}), (\d{1,4}) (\d{1,2}):(\d{2}) (am|pm)|(\d{2}):(\d{2}):(\d{2}) (\d{2})/(\d{2})/(\d{4}))"
_ER_SLOCATION = R"-slocation (([-+]?(?:90|[0-8]\d|\d)\.\d+)\s*,\s*([-+]?(?:180|1[0-7]\d|\d{1,2})\.\d+)|(\d|90|[0-8]\d)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(N|S)\s*,\s*(\d{1,2}|[1][0-7]\d|180)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(W|E)|0([0-8]\d|90)([0-5]\d)(\d?\d.\d{4})(N|S)(0\d{1,2}|1[0-7]\d|180)([0-5]\d)(\d?\d.\d{4})(W|E)) (([-+]?(?:90|[0-8]\d|\d)\.\d+)\s*,\s*([-+]?(?:180|1[0-7]\d|\d{1,2})\.\d+)|(\d|90|[0-8]\d)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(N|S)\s*,\s*(\d{1,2}|[1][0-7]\d|180)°\s*(\d|[0-5]\d)\'\s*((?:\d|[0-5]\d).\d{4})\"\s*(W|E)|0([0-8]\d|90)([0-5]\d)(\d?\d.\d{4})(N|S)(0\d{1,2}|1[0-7]\d|180)([0-5]\d)(\d?\d.\d{4})(W|E))"


def comando_valido(comando: str) -> bool:
    """
    Determina si el comando dado es válido.
    :param comando: Cadena de texto del comando
    :return: Si es válido o no
    """
    opciones = re.findall(_ER_COMANDO, comando)
    valido = True
    i = 0
    while i < len(opciones) and valido:
        opcion = opciones[i]
        desglose = opcion.split()
        # Ejemplo de desglose: '-n', 'fichero.txt'
        # TODO: Hacer expresiones regulares para la captura de -slocation, -stime, -sphone correctamente
        comando_op = desglose.pop(0)[1:]
        # Si lo que acompaña al guión no es una opción reconocida, el comando no es válido
        if comando_op not in _OPCIONES_VALIDAS:
            valido = False
        # Si el número de argumentos no cuadra con los que tienen que ser, el comando no es válido.
        # Si el comando es de varios filtros, esta comprobación solo se realiza para el último filtro (por el argumento del fichero)
        elif (len(opciones) == 1 or len(opciones) - 1 == i) and len(desglose) not in _NUM_ARGUMENTOS[comando_op]:
            valido = False
        # Esta comprobación solo se realiza en comandos de varios filtros. Se comprueba si los argumentos de
        # la opción son exactamente los esperados menos uno (le quitamos el fichero). Si no, el comando no es válido
        elif len(opciones) - 1 != i and len(desglose) not in [n - 1 for n in _NUM_ARGUMENTOS[comando_op]]:
            valido = False
        i += 1
    return valido
