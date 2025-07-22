'''
Juego del ahorcado
'''

from random import *

# elegir palabra y mostrar guiones, cargar vidas
def inicio_ahorcado():
    estados_mexico = [
    "Aguascalientes", "Baja California", "Baja California Sur", 
    "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", 
    "CDMX", "Durango", "Guanajuato", "Guerrero", 
    "Hidalgo", "Jalisco", "Mexico", "Michoacan", "Morelos", 
    "Nayarit", "Nuevo Leon", "Oaxaca", "Puebla", "Queretaro", 
    "Quintana Roo", "San Luis Potosi", "Sinaloa", "Sonora", 
    "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatan", 
    "Zacatecas"]
    
    palabra_secreta = choice(estados_mexico)
    guiones = '-' * len(palabra_secreta)
    
    parametros_inicio = {"vidas":6, "estado":palabra_secreta.lower(), "guiones":guiones}
    
    return parametros_inicio

def obtener_una_letra(mensaje="Ingresa una letra: "):
    while True:
        entrada = input(mensaje).strip()
        if len(entrada) != 1:
            if entrada.isspace(): 
                continue
            print("Debe ser exactamente un carácter.")
        elif not (entrada.isalpha() or entrada.isspace()):
            print("Solo se permiten letras (a-z) minus o espacio.")
        else:
            return entrada.lower()

def enmascarar_palabra(palabra, letras_reveladas=None):
    if letras_reveladas is None:
        letras_reveladas = set()
    
    resultado = []
    for letra in palabra:
        if letra.lower() in letras_reveladas:
            resultado.append(letra)
        else:
            resultado.append('_')
    return ''.join(resultado)

def play_game(config_inicio):
    lista_errores = []
    vidas = config_inicio['vidas']
    guiones = config_inicio['guiones']
    estado = config_inicio['estado']
    letras_encontradas = []
    resultado = ''
    
    print("Este es el juego del ahorcado version estados de Mexico")
    print(f"{estado} Adivina el estado de Mexico que pense tienes {vidas} vidas: ")
    print(f"{guiones}")
    while vidas > 0:
        
        if str(resultado) == str(estado):
            print(f"GANASTE ENCONTRASTE LA PALABRA: {estado.upper()}")
            return 0
        
        letra = obtener_una_letra("Adivina la letra: ")
        
        if letra in letras_encontradas:
            print(f"La letra {letra} ya ha sido encontrada")
            continue

        if letra in estado:
            letras_encontradas.append(letra)
            resultado = enmascarar_palabra(estado, letras_encontradas)
            print(resultado)
        else:
            lista_errores.append(letra)
            print(lista_errores)
            vidas -= 1
            print(f"Te quedan {vidas} vidas...")
            
    
play_game(inicio_ahorcado())

