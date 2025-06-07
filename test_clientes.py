import unittest
import os
import json

from src import CodigoPyhton as gestion  # 👈 Asegúrate de que coincida con el nombre de tu archivo real

class TestGestionClientes(unittest.TestCase):

    def setUp(self):
        # Archivo de prueba
        self.test_nombre = "cliente_test"
        self.test_desc = "Servicio de prueba"
        gestion.clientes.clear()
        if os.path.exists("clientes.json"):
            os.remove("clientes.json")

    def test_crear_cliente(self):
        gestion.crear_clientes(self.test_nombre, self.test_desc)
        self.assertIn(self.test_nombre, gestion.clientes)
        self.assertTrue(os.path.exists(gestion.clientes[self.test_nombre]))

    def tearDown(self):
        if self.test_nombre in gestion.clientes:
            os.remove(gestion.clientes[self.test_nombre])
        if os.path.exists("clientes.json"):
            os.remove("clientes.json")

if __name__ == "__main__":
    unittest.main()

