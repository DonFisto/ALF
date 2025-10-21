import regex as re
opciones_validas = ('n', 'sphone', 'snif', 'stime', 'slocation')
num_argumentos = {'n': [1,3], 'sphone':[2], 'snif':[2], 'stime':[3], 'slocation':[3]}
def comando_valido(comando):
    opciones = re.findall(r"(-\w+(?: +[\w.\p{L}]+)* *)", comando)
    for opcion in opciones:
        desglose = opcion.split()
        # Ejemplo de desglose: '-n', 'fichero.txt'
        comando = desglose.pop(0)[1:]
        if comando not in opciones_validas:
            return False
        if len(desglose) not in num_argumentos[comando]:
            return False
    return True

if __name__ == "__main__":
    # TESTING
    assert(comando_valido("-n fichero.txt"))
    assert(comando_valido("-sphone 234234 43124"))
    assert(comando_valido("-n fichero.txt e g -sphone 123 fi.txt"))
    assert(comando_valido("-n -") == False)