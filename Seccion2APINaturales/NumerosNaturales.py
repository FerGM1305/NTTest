from pydantic import BaseModel

class NumeroRequest(BaseModel):
    numero: int


class NumeroConjunto100:
    def __init__(self):
        self.numeros = set(range(1, 101))
        self.numero_extraido = None

    def extract(self, numero):
        if numero < 1 or numero > 100:
            raise ValueError("El número debe estar entre 1 y 100.")
        if numero in self.numeros:
            self.numeros.remove(numero)
            self.numero_extraido = numero
        else:
            raise ValueError(f"El número {numero} ya fue extraído o no está en el conjunto.")

    def calcular_numero_faltante(self):
        suma_total = sum(range(1, 101))
        suma_restante = sum(self.numeros)
        numero_faltante = suma_total - suma_restante
        return numero_faltante
