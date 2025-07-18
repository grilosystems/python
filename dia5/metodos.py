print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

def saludar():
    print("¡Hola mundo!")
    
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
    

nombre_persona = "Marco"

def cuadrado(un_numero):
    print(un_numero ** 2)
    
un_numero = 2

def cuadrado(un_numero):
    print(un_numero ** 2)
    
un_numero = 2

def usd_a_eur(dolares):
    return dolares * 0.90
    
dolares = 20

def invertir_palabra(palabra):
    return palabra[::-1].upper()
    
palabra = "CURSO"

def suma_menores(lista_numeros):
    return sum(numero for numero in lista_numeros if numero > 0 and numero < 1000)
    
lista_numeros = [0,1,2,0,3,999,-1,1000]

print(suma_menores(lista_numeros))

def todos_positivos(lista_numeros):
    return all(numero > 0 for numero in lista_numeros)
    
lista_numeros = [1,2,3,4,5,6]

def cantidad_pares(lista_numeros):
    return sum(1 for numero in lista_numeros if numero%2 == 0)
    
lista_numeros = [1,2,4,6,3,6,8,9]

print(cantidad_pares(lista_numeros))