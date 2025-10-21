import random as rn
import verificaciones.verificacion_fecha as vf
def genera_tlf():
    numero = ""
    if rn.randint(0, 1):
       numero += "+" + str(rn.randint(1, 99))
    for i in range(9):
        numero += str(rn.randint(0, 9))
    return numero

def genera_nif():
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    nif = ""
    for i in range(8):
        nif += str(rn.randint(0, 9))
    idx = int(nif) % 23
    nif += letras_dni[idx]
    return nif

def genera_fecha(formato = 1):
    output = " "
    anio = rn.randint(1,9999)
    mes = rn.randint(1,12)
    if mes in {1,3,5,7,8,10,12}:
        dia = rn.randint(1,31)
    elif not mes == 2:
        dia = rn.randint(1, 30)
    else:
        if vf.bisiesto(int(anio)):
            dia = rn.randint(1, 29)
        else:
            dia = rn.randint(1, 28)
    hora = rn.randint(0,23)
    minuto = rn.randint(0,59)
    segundo = rn.randint(0,59)
    if formato == 1:
        anio_str = ""
        i = 10
        for j in range(4):
            anio_str = str(int((anio % i - anio % (i/10))/(i/10))) + anio_str
            i = i*10
        mes_str = str(mes)
        if mes < 10: mes_str = "0" + mes_str
        dia_str = str(dia)
        if dia < 10: dia_str = "0" + dia_str
        hora_str = str(hora)
        if hora < 10: hora_str = "0" + hora_str
        minuto_str = str(minuto)
        if minuto < 10: minuto_str = "0" + minuto_str
        
        output = output + anio_str + "-" + mes_str + "-" + dia_str + " " + hora_str + ":" + minuto_str
    #TODO Formato 2
    elif formato == 2:
        anio_str = str(anio)

        mes_str = vf.numero_a_mes(mes)
        dia_str = str(dia)
        if hora < 12:
            hora_str = str(hora)
            ext = "AM"
        else:
            hora_str = str(hora - 12)
            ext = "PM"
        minuto_str = str(minuto)
        if minuto < 10: minuto_str = "0" + minuto_str

        output = mes_str + " " + dia_str + ", " + anio_str + " " + hora_str + ":" + minuto_str + " " + ext
    #TODO Formato 3
    elif formato == 3:
        anio_str = ""
        i = 10
        for j in range(4):
            anio_str = str(int((anio % i - anio % (i / 10)) / (i / 10))) + anio_str
            i = i * 10
        mes_str = str(mes)
        if mes < 10: mes_str = "0" + mes_str
        dia_str = str(dia)
        if int(dia) < 10: dia_str = "0" + dia_str
        hora_str = str(hora)
        if hora < 10: hora_str = "0" + hora_str
        minuto_str = str(minuto)
        if minuto < 10: minuto_str = "0" + minuto_str
        segundo_str = str(segundo)
        if segundo < 10: segundo_str = "0" + segundo_str


        output = hora_str + ":" + minuto_str + ":" + segundo_str + " " + dia_str + "\\" + mes_str + "\\" + anio_str
    print (output)
    return output
#TODO generar coordenadas
def genera_coordenadas(formato = 1):
    latitud = rn.random()*180.0 - 90.0
