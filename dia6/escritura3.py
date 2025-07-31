registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

registro = open("registro.txt","a")
for c in registro_ultima_sesion:
    registro.writelines(c + "\t")

registro = open("registro.txt","r")
print(registro.read())