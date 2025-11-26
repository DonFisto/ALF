import input_formatting
import verificaciones.verificaciones_basicas
from clases.entrada import Entrada
from clases.tiempo import Tiempo
from clases.ubicacion import Ubicacion
from interprete.normalizacion import imprimir_normalizado
from generador import genera_entrada


def interpretar_comando(comando: list[str]):
    """
    Interpreta los argumentos del comando dado (siempre correcto). Hay tres ramas excluyentes del comando:

    - Normalizar: -n <fichero> [<f1> <f2>]>
    - Generar: -generate <fichero> <num_entradas>
    - Filtrar (Se aceptan varios filtros): -sphone <telefono> <fichero> | -snif <NIF> <fichero> |-stime <desde> <hasta> <fichero> | -slocation <desde> <hasta> <fichero>

    :param comando: Array no vacío con las opciones del comando
    """
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
    elif comando[0] == "-generate":
        #GENERADOR
        fichero = comando[1]
        num_entradas = int(comando[2])
        genera_entrada(fichero, num_entradas)
        print("Entrada generada correctamente")
    else:
        # FILTROS
        try:
            data = get_filtered_data(comando)
            for entrada in data:
                print(entrada.get_line())
        except ValueError as e:
            print(e)


def get_filtered_data(comando: list[str]) -> list[Entrada]:
    """
    Obtiene los datos del fichero especificado en el último argumento del comando, y aplica los filtros especificados en el resto.
    :param comando: Lista con los argumentos del comando
    :return: Datos con los filtros aplicados
    :raise ValueError: Si alguno de los campos de los filtros no es correcto, o si la propia lista de comandos está mal estricturada.
    """
    # El último argumento es siempre el fichero
    lines = ""
    with open(comando.pop(), 'r', encoding='utf-8') as file:
        lines = file.readlines()

    data = input_formatting.leer_datos(lines)
    while len(comando) > 0:
        if comando[0] == "-sphone":
            telefono = comando[1]

            if not verificaciones.verificaciones_basicas.tlf_valido(telefono):
                raise ValueError("Teléfono especificado en el filtro -sphone no válido")

            data = [d for d in data if d.get_tlf() == telefono]
            comando = comando[2:]

        elif comando[0] == "-snif":
            nif = comando[1]

            if not verificaciones.verificaciones_basicas.nif_valido(nif):
                raise ValueError("NIF especificado en el filtro -snif no válido")

            data = [d for d in data if d.get_nif() == nif]
            comando = comando[2:]
        elif comando[0] == "-stime":
            try:
                desde = Tiempo.from_string(comando[1])
                hasta = Tiempo.from_string(comando[2])
                # Filtramos usando la relación de orden definida en la clase Tiempo
                data = [d for d in data if d.get_fecha() <= hasta and d.get_fecha() >= desde]
                comando = comando[3:]
            except ValueError:
                raise ValueError("Alguna marca temporal especificada en el filtro -stime no fue válida")
        elif comando[0] == "-slocation":
            try:
                desde = Ubicacion.from_string(comando[1])
                hasta = float(comando[2])
                # Filtramos usando la fórmula Haversine ya implementada en la clase Ubicacion
                data = [d for d in data if d.get_ubicacion().distancia_con(desde) <= hasta]
                comando = comando[3:]
            except ValueError:
                raise ValueError("La ubicación o la cota de kilómetros especificadas en el filtro -slocation no fueron válidas")
        else:
            raise ValueError("El array de comandos no es válida o no se gestionó de forma correcta")
    return data