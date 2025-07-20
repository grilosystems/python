
def devolver_distintos(num1,num2,num3):
    '''
        Crea una función llamada devolver_distintos() que reciba 3integers como parámetros. 
        Si la suma de los 3 numeros es mayor a 15, va a devolver elnúmero mayor.
        Si la suma de los 3 numeros es menor a 10, va a devolver elnúmero menor.
        Si la suma de los 3 números es un valor entre 10 y 15 (incluidos) va a devolver el 
        número de valor intermedio.
    '''
    numeros = [num1,num2,num3]
    suma = sum(numeros)
    if suma > 15:
        return max(numeros)
    elif suma < 10:
        return min(numeros)
    elif 10 <= suma <= 15:
        return sorted(numeros)[1]
    return None

print(devolver_distintos(1,0,9))