def dibujar_rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(caracter * ancho)


ancho = int(input("Ancho: "))
alto = int(input("Alto: "))
caracter = str(input("Caracter: "))

dibujar_rectangulo(ancho, alto, caracter)
