class Persona:
    def __init__(self, nombre="", edad=0):
        self.nombre = nombre
        self.edad = edad

    def cargar_datos(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad de la persona: "))

    def imprimir_datos(self):
        print("Nombre:", self.nombre)
        print("Edad:", self.edad)


class Empleado(Persona):
    def __init__(self, nombre="", edad=0, sueldo=0):
        super().__init__(nombre, edad)
        self.sueldo = sueldo

    def pagar_impuestos(self):
        if self.sueldo > 3000:
            print("Debe pagar impuestos.")
        else:
            print("No debe pagar impuestos.")


if __name__ == "__main__":

    
    empleado = Empleado()
    empleado.cargar_datos()  
    empleado.sueldo = float(input("Ingrese el sueldo del empleado: "))
    print("\nDatos del empleado:")
    empleado.imprimir_datos()  
    empleado.pagar_impuestos()  