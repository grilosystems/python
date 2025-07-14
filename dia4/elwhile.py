numero = 10

while numero > -1:
    print(numero)
    numero -= 1
    
numero = 50

while numero > -1:
    divfive = numero%5
    if divfive == 0:
        print(numero)
        numero -= 1
    else:
        numero -= 1
        continue
    
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for numero in lista_numeros:
    if numero < 0:
        break
    else:
        print(numero)
        
suma_cuadrados = 0

for cuadrado in range(1,16):
    suma_cuadrados += (cuadrado*cuadrado)
    
print(suma_cuadrados)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice, nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')
    
lista_indices = list(enumerate("Python"))
print(lista_indices)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice, nombre in enumerate(lista_nombres):
    if nombre.startswith('M'):
        print(indice)