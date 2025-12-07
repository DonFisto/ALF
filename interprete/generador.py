import random as rn
from random import randint

from clases.tiempo import Tiempo
from clases.ubicacion import Ubicacion
DICCIONARIOS = {
    "producto": [
        "auricular inalámbrico", "altavoz portátil", "ratón óptico", "teclado mecánico", "monitor LED", "pantalla 4K", "cámara digital", "cámara web HD",
        "lámpara de escritorio", "lámpara LED regulable", "micrófono USB", "tableta gráfica", "impresora multifunción", "escáner portátil",
        "disco duro externo", "SSD portátil", "router Wi-Fi", "amplificador de señal", "cargador rápido", "power bank", "cable USB-C", "cable HDMI", "hub USB-C",
        "lector de tarjetas", "mini proyector", "barra de sonido", "subwoofer compacto", "smartwatch", "pulsera de actividad", "móvil Android", "smartphone compacto",
        "tablet ultraligera", "ordenador portátil", "mini PC", "sistema de refrigeración", "ventilador USB", "silla ergonómica", "alfombrilla gamer", "altavoz inteligente",
        "adaptador Bluetooth", "teclado inalámbrico", "stylus digital", "monitor curvo", "enrutador gigabit", "tarjeta de red", "disco NVMe",
        "carcasa externa", "webcam 4K", "trípode ajustable", "foco LED", "soporte para monitor", "soporte de móvil", "soporte de portátil",
        "barra estabilizadora", "grabadora digital", "dispositivo GPS", "monitor portátil", "capturadora de vídeo", "dron compacto",
        "cámara deportiva", "robot aspirador", "humidificador", "purificador de aire", "cafetera automática", "batidora eléctrica", "tostadora inteligente",
        "freidora de aire", "sartén antiadherente", "cacerola de acero", "juego de cuchillos", "set de herramientas", "taladro eléctrico",
        "linterna LED", "estación meteorológica", "reloj digital", "calentador portátil", "secador de pelo", "plancha de vapor",
        "maquinilla eléctrica", "altavoz de escritorio", "antena Wi-Fi", "adaptador de corriente", "convertidor USB-Ethernet", "panel solar portátil",
        "kit de iluminación", "sistema de alarma", "cerradura inteligente", "termostato digital", "báscula inteligente", "medidor láser",
        "estuche rígido", "mochila técnica", "maletín acolchado", "organizador de cables", "cuaderno digital", "protector de pantalla",
        "soporte plegable", "micrófono lavalier", "dispositivo NFC"
    ],
    "adjetivo": [
        "compacto", "resistente", "ergonómico", "potente", "ligero", "innovador", "duradero", "silencioso", "eficiente", "moderno", "cómodo", "inteligente",
        "rápido", "preciso", "fiable", "versátil", "avanzado", "elegante", "minimalista", "sofisticado", "robusto", "portátil", "amplio", "ultraligero",
        "intuitivo", "reducido", "compacto", "sólido", "estético", "premium", "profesional", "estable", "equilibrado", "potenciado", "optimizado",
        "silencioso", "regulable", "adaptable", "ajustable", "mejorado", "reforzado", "preciso", "rápido", "eficaz", "confiable", "actual",
        "ergonómico", "luminoso", "sofisticado", "exclusivo", "cómodo", "aventajado", "amplificado", "flexible", "modular", "de alta gama",
        "resistente al desgaste", "de bajo consumo", "de diseño limpio", "de estilo elegante", "compacto y ligero", "económico", "equilibrado y firme",
        "silencioso y estable", "altamente eficiente", "tecnológico", "discreto", "ligero y resistente", "compacto y potente", "protegido",
        "acolchado", "amortiguado", "refinado", "adaptativo", "automatizado", "mejorado en prestaciones", "pulido", "estilizado", "controlado",
        "optimizado en eficiencia", "sofisticado en diseño", "de gran precisión", "ultra resistente", "ultra silencioso", "extra ligero", "extra potente",
        "premium y elegante", "de rendimiento avanzado", "estabilizado", "anticorrosión", "hipoalergénico", "antideslizante", "clásico",
        "minimalista funcional", "robusto y fiable", "fiable y versátil", "potente y silencioso", "de perfil delgado", "compacto reforzado"
    ],
    "caracteristica": [
        "con conectividad Bluetooth", "con batería de larga duración", "con carga rápida", "compatible con múltiples dispositivos",
        "con pantalla iluminada", "con sensores avanzados", "con estructura reforzada", "con acabado profesional",
        "con iluminación regulable", "con sistema de reducción de ruido", "con memoria ampliable", "con protección contra caídas",
        "con certificación energética", "con interfaz intuitiva", "con controles táctiles", "con conectores universales",
        "con Wi-Fi de alta velocidad", "con sistema antivibración", "con diseño plegable", "con superficie antideslizante",
        "con calibración automática", "con filtros intercambiables", "con garantía extendida", "con soporte magnético",
        "con resistencia al agua", "con materiales reciclados", "con modo silencioso", "con función de ahorro energético",
        "con conexión rápida USB-C", "con sistema térmico avanzado", "con modo de alta precisión", "con motor optimizado",
        "con sensores inteligentes", "con soporte ergonómico", "con amplificación mejorada", "con protección UV",
        "con estructura ligera", "con carcasa reforzada", "con ventilación optimizada", "con cable trenzado",
        "con indicadores LED", "con sincronización automática", "con resistencia reforzada", "con materiales premium",
        "con antena integrada", "con sistema de bloqueo seguro", "con memoria integrada", "con botón multifunción",
        "con ajuste de intensidad", "con control remoto", "con base estable", "con tecnología de bajo ruido",
        "con motor silencioso", "con sensor de proximidad", "con recubrimiento antiarañazos", "con doble aislamiento",
        "con disipación eficiente", "con control por voz", "con sellado hermético", "con pantalla táctil",
        "con modo inteligente", "con soporte universal", "con estructura metálica", "con acoplamiento rápido",
        "con recambio incluido", "con cable reforzado", "con precisión milimétrica", "con adaptador incorporado",
        "con conexión inalámbrica estable", "con sistema de anclaje rápido", "con soporte articulado", "con tecnología avanzada",
        "con acabado mate", "con alta sensibilidad", "con acento premium", "con mando integrado",
        "con apagado automático", "con doble función", "con batería intercambiable", "con modo automático",
        "con sensor de iluminación", "con diseño ultracompacto", "con protección adicional", "con materiales de larga duración",
        "con optimización energética", "con sistema antihuellas", "con equilibrio térmico", "con filtros protectores",
        "con software actualizado", "con carcasa resistente", "con montaje rápido", "con rendimiento estable",
        "con cable desmontable", "con tecnología silenciosa", "con componentes de precisión", "con sistema modular"
    ],
    "uso": [
        "pensado para uso profesional", "adecuado para oficinas", "recomendado para viajes", "excelente para tareas diarias",
        "útil en espacios reducidos", "diseñado para actividades creativas", "apto para gamers", "orientado a usuarios avanzados",
        "perfecto para principiantes", "recomendado para fotografía", "ideal para reuniones online", "útil para presentaciones",
        "adecuado para largas sesiones de trabajo", "estable en exteriores", "pensado para uso intensivo", "recomendado para teletrabajo",
        "perfecto para estudiantes universitarios", "útil en laboratorios", "ideal para edición de vídeo", "perfecto para streaming",
        "apto para tareas multitarea", "útil en estudios musicales", "recomendado para educación a distancia", "pensado para movilidad",
        "adecuado para transporte diario", "ideal para entornos industriales", "útil en espacios compartidos", "perfecto para oficinas abiertas",
        "pensado para entornos fríos", "recomendado para viajes largos", "ideal para usuarios exigentes", "adecuado para rutinas ligeras",
        "diseñado para alta precisión", "perfecto para fotografía móvil", "útil para edición de audio", "recomendado para gaming portátil",
        "ideal para freelancers", "adecuado para estudios creativos", "pensado para máxima comodidad", "útil en talleres",
        "perfecto para transporte seguro", "ideal para videollamadas", "apto para sesiones de grabación", "pensado para productividad",
        "útil en proyectos educativos", "ideal para usuarios técnicos", "perfecto para aprender nuevas habilidades", "recomendado para principiantes",
        "adecuado para cursos online", "pensado para mejorar la productividad", "ideal para trabajo colaborativo", "útil en espacios profesionales",
        "adecuado para entornos exigentes", "recomendado para pequeños negocios", "perfecto para trabajo híbrido", "diseñado para usuarios móviles",
        "ideal para transporte diario", "útil para creadores de contenido", "recomendado para diseñadores", "adecuado para ingenieros",
        "perfecto para programadores", "ideal para editores", "pensado para largas jornadas", "útil en conferencias",
        "adecuado para reuniones frecuentes", "ideal para trabajo remoto", "perfecto para uso prolongado", "recomendado para trabajo creativo",
        "ideal para estudiantes de tecnología", "útil para docentes", "adecuado para aulas digitales", "perfecto para salas de estudio",
        "recomendado para uso doméstico", "ideal para familias", "útil en viajes cortos", "adecuado para mochilas pequeñas",
        "pensado para usuarios activos", "perfecto para desplazamientos diarios", "ideal para quienes buscan comodidad", "recomendado para viajeros urbanos",
        "útil en espacios pequeños", "adecuado para escritorios", "pensado para un uso continuo", "ideal para optimizar rutinas",
        "perfecto para mejorar la productividad", "útil para responder mensajes", "adecuado para grabaciones", "recomendado para música",
        "perfecto para entornos silenciosos", "ideal para trabajo nocturno", "útil en situaciones de emergencia", "pensado para accesibilidad",
        "diseñado para máxima portabilidad", "apto para toda la familia", "ideal para quienes buscan versatilidad", "perfecto para cualquier rutina",
        "ideal para trabajar desde casa", "perfecto para estudiantes"
    ]

}


