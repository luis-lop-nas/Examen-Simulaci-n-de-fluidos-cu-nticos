"""
Módulo de operadores cuánticos.
Define la clase OperadorCuantico para representar matrices unitarias
y aplicarlas a estados cuánticos.
"""

import numpy as np
from src.estado_cuantico import EstadoCuantico

class OperadorCuantico:
    """Representa un operador cuántico (matriz unitaria) aplicable a estados."""

    def __init__(self, nombre: str, matriz: list):
        """
        Inicializa el operador.
        :param nombre: Identificador del operador (ej. 'X', 'H').
        :param matriz: Matriz unitaria como lista de listas de números.
        """
        self.nombre = nombre
        # Convertimos la matriz a numpy.ndarray de tipo complejo para cálculos eficaces
        self.matriz = np.array(matriz, dtype=complex)

    def aplicar(self, estado: EstadoCuantico) -> EstadoCuantico:
        """
        Aplica este operador a un EstadoCuantico dado.
        :param estado: Instancia de EstadoCuantico a transformar.
        :return: Nuevo EstadoCuantico con vector transformado y nuevo id.
        """
        # Comprobamos que la matriz es cuadrada
        if self.matriz.shape[0] != self.matriz.shape[1]:
            raise ValueError("La matriz del operador no es cuadrada.")
        # Comprobamos que la dimensión del operador coincide con la del estado
        if self.matriz.shape[1] != len(estado.vector):
            raise ValueError(f"Dimensiones incompatibles: el operador espera vectores de tamaño {self.matriz.shape[1]}, pero el estado tiene tamaño {len(estado.vector)}.")
        # Multiplicación matriz-vector para obtener el nuevo vector de amplitudes
        nuevo_vector = np.dot(self.matriz, np.array(estado.vector, dtype=complex))
        # Generamos un identificador descriptivo para el nuevo estado
        nuevo_id = f"{estado.id}_{self.nombre}"
        # Devolvemos una nueva instancia de EstadoCuantico con el vector resultante
        return EstadoCuantico(nuevo_id, nuevo_vector.tolist(), estado.base)