class Familia:
    def __init__(self, nombre_padre="Juan", nombre_madre="María", hijos=None):
        self.nombre_padre = nombre_padre
        self.nombre_madre = nombre_madre
        self.hijos = hijos if hijos is not None else []

    def __str__(self):
        nombres_hijos = ", ".join(self.hijos)
        return f"Padre: {self.nombre_padre}, Madre: {self.nombre_madre}, Hijos: {nombres_hijos}"


if __name__ == "__main__":
    familia1 = Familia()
    print("Familia con nombres predefinidos:")
    print(familia1)

    print("\nIngrese los nombres de la familia:")
    nombre_padre = input("Nombre del padre: ")
    nombre_madre = input("Nombre de la madre: ")
    num_hijos = int(input("Número de hijos: "))
    hijos = []
    for i in range(num_hijos):
        hijo = input(f"Nombre del hijo {i+1}: ")
        hijos.append(hijo)
    familia2 = Familia(nombre_padre, nombre_madre, hijos)
    print("\nFamilia con nombres ingresados por el usuario:")
    print(familia2)