def contar_primos(limite):
    '''
        Escribe una función llamada contar_primos() que requiera un solo argumento numérico.
        Esta función va a mostrar en pantalla todos los números primos existentes en el rango que va desde 
        cero hasta ese número incluido, y va a devolver la cantidad de números primos que encontró.
        Aclaración, por convención el 0 y el 1 no se consideran primos.
    '''
    if limite < 2:
        print("No hay números primos en el rango.")
        return 0
    
    lista_primos = []
    lista_numeros = list(range(2,limite+1))

    for numero in lista_numeros:
        lista_primos.append(numero)
        for numero2 in lista_numeros: 
            if numero%numero2 == 0 and numero != numero2:
                lista_primos.pop()
                break
            
    print(f"Total de primos encontrados: {len(lista_primos)}\nPrimos encontrados: {lista_primos}")
        
contar_primos(10)
# 3,5,7