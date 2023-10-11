"""
Estas pruebas (caja de cristal) son muy buenas para hacer Regression testing o mocks, cuando descubrimos un bug de un programa que ya salio a luz.
"""

import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)

        self.assertEqual(resultado, False)
        

# Si el nombre de este modulo es main, y unicamente es main cuando este es el punto de entrada, cuando lo ejecutamos directamente como script, entonces vamos a correr la funcion main dentro del modulo unittest
if __name__ == '__main__':
    unittest.main()