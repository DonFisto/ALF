from interprete.normalizacion import imprimir_normalizado


def interpretar_comando(comando):
    if comando[0] == "-n":
        #NORMALIZAR
        input_file = comando[1]
        file = open(input_file, 'r', encoding='utf-8')
        if len(comando) == 4:
            f1 = comando[2]
            f2 = comando[3]
            imprimir_normalizado(file, f1, f2)
        else:
            imprimir_normalizado(file)
    elif comando[0] == "-sphone":
        raise NotImplementedError
        #FILTRO POR TELÉFONO
    elif comando[0] == "-snif":
        raise NotImplementedError
        #FILTRO POR NIF
    elif comando[0] == "-stime":
        raise NotImplementedError
        #FILTRO POR HORA
    elif comando[0] == "-slocation":
        raise NotImplementedError
        #FILTRO POR LUGAR