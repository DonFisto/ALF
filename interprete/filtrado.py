import input_formatting
import verificaciones.verificaciones_basicas
from clases.entrada import Entrada
from clases.tiempo import Tiempo
from clases.ubicacion import Ubicacion


def _get_filtered_data(comando: list[str]) -> list[Entrada]:
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