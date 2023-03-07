import unittest
import database1 as db1
import database2 as db2

class TestDatabase(unittest.TestCase):
    def test_str_alumno(self):
        alumno = db1.Alumno("Juan", "Pérez", "10")
        self.assertEqual(str(alumno), "Juan Pérez ha sacado un 10 de nota.")

    def test_obtener_datos(self):
        cadena = "zeréP nauJ,01"
        alumno = db1.obtener_datos(cadena)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.nota, "10")

    def test_str_numeromag(self):
        numeromag = db2.NumeroMagico(12345679, 5, 9*5*12345679)
        self.assertEqual(str(numeromag), "El numero magico es: 555555555")

    def test_numero_magico(self):
        numeromag = db2.numero_magico(5)
        self.assertEqual(numeromag.numero_final, 555555555)
        self.assertEqual(numeromag.numero_magico, 12345679)
        self.assertEqual(numeromag.numero_usuario, 5)

if __name__ == "__main__":
    unittest.main()
