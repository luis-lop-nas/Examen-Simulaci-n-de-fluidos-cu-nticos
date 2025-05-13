"""
Módulo de estados cuánticos.
Define la clase EstadoCuantico para modelar vectores de estado y cálculos de medición.
"""

from typing import List, Union
import math

class EstadoCuantico:
    """Representa un estado cuántico con amplitudes y base de medida."""
    def __init__(self, identificador: str, vector: List[Union[float, complex]], base: str):
        """
        Inicializa el estado cuántico.
        :param identificador: nombre único del estado.
        :param vector: lista de amplitudes (float o complex).
        :param base: nombre de la base de representación.
        """
        # Validación: el vector no puede estar vacío
        if not vector:
            raise ValueError("El vector de estado no puede estar vacío.")
        self.id = identificador
        self.vector = vector
        self.base = base

    def medir(self) -> List[float]:
        """
        Calcula la distribución de probabilidades de medir cada componente.
        :return: lista de probabilidades normalizadas.
        """
        # Probabilidad = |amplitud|^2
        probabilidades = [abs(amplitud)**2 for amplitud in self.vector]
        suma = sum(probabilidades)
        # Normalizar para corregir leves desvíos numéricos
        return [p / suma for p in probabilidades]

    def __str__(self):
        """Devuelve una representación legible del estado."""
        return f"{self.id}: vector={self.vector} en base {self.base}"