

import numpy as np
from src.estado_cuantico import EstadoCuantico

class OperadorCuantico:
    def __init__(self, nombre: str, matriz: list):
        self.nombre = nombre
        self.matriz = np.array(matriz, dtype=complex)

    def aplicar(self, estado: EstadoCuantico) -> EstadoCuantico:
        if len(self.matriz) != len(estado.vector):
            raise ValueError("Dimensiones incompatibles entre operador y estado.")
        nuevo_vector = np.dot(self.matriz, np.array(estado.vector, dtype=complex))
        nuevo_id = f"{estado.id}_{self.nombre}"
        return EstadoCuantico(nuevo_id, nuevo_vector.tolist(), estado.base)