import re

TLF_ES = r'\d{3} \d{3} \d{3}'
TLF_IN = r'\+(?:\d\s?){10,15}'
NIF_NIE = r'(\d{8}|[XYZ]\d{7})([A-Z])'
PRECIO = r'[1-9]\d*(.\d+|)($|€)'
def tlf_valido(tlf):
    """
    Determina si un teléfono está en un formato válido. Estos son:
    - Tres grupos de tres dígitos separados cada uno por un espacio (teléfono español)
    - Un '+' seguido de entre 10 y 15 dígitos separados indiferentemente.
    :param tlf: Cadena del teléfono
    :return: Si es válido o no
    """
    # Formato español
    valido = re.fullmatch(TLF_ES, tlf)
    if not valido:
        # Formato internacional
        valido = re.fullmatch(TLF_IN, tlf)
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
    valido = re.fullmatch(NIF_NIE, nif)
    if not valido:
        return False
    digitos = valido.group(1)
    letra = valido.group(2)
    valido = bool(letra == letra_dni(digitos))
    return bool(valido)
def descripcion_valida(descripcion):
    """
    Determina si la descripción es válida.
    :param descripcion: Descripción a comprobar
    :return: Si es válido su formato o no.
    """
    return True
def precio_valido(precio):
    """
    Determina si un precio tiene un formato válido. Este debe cumplir:
    - No debe tener ceros a la izquierda.
    - No debe tener cifras decimales, si la parte decimal es nula.
    - Debe acabar en '$' o '€'
    :param precio: Precio a comprobar.
    :return: Si es válido su formato o no.
    """
    formato_valido = re.fullmatch(PRECIO, precio)
    return bool(formato_valido)

def letra_dni(numero_dni):
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
        numero_dni[0] = 0
    elif numero_dni[0] == 'Y':
        numero_dni[0] = 1
    elif numero_dni[0] == 'Z':
        numero_dni[0] = 2

    while(not valido):
        try:
            index = int(numero_dni) % 23
            valido = True
        except ValueError:
            print("introduce un valor numerico")
    return letras_dni[index]