def genera_tlf():
    """
    Genera un número de teléfono aleatorio sea en formato español o internacional y lo devuelve como cadena de texto.
    :return: Número de telefono generado.
    """
    numero = ""
    if rn.randint(0, 1):
        #formato internacional
        numero = "+"
        for i in range(randint(10, 15)):
            numero += str(rn.randint(0, 9))
    else:
        #formato español
        for i in range(3):
            for _ in range(3):
                # Añadir tres números
                numero += str(rn.randint(0, 9))
            #Añadir espacio de separación, salvo si es el último.
            if i != 2:
                numero += " "
    return numero

def genera_nif():
    """
    Genera un nif/nie válido y lo devuelve como cadena de texto.
    :return: nif/nie generado.
    """
    #listas de letras validas para nie/dni
    letras_nie = "XYZ"
    letras_dni = "TRWAGMYFPDXBNJZSQVHLCKE"
    nif = ""
    #generación de 8 dígitos aleatorios
    for i in range(8):
        nif += str(rn.randint(0, 9))
    #asignación de la letra correcta
    idx = int(nif) % 23
    nif += letras_dni[idx]
    #si empieza por 0, 1 o 2 se determina de forma aleatoria si se convierte en nie
    if nif[0] in "012":
        extranjero_rnd = rn.randint(0,1)
        #en caso de ser nie, se cambia el primer dígito (0, 1, 2) por X, Y, Z respectivamente
        if extranjero_rnd:
            nif = letras_nie[int(nif[0])] + nif[1:]
    return nif

