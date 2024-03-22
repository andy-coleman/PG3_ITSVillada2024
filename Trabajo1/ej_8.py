def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)

def dibujar_triangulo(base, caracter):
    for i in range(1, base + 1):
        print(caracter * i)

opcion = input("¿Desea dibujar un rectángulo (R) o un triángulo (T)? ").upper()

if opcion == 'R':
    ancho = int(input("Ingrese el ancho del rectángulo: "))
    alto = int(input("Ingrese el alto del rectángulo: "))
    caracter = input("Ingrese el carácter para dibujar el rectángulo: ")
    dibujar_rectangulo(ancho, alto, caracter)
elif opcion == 'T':
    base = int(input("Ingrese la base del triángulo: "))
    caracter = input("Ingrese el carácter para dibujar el triángulo: ")
    dibujar_triangulo(base, caracter)
else:
    print("Opción no válida. Por favor, ingrese 'R' para rectángulo o 'T' para triángulo.")
