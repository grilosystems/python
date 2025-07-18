from random import *

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    
    return [dado1,dado2]

def evaluar_jugada(dados):
    suma_dados = dados[0] + dados[1]
    
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentablemente")
    elif suma_dados > 6 and suma_dados < 10:
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    else:
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

evaluar_jugada(lanzar_dados())

def reducir_lista(lista_numeros):
    lista_numeros.remove(max(lista_numeros))
    return list(set(lista_numeros))
    
    
def promedio(lista_numeros):
    return (sum(numero for numero in lista_numeros)/len(lista_numeros))
    
lista_numeros=[1,2,15,7,2]

print(promedio(reducir_lista(lista_numeros)))

def lanzar_moneda():
    return choice(['Cara','Cruz'])

def probar_suerte(moneda_lanzada, lista_numeros):
    if moneda_lanzada == 'Cara':
        print("La lista se autodestruirá")
        return []
    else:
        print("La lista fue salvada")
        return lista_numeros
    
lista_numeros = [1,2,3,4,5,6]
probar_suerte(lanzar_moneda(),lista_numeros)