def genera_fecha(formato = 1):
    """
    Genera una fecha válida y la devuelve como cadena de texto con el formato indicado.
    :param formato: valor entero entre 1 y 3 que toma por defecto el valor 1 e indica el formato con el que se devuelve la fecha generada
    :return: fecha generada expresada en el formato indicado.
    """
    anio = rn.randint(1,9999)
    mes = rn.randint(1,12)
    if mes in {1,3,5,7,8,10,12}:
        dia = rn.randint(1,31)
    elif mes != 2:
        dia = rn.randint(1, 30)
    else:
        if Tiempo.bisiesto(int(anio)):
            dia = rn.randint(1, 29)
        else:
            dia = rn.randint(1, 28)
    hora = rn.randint(0,23)
    minuto = rn.randint(0,59)
    segundo = rn.randint(0,59)
    tiempo = Tiempo(dia, mes, anio, hora, minuto, segundo)
    return tiempo.formatear(formato)

def genera_coordenadas(formato = 1):
    """
    Genera una ubicación válida y la devuelve como cadena de texto con el formato indicado.
    :param formato: valor entero entre 1 y 3 que toma por defecto el valor 1 e indica el formato con el que se devuelve la ubicación generada
    :return: ubicación generada en el formato indicado.
    """
    latitud = rn.random() * 180.0 - 90.0
    longitud = rn.random() * 360.0 - 180.0
    coordenadas = Ubicacion(latitud, longitud)
    return coordenadas.formatear(formato)

def genera_descripcion():
    """
    Genera una descripción tomando valores aleatorios de diccionarios de descripciones predefinidos y la devuelve como cadena de texto.
    :return: descripción generada.
    """
    producto = rn.choice(DICCIONARIOS["producto"])
    adjetivo = rn.choice(DICCIONARIOS["adjetivo"])
    caracteristica = rn.choice(DICCIONARIOS["caracteristica"])
    uso = rn.choice(DICCIONARIOS["uso"])
    return f"{producto} {adjetivo} {caracteristica}. {uso}."

def genera_precio():
    """
    Genera un precio aleatorio para un item en euros o en dolares y lo devuelve como cadena de texto.
    :return: precio generado.
    """
    precio = rn.random() * (10 ** (randint(0, 6))) # Número aleatorio en [0, 1), y corremos la coma un número aleatorio de posiciones
    euro_dolar = rn.randint(0, 1)
    min_decimales = rn.randint(1, 10)
    output = f"{precio:.{min_decimales}f}"
    if euro_dolar == 0:
        output += "€"
    else:
        output += "$"
    return output

def genera_espacios(max_espacios):
    """
    Genera un número aleatorio de espacios entre 1 y el máximo indicado y lo devuelve como cadena de texto.
    :param max_espacios: valor entero que indica el número máximo de espacios que se pueden generar
    :return: cadena de texto con tantos espacios en blanco como se hayan generado de forma aleatoria.
    """
    output = ""
    for i in range(rn.randint(1, max_espacios)):
        output += " "
    return output

def genera_linea():
    """
    Genera una linea aleatoria que consta de un número de telefono, un nif/nie, una fecha, una ubicación, una descripción y un precio y la devuelve como cadena de texto con los valores separados por ;
    :return: linea generada.
    """
    ffecha = rn.randint(1,3)
    fcoord = rn.randint(1, 3)
    output = genera_tlf() + ";" + genera_nif() + ";" + genera_fecha(ffecha) + ";" + genera_coordenadas(fcoord) + ";" + genera_descripcion() + ";" + genera_precio()
    return output


def genera_entrada(nombre_fichero, num_entradas):
    """
    Genera tantas lineas aleatorias como se indique y las almacena el archivo indicado.
    :param nombre_fichero: fichero en el que se almacena la entrada generada
    :param num_entradas: número de lineas en la entrada
    :return: no se devuelve ningún valor.
    """
    file = open(nombre_fichero, "w", encoding='utf-8')
    for i in range(num_entradas):
        file.write(genera_linea() + "\n")
    return

