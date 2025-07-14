valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [cuadrado ** 2 for cuadrado in valores]

print(valores_cuadrado)

valores = [1, 2, 3, 4, 5, 6, 9.5] 

valores_pares = [par for par in valores if par%2 == 0]

print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(f-32)*(5/9) for f in temperatura_fahrenheit]

print(grados_celsius)