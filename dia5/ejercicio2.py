def unicas_orden(word):
    '''
        Escribe una función (puedes ponerle cualquier nombre quequieras) que reciba 
        cualquier palabra como parámetro, y quedevuelva todas sus letras únicas 
        (sin repetir) pero en ordenalfabético.
        Por ejemplo si al invocar esta función pasamos la palabra"entretenido", 
        debería devolver ['d', 'e', 'i', 'n', 'o', 'r', 't']
    '''
    letras = list(set(word))
    letras.sort()
    return letras           

print(unicas_orden("entretenido"))