"""Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los
métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a
Definir dos objetos de la clase Alumno."""


class Alumno:
    nota = int
    def inicializar(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):
        print("Nombre:",self.nombre)
        print("Nota:",self.nota)

    def notas(self):
        if nota >= 6:
            print(f"Materia regularizada")
        else:
            print(f"Materia libre")
        


alumno1 = Alumno
alumno1.inicializar("andy", 5)
alumno1.imprimir()
alumno1.notas()

alumno2 = Alumno
alumno2.inicializar("jose", 5)
alumno2.imprimir()
alumno2.notas()