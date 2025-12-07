import re

# Expresión regular para validar el teléfono español
_TLF_ES = r'\d{3}\s*\d{3}\s*\d{3}'
# Expresión regular para validar el teléfono internacional
_TLF_IN = r'\+(?:\d\s?){10,15}'
# Expresión regular para validar el DNI/NIE
_NIF_NIE = r'(\d{8}|[XYZ]\d{7})([A-Z])'
# Expresión regular para validar el precio
_PRECIO = r'(0|[1-9]\d*)(\.\d+|)(\$|€)'


def tlf_valido(tlf):
    """
    Determina si un teléfono está en un formato válido. Estos son:
    - Tres grupos de tres dígitos separados cada uno por un espacio (teléfono español)
    - Un '+' seguido de entre 10 y 15 dígitos separados indiferentemente.
    :param tlf: Cadena del teléfono
    :return: Si es válido o no
    """
    # Formato español
    valido = re.fullmatch(_TLF_ES, tlf)
    if not valido:
        # Formato internacional
        valido = re.fullmatch(_TLF_IN, tlf)
    return bool(valido)


def nif_valido(nif):
    """
    Determina si un NIF (o NIE) es válido.
    - Si es NIF, deben ser ocho dígitos seguidos de una letra válida.
    - Si es NIE, debe ser una letra en {X,Y,Z}, siete dígitos seguidos y una letra válida.
    Además, en ambos casos, la letra de confirmación debe ser correcta. Véase `letra_dni`.
    :param nif: NIF o NIE a comprobar
    :return: Si es válido su formato o no
    """
    valido = re.fullmatch(_NIF_NIE, nif)
    if not valido:
        return False
    digitos = valido.group(1)
    letra = valido.group(2)
    valido = bool(letra == _letra_dni(digitos))
    return bool(valido)


def descripcion_valida(descripcion):
    """
    Determina si la descripción es válida.
    :param descripcion: Descripción a comprobar
    :return: Si es válido su formato o no.
    """
    return True # La función, a pesar de ser inútil, existe para poder agregar restricciones a las descripciones de forma fácil


def precio_valido(precio):
    """
    Determina si un precio tiene un formato válido. Este debe cumplir:
    - No debe tener ceros a la izquierda.
    - No debe tener cifras decimales, si la parte decimal es nula.
    - Debe acabar en '$' o '€'
    :param precio: Precio a comprobar.
    :return: Si es válido su formato o no.
    """
    formato_valido = re.fullmatch(_PRECIO, precio)
    return bool(formato_valido)


def _letra_dni(numero_dni):
    """
    Calcula la letra del DNI o NIE. En caso de ser NIE, se realizará la asignación de la letra inicial:
    - X -> 0
    - Y -> 1
    - Z -> 2
    :param numero_dni: DNI o NIE, sin la última letra.
    :return: La letra correcta del DNI o NIE.
    """
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    valido = False
    index = 0
    if numero_dni[0] == 'X':
        numero_dni = "0" + numero_dni[1:]
    elif numero_dni[0] == 'Y':
        numero_dni = "1" + numero_dni[1:]
    elif numero_dni[0] == 'Z':
        numero_dni = "2" + numero_dni[1:]

    while not valido:
        try:
            index = int(numero_dni) % 23
            valido = True
        except ValueError:
            print("introduce un valor numerico")
    return letras_dni[index]
