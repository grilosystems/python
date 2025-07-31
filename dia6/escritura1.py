mi_archivo = open("mi_archivo.txt", "w")

mi_archivo.write("Nuevo texto")

mi_archivo = open("mi_archivo.txt", "r")

contenido = mi_archivo.read()

print(contenido)