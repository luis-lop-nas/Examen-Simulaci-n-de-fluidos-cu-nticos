
import unittest
from src.estado_cuantico import EstadoCuantico
from src.operador_cuantico import OperadorCuantico

class TestOperadorCuantico(unittest.TestCase):

    def test_aplicar_puerta_x(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        X = OperadorCuantico("X", [[0, 1], [1, 0]])
        resultado = X.aplicar(estado)
        self.assertAlmostEqual(resultado.vector[0], 0.0)
        self.assertAlmostEqual(resultado.vector[1], 1.0)
        self.assertEqual(resultado.id, "q0_X")

    def test_aplicar_hadamard(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        H = OperadorCuantico("H", [[0.70710678, 0.70710678],
                                   [0.70710678, -0.70710678]])
        resultado = H.aplicar(estado)
        self.assertAlmostEqual(resultado.vector[0], 0.70710678, places=5)
        self.assertAlmostEqual(resultado.vector[1], 0.70710678, places=5)

    def test_dimension_incompatible(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        operador = OperadorCuantico("M", [[1, 0, 0], [0, 1, 0]])
        with self.assertRaises(ValueError):
            operador.aplicar(estado)

if __name__ == "__main__":
    unittest.main()