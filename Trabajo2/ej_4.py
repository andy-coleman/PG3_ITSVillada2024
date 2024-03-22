class Operaciones:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.mostrar_resultados()

    def suma(self):
        return self.num1 + self.num2

    def resta(self):
        return self.num1 - self.num2

    def multiplicacion(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir entre cero."

    def mostrar_resultados(self):
        print("Suma:", self.suma())
        print("Resta:", self.resta())
        print("Multiplicación:", self.multiplicacion())
        print("División:", self.division())

# Ejemplo de uso
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

operaciones = Operaciones(num1, num2)