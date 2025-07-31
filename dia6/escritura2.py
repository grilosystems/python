mi_archivo = open("mi_archivo.txt","a")
mi_archivo.write("Nuevo inicio de sesión")

mi_archivo = open("mi_archivo.txt","r")
contenido = mi_archivo.read()
print(contenido)