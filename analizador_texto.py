texto = input("Ingresa un texto a elección: ")
letras = []

texto = texto.lower()

letras.append(input("Ingresa primera letra: ").lower())
letras.append(input("Ingresa segunda letra: ").lower())
letras.append(input("Ingresa tercera letra: ").lower())

print("\n")
print("Cantidad de letras: ")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])

print(f"Hemos encontrado la letra {letras[0]} repetida {cantidad_letras1} veces")
print(f"Hemos encontrado la letra {letras[1]} repetida {cantidad_letras2} veces")
print(f"Hemos encontrado la letra {letras[2]} repetida {cantidad_letras3} veces")

print("\n")
print("Cantidad de palabras: ")
palabras = texto.split()
print(f"Hemos encontrado {len(palabras)} palabras")

print("\n")
print("Letras de inicio y fin: ")
print(f"Letra de inicio: {texto[0]}")
print(f"Letra de fin: {texto[-1]}")

print("\n")
print("Texto reversado: ")
palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Si ordenamos tu texto al reves tenemos: '{texto_invertido}'")

print("\n")
print("Buscando la palabra Python: ")
buscar_python = 'python' in texto
dic = {True:"si", False:"no"}
print(f"La palabra Python {dic[buscar_python]} se encuentra")