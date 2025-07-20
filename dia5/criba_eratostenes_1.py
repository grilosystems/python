def contar_primos(limite):
    if limite < 2:
        return 0
    
    # Criba de Eratóstenes con optimizaciones:
    sieve = bytearray([1]) * (limite + 1)
    sieve[0:2] = b'\x00\x00'  # 0 y 1 no son primos
    
    # Solo verificamos hasta √limite
    for num in range(2, int(limite ** 0.5) + 1):
        if sieve[num]:
            # Marcamos múltiplos comenzando desde num²
            sieve[num*num : limite+1 : num] = b'\x00' * len(sieve[num*num : limite+1 : num])
    
    # Contamos los primos (opcional: podemos generarlos)
    primos_localizados = [i for i, es_primo in enumerate(sieve) if es_primo]
    return primos_localizados

def guardar_primos(lista_numeros_primos):
    with open("primos.txt", "w") as file:
        file.write(f"Total de primos encontrados: {len(lista_numeros_primos)}\n")
        file.write("Lista de numeros primos:\n ")
        for primo in lista_numeros_primos:
            file.write(f"{primo}\n")

guardar_primos(contar_primos(1000000))