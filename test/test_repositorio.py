"""Pruebas unitarias para RepositorioDeEstados: alta, listado, operadores y medición."""
import unittest
from src.repositorio import RepositorioDeEstados
from src.operador_cuantico import OperadorCuantico

# Agrupa pruebas para la clase RepositorioDeEstados
class TestRepositorioDeEstados(unittest.TestCase):

    # Verificar que se agregan estados y se listan correctamente
    def test_agregar_y_listar_estados(self):
        self.repo.agregar_estado("q0", [1, 0], "computacional")
        self.repo.agregar_estado("q1", [0, 1], "computacional")
        estados = self.repo.listar_estados()
        self.assertEqual(len(estados), 2)
        self.assertTrue(any("q0" in e for e in estados))
        self.assertTrue(any("q1" in e for e in estados))

    # Verificar que no se puede agregar un estado con id duplicado
    def test_agregar_estado_duplicado(self):
        self.repo.agregar_estado("q0", [1, 0], "computacional")
        with self.assertRaises(ValueError):
            self.repo.agregar_estado("q0", [0.5, 0.5], "computacional")

    # Verificar que aplicar un operador crea el estado transformado
    def test_aplicar_operador(self):
        self.repo.agregar_estado("q0", [1, 0], "computacional")
        X = OperadorCuantico("X", [[0, 1], [1, 0]])
        self.repo.aplicar_operador("q0", X, "q0_X")
        self.assertIn("q0_X", self.repo.estados)
        resultado = self.repo.estados["q0_X"]
        self.assertAlmostEqual(resultado.vector[0], 0.0)
        self.assertAlmostEqual(resultado.vector[1], 1.0)

    # Verificar la medición de un estado base puro
    def test_medicion(self):
        self.repo.agregar_estado("q0", [1, 0], "computacional")
        probabilidades = self.repo.medir_estado("q0")
        self.assertAlmostEqual(probabilidades[0], 1.0)
        self.assertAlmostEqual(probabilidades[1], 0.0)

if __name__ == "__main__":
    unittest.main()