def buscar_valor(lista, valor):
    for i, num in enumerate(lista):
        if num == valor:
            return i
    return None  

lista = [8, 6, 9, 32]


valor_buscado = int(input("Ingrese el valor a buscar: "))


indice = buscar_valor(lista, valor_buscado)
if indice is not None:
    print(f"El valor {valor_buscado} se encuentra en el índice {indice} de la lista.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la lista.")



buscar_valor(lista, valor_buscado)