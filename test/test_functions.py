import unittest
from app import app

class TestCustomFunctions(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Bienvenido a mi aplicación web en Python", response.data)

if __name__ == '__main__':
    unittest.main()
