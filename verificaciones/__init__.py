"""
Paquete con la verificación de comando, y todos los atributos de entrada a excepción de Ubicación y Tiempo.
"""
from .verificacion_comando import comando_valido
from .verificaciones_basicas import tlf_valido, nif_valido, precio_valido, descripcion_valida
