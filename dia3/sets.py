mi_set = set([1,2,3,4,5])

print(type(mi_set))
print(mi_set)

#otra forma de declarar sets
other_set = {1,2,3}
print(type(other_set))
print(other_set)

#Los sets son elementos unicos 
mi_set2 = {1,1,2,2,3,3,4,4,5,5,5}
print(mi_set2)

#el set si admite tuplas
mi_set3 = {1,2,(10,20),4,5}
print(mi_set3)
print(len(mi_set3))

#Buscar dentro de un set
print(2 in mi_set3)

#union de set 
set_mix = mi_set3.union(mi_set)
print(set_mix)

set_mix.add((10,22))
print(set_mix)
set_mix.remove(4)
print(set_mix)

# metodo discart es diferewnte a remove y no manda errores
set_mix.discard((10,22))
print(set_mix)

#metodo clear, sirve para vaciar el set
set_mix.clear()
print(set_mix)