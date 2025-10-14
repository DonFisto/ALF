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
    anio = ""
    for i in range(4): anio += str(rn.randint(0,9))
    if int(anio) == 0: anio = "0001"
    mes = str(rn.randint(1,12))
    if int(mes) < 10: mes = "0" + mes
    dia = ""
    if int(mes) in {1,3,5,7,8,10,12}:
        dia += str(rn.randint(1,31))
    elif not mes == 2:
        dia += str(rn.randint(1, 30))
    else:
        if vf.bisiesto(int(anio)):
            dia += str(rn.randint(1, 29))
        else:
            dia += str(rn.randint(1, 28))



