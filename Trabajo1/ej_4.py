def ordenar_de_mayor_a_menor(lista):
    return sorted(lista, reverse=True)


numeros_str = input("Ingrese una lista de números enteros separados por comas: ")
numeros = [int(num) for num in numeros_str.split(",")]

lista_ordenada = ordenar_de_mayor_a_menor(numeros)
print("Lista original:", numeros)
print("Lista ordenada de mayor a menor:", lista_ordenada)

ordenar_de_mayor_a_menor(numeros)