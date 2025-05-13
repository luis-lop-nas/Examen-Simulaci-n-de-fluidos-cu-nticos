"""Pruebas unitarias para la clase EstadoCuantico, verificando creación, medición y representación."""

import unittest
from src.estado_cuantico import EstadoCuantico

# Agrupa pruebas para la clase EstadoCuantico
class TestEstadoCuantico(unittest.TestCase):

    # Verificar atributos al crear un estado
    def test_creacion_estado(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        self.assertEqual(estado.id, "q0")
        self.assertEqual(estado.vector, [1, 0])
        self.assertEqual(estado.base, "computacional")

    # Verificar medición de un estado base puro
    def test_medicion_estado_base(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        probabilidades = estado.medir()
        self.assertAlmostEqual(probabilidades[0], 1.0)
        self.assertAlmostEqual(probabilidades[1], 0.0)

    # Verificar medición de un estado en superposición
    def test_medicion_superposicion(self):
        estado = EstadoCuantico("plus", [0.70710678, 0.70710678], "computacional")
        probabilidades = estado.medir()
        self.assertAlmostEqual(probabilidades[0], 0.5, places=2)
        self.assertAlmostEqual(probabilidades[1], 0.5, places=2)

    # Asegurar que un vector vacío genera excepción
    def test_vector_vacio(self):
        with self.assertRaises(ValueError):
            EstadoCuantico("vac", [], "computacional")

    # Comprobar representación en cadena
    def test_str(self):
        estado = EstadoCuantico("q0", [1, 0], "computacional")
        self.assertIn("q0", str(estado))
        self.assertIn("vector=[1, 0]", str(estado))
        self.assertIn("computacional", str(estado))

if __name__ == "__main__":
    unittest.main()