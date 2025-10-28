import re


def tlf_valido(tlf):
    valido = re.fullmatch(r'(\+\d{2}|)\d{3} \d{3} \d{3}', tlf)
    return bool(valido)

def nif_valido(nif):
    valido = re.fullmatch(r'(\d{8})([A-Z])', nif)
    if not valido:
        return False
    digitos = valido.group(1)
    letra = valido.group(2)
    valido = bool(letra == letra_dni(digitos))
    return bool(valido)
def descripcion_valida(descripcion):
    return True
def precio_valido(precio):
    formato_valido = re.fullmatch(r'[1-9]\d*(.\d+|)($|€)', precio)
    return bool(formato_valido)

def letra_dni(numero_dni):
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    valido = False
    index = 0
    while(not valido):
        try:
            index = int(numero_dni) % 23
            valido = True;
        except ValueError:

            print("introduce un valor numerico")
    return letras_dni[index]
