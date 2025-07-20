def hay_consecutivos_iguales(*args):
    '''
        Escribe una función que requiera una cantidad indefinida deargumentos. 
        Lo que hará esta función es devolver True si enalgún momento se ha ingresado al 
        numero cero repetido dosveces consecutivas.
        Por ejemplo:
            (5,6,1,0,0,9,3,5) >>> True
            (6,0,5,1,0,3,0,1) >>> False
    '''
    lista_numeros = list(args)
    return any(a == b for a, b in zip(lista_numeros, lista_numeros[1:]))

print(hay_consecutivos_iguales(1,2,3,4,0,1,0))  