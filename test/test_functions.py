import unittest
from app import custom_function

class TestCustomFunctions(unittest.TestCase):

    def test_custom_function(self):
        result = custom_function(arg1, arg2)  # Llama a tu función personalizada con argumentos adecuados
        self.assertEqual(result, expected_result)  # Verifica que el resultado sea el esperado

if __name__ == '__main__':
    unittest.main()
