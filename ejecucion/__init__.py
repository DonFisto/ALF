"""
Paquete con el código del flujo de ejecución del programa:

- Códigos de salida para errores
- Lectura de archivos de entrada
- Flujo normal del programa
- Normalización de entradas de datos (-n)
- Generador de entradas aleatorias (-generate)
- Filtrado de entradas de datos (-sphone, -snif, -stime, -slocation...)
"""
from .control_errores import *
from .interprete import interpretar_comando
