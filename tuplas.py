mi_tupla = (1,2,3,4)
print(mi_tupla)

print(mi_tupla[0])
print(mi_tupla[-2])

mi_tupla2 = (1,2,(10,20),9)
print(mi_tupla2[2])

# Seleccion de un elemento de una tupla dentro de otra tupla
print(mi_tupla2[2][0])

#asignacion de variables a partir de una tupla 
t = (1,2,3)
x,y,z = t

print(y)

#Numero de elementos
print(len(t))
#Contar numero de apariciones
print(t.count(1))
#Indice del elemento
print(t.index(3))

mi_tupla3 = (1, 2, 3, 2, 3, 1, 3, 2)

mi_lista = list(mi_tupla3)

print(type(mi_lista))