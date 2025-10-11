import verificaciones_basicas as vb
def data_segregation(input_text):
    lines = input_text.readlines()
    clean_lines = []
    for line in lines:
        args = line.split(";")
        tlf = args[0].strip()
        nif = args[1].strip()
        date = args[2].strip()
        coords = args[3].strip()
        desc = args[4].strip()
        price = args[5].strip()
        clean_args = [tlf, nif, date, coords, desc, price]
        clean_lines.append(clean_args)
    return clean_lines

def verificacion_datos(datos):
    datos_correctos = []
    for lista in datos:
        valido = True
        if not vb.tlf_valido(lista[0]): valido = False


    return True
