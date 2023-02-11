import unittest
import database as db

class TestDatabase(unittest.TestCase):
    def test_str_alumno(self):
        alumno = db.Alumno("Juan", "Pérez", "10")
        self.assertEqual(str(alumno), "Juan Pérez ha sacado un 10 de nota.")

    def test_obtener_datos(self):
        cadena = "zeréP nauJ,01"
        alumno = db.obtener_datos(cadena)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.apellido, "Pérez")
        self.assertEqual(alumno.nota, "10")

if __name__ == "__main__":
    unittest.main()
