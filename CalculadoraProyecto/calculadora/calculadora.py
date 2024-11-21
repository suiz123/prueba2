class Calculadora:
    """
    Clase Calculadora Básica: realiza operaciones matemáticas básicas.
    """
    def suma(self, a, b):
        """Devuelve la suma de dos números."""
        return a + b
 
    def resta(self, a, b):
        """Devuelve la resta de dos números."""
        return a - b
 
    def multiplicacion(self, a, b):
        """Devuelve la multiplicación de dos números."""
        return a * b
 
    def division(self, a, b):
        """
        Devuelve la división de dos números.
        Maneja la división por cero.
        """
        if b == 0:
            raise ValueError("No se puede dividir por cero.")
        return a / b
