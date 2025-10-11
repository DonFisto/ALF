import re


def tlf_valido(tlf):
    valido = re.fullmatch(r'(\+\d{2}|)\d{9}', tlf)
    return bool(valido)

def nif_valido(nif):
    formato_valido = re.fullmatch(r'(\d{8})(\p{Lu})', nif)
    correcto = False
    if formato_valido:
        m = re.search(r'(\d{8})(\p{Lu})', nif)
        correspondencia = "TRWAGMYFPDXBNJZSQVHLCKE"
        digitos = m.group(1)
        letra = m.group(2)
        idx = digitos % 23
        correcto = (letra == correspondencia[idx])
    return (bool(formato_valido) and correcto)