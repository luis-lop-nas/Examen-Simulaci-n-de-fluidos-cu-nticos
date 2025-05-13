

"""Pruebas unitarias para la clase OperadorCuantico, incluyendo transformación de estados y validaciones."""
import unittest
from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico

# Agrupa pruebas para la clase OperadorCuantico
class TestOperadorCuantico(unittest.TestCase):

    # Verificar aplicación de la puerta X a |0> → |1>
    def test_aplicar_puerta_x(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        X = OperadorCuantico("X", [[0, 1], [1, 0]])
        resultado = X.aplicar(estado)
        self.assertAlmostEqual(resultado.vector[0], 0.0)
        self.assertAlmostEqual(resultado.vector[1], 1.0)
        self.assertEqual(resultado.id, "q0_X")

    # Verificar aplicación de la puerta Hadamard a |0> → superposición
    def test_aplicar_hadamard(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        H = OperadorCuantico("H", [[0.70710678, 0.70710678],
                                   [0.70710678, -0.70710678]])
        resultado = H.aplicar(estado)
        self.assertAlmostEqual(resultado.vector[0], 0.70710678, places=5)
        self.assertAlmostEqual(resultado.vector[1], 0.70710678, places=5)

    # Verificar que al aplicar un operador de dimensión incorrecta se lance ValueError
    def test_dimension_incompatible(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        operador = OperadorCuantico("M", [[1, 0, 0], [0, 1, 0]])
        with self.assertRaises(ValueError):
            operador.aplicar(estado)

if __name__ == "__main__":
    unittest.main()