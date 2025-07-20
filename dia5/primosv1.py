def contar_primos(limite):
    '''
        Función que encuentra y cuenta números primos hasta el límite dado.
        Retorna: cantidad de primos encontrados
    '''
    if limite < 2:
        print("No hay números primos en el rango.")
        return 0
    
    lista_primos = []
    
    # El dos sabemos que es un primo y no creo que deje de serlo jejeje
    if limite >= 2:
        lista_primos.append(2)

    for numero in range(3,limite + 1, 2):
        es_primo = True
        max_divisor = int(numero ** 0.5) + 1
        
        # Verificamos divisibilidad solo hasta √numero
        for primo in lista_primos: 
            if primo > max_divisor == 0:
                break
            if numero % primo == 0:
                es_primo = False
                break
            
        if es_primo:
            lista_primos.append(numero)
            
    print(f"Total de primos encontrados: {len(lista_primos)}\nPrimos encontrados: {lista_primos}")
        
contar_primos(10)
# 2,3,5,7