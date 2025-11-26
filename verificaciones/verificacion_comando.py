import regex as re
opciones_validas = ('n', 'sphone', 'snif', 'stime', 'slocation', 'generate')
num_argumentos = {'n': [1,3], 'sphone':[2], 'snif':[2], 'stime':[2], 'slocation':[3], 'generate':[2]}

def comando_valido(comando):
    opciones = re.findall(r"(-\w+(?: +[\w.\p{L}]+)* *)", comando)
    for i, opcion in enumerate(opciones):
        desglose = opcion.split()
        # Ejemplo de desglose: '-n', 'fichero.txt'
        comando = desglose.pop(0)[1:]
        if comando not in opciones_validas:
            # Si lo que acompaña al guión no es una opción reconocida, el comando no es válido
            return False
        if (len(opciones) == 1 or len(opciones) - 1 == i) and len(desglose) not in num_argumentos[comando]:
            # Si el número de argumentos no cuadra con los que tienen que ser, el comando no es válido.
            # Si el comando es de varios filtros, esta comprobación solo se realiza para el último filtro (por el argumento del fichero)
            return False
        if len(opciones) - 1 != i and len(desglose) not in [n-1 for n in num_argumentos[comando]]:
            # Esta comprobación solo se realiza en comandos de varios filtros. Se comprueba si los argumentos de
            # la opción son exactamente los esperados menos uno (le quitamos el fichero). Si no, el comando no es válido
            return False
    return True

if __name__ == "__main__":
    # TESTING
    assert(comando_valido("-n fichero.txt"))
    assert(comando_valido("-sphone 234234 43124"))
    assert(comando_valido("-n fichero.txt e g -sphone 123 fi.txt"))
    assert(comando_valido("-n -") == False)