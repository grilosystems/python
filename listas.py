#Una lista es un tipo ordenado de objetos y estas pueden ser de distintos objetos y se pueden anidar, incluso una lista de listas

mi_lista = ["a","b","c","d"]
mi_lista2 = ["e","f","g","h"]

resultado = mi_lista[1]

print(resultado)

print(mi_lista[0:2])

print(mi_lista + mi_lista2)

mi_lista.reverse()
print(mi_lista)
mi_lista.sort()
print(mi_lista)