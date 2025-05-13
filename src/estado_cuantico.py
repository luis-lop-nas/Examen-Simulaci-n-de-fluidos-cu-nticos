

from typing import List, Union
import math

class EstadoCuantico:
    def __init__(self, identificador: str, vector: List[Union[float, complex]], base: str):
        if not vector:
            raise ValueError("El vector de estado no puede estar vacío.")
        self.id = identificador
        self.vector = vector
        self.base = base

    def medir(self) -> List[float]:
        """Devuelve las probabilidades de cada estado base al medir."""
        probabilidades = [abs(amplitud)**2 for amplitud in self.vector]
        suma = sum(probabilidades)
        # Normalizamos si hay pequeñas desviaciones numéricas
        return [p / suma for p in probabilidades]

    def __str__(self):
        return f"{self.id}: vector={self.vector} en base {self.base}"