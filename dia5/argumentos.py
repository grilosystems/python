def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1,2,3,4))

def suma_cuadrados(*args):
    return sum(numero**2 for numero in args)
    
print(suma_cuadrados(1,2,3))

def suma_absolutos(*args):
    return sum(abs(numero) for numero in args)
    
print(suma_absolutos(-1,-1,2))

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"
    
print(numeros_persona("Marco",1,2,3,4,5))