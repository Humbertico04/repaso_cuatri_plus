import unittest
import database1 as db1
import database2 as db2
import database3 as db3
import descomposicion as db5

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

    def test_comparar_listas(self):
        lista = db3.listas.comparar_listas(["h",'o','l','a',' ', 'm','u','n','d','o'], ["h",'o','l','a',' ', 'l','u','n','a'])
        self.assertEqual(lista, ['h', 'o', 'l', 'a', ' ', 'u', 'n', 'o'])
    
    def test_elementos_repetidos(self):
        lista = db3.listas.elementos_repetidos(['h', 'o', 'l', 'a', ' ', 'u', 'n', 'o'])
        self.assertEqual(lista, ['h', 'o', 'l', 'a', ' ', 'u', 'n'])

    def test_descomposicion(self):
        lista = db5.descomposicion(248)
        self.assertEqual(lista, "\n002\n040\n800")

if __name__ == "__main__":
    unittest.main()