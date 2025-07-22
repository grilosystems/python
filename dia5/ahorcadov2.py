from random import choice

palabras = ['panadero', 'dinosaurio', 'tiburon', 'megalodon', 'memin']
letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado = False

def elegir_palabra(lista_palabras):
    palabra_elegida = choice(lista_palabras)
    letras_unicas = len(set(palabra_elegida))
    
    return palabra_elegida, letras_unicas

def pedir_letra():
    letra = input("Ingresa una letra: ")
    es_valida = False
    while not es_valida:
        if letra.isalpha() and len(letra) == 1:
            es_valida = True
        else:
            print("Debe ser una letra entre [a-z]")
            es_valida = True
            
    return letra

def mostrar_nuevo_tablero(palabra_elegida):
    
    lista_oculta = []
    
    for l in palabra_elegida:
        if l in letras_correctas:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
            
    print(' '.join(lista_oculta))
    
def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    
    fin = False
    
    if letra_elegida in palabra_oculta and letra_elegida not in letras_correctas:
        letras_correctas.append(letra_elegida)
        coincidencias += 1
    elif letra_elegida in palabra_oculta and letra_elegida in letras_correctas:
        print('Ya has encontrado esa letra intenta con otra')
    else:
        letras_incorrectas.append(letra_elegida)
        vidas -= 1
        
    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
        
    return vidas, fin, coincidencias

def perder():
    print("Te has quedado sin vidas")
    print("La palabra oculta era " + palabra)
    
    return True

def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print("Felicitaciones, has encontrado la palabra!!!")
    
    return True

palabra, letras_unicas = elegir_palabra(palabras)

while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('Letras incorrectas: ' + '-'.join(letras_incorrectas))
    print(f'Vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    
    letra = pedir_letra()
    intentos, terminado, aciertos = chequear_letra(letra, palabra, intentos, aciertos)
    
    juego_terminado = terminado