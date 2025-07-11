texto = "Este es el texto de Marco"

resultado = texto

print(resultado)

print(resultado.upper())
print(resultado.lower())
print(resultado.split())
print(resultado.split("t"))

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
print(" ".join([a,b,c,d]))

print(resultado.find("Marco"))
print(resultado.replace("Marco", "Marco Antonio"))

poema = """Mil pequeños peces blancos
comosi hirviera
el color del agua"""

print(poema)
print("agua" in poema)
print(len(poema))