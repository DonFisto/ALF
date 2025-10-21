class Ubicacion:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud
    def formato(self, f = 1):
        raise NotImplementedError("No implementado")

    def get_latitud(self):
        return self.latitud
    def get_longitud(self):
        return self.longitud