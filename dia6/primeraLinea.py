mi_archivo = open("Prueba.txt", "r")

# primera linea
primera_linea = mi_archivo.readline()
print("La primera linea es: " + primera_linea)

mi_archivo.close()