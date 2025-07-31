mi_archivo = open("Prueba.txt", "r")

# segunda linea
lineas = mi_archivo.readlines()
print("La segunda linea es: " + lineas[1])

mi_archivo.close()