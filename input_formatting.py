import verificaciones_basicas as vb
import verificacion_fecha as vf
import verificacion_coordenadas as vc
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
        if not vb.nif_valido(lista[1]): valido = False
        if not vf.tiempo_valido(lista[2]): valido = False
        if not vc.coordenadas_validas(lista[3]): valido = False
        if not vb.descripcion_valida(lista[4]): valido = False
        if not vb.precio_valido(lista[5]): valido = False
        if valido:
            datos_correctos.append(lista)


    return datos_correctos
