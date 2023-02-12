import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def test_str_numeromag(self):
        numeromag = db.NumeroMagico(12345679, 5, 9*5*12345679)
        self.assertEqual(str(numeromag), "El numero magico es: 555555555")

    def test_numero_magico(self):
        numeromag = db.numero_magico(5)
        self.assertEqual(numeromag.numero_final, 555555555)
        self.assertEqual(numeromag.numero_magico, 12345679)
        self.assertEqual(numeromag.numero_usuario, 5)

if __name__ == "__main__":
    unittest.main()