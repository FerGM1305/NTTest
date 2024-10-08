import unittest
from fastapi.testclient import TestClient
from ApiNumerosNaturales import app

client = TestClient(app)

class TestAPI(unittest.TestCase):

    def test_extraer_numero_valido(self):
        # Enviar un número válido para extraer
        response = client.post("/extraer/", json={"numero": 5})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Número 5 extraído correctamente."})

    def test_extraer_numero_ya_extraido(self):
        # Intentar extraer el mismo número dos veces
        response = client.post("/extraer/", json={"numero": 5})
        self.assertEqual(response.status_code, 400)  # La primera extracción debe funcionar

        response = client.post("/extraer/", json={"numero": 5})
        self.assertEqual(response.status_code, 400)  # La segunda debe fallar
        self.assertEqual(response.json(), {"detail": "El número 5 ya fue extraído o no está en el conjunto."})

    def test_extraer_numero_fuera_de_rango(self):
        # Intentar extraer un número fuera del rango permitido
        response = client.post("/extraer/", json={"numero": 105})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "El número debe estar entre 1 y 100."})

    def test_numero_faltante(self):
        # Extraer un número y verificar que el faltante es el correcto
        client.post("/extraer/", json={"numero": 5})#Extraemos el número 5

        response = client.get("/faltante/")
        self.assertEqual(response.status_code, 200)
        numero_faltante = response.json()["numero_faltante"]
        self.assertEqual(numero_faltante, 5)

if __name__ == '__main__':
    unittest.main()
