from random import randint

numero_secreto = randint(1,11)
intentos = 8
# print(numero_secreto)
player = input('Cual es tu nombre? ')
numero_player = input(f'Hola {player}, he pensado un numero entre el 1 al 10 tienes 8 intentos para adivinar.\nDigita un numero: ')

while intentos > 1:
    if int(numero_player) == numero_secreto:
        print(f'Felicidades {player}, adivinaste, el numero secreto es {numero_player}')
        break
    elif int(numero_player) < numero_secreto:
        intentos -= 1
        numero_player = input(f'Te quedan {intentos} intentos {player}, el numero es MAYOR al que diste, digita un numero: ')
    elif int(numero_player) > numero_secreto:
        intentos -= 1
        numero_player = input(f'Te quedan {intentos} intentos {player}, el numero es MENOR al que diste, digita un numero: ')
    elif int(numero_player) not in range(1,10):
        intentos -= 1
        print(f'{player}, el numero que digitaste no comprende del 1 al 10: {numero_player}')
else:
    print(f':( lo siento {player}, el numero que pense era: {numero_secreto}')