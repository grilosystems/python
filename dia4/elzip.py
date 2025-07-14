capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

pais_capital = list(zip(paises, capitales))

for pais, capital in pais_capital:
   print(f"La capital de {pais} es {capital}")
   
marcas = ["Apple", "Samsung", "Nike", "Tesla", "Coca-Cola"]
productos = ["iPhone 15", "Galaxy S24", "Air Jordan 1", "Model 3", "Coca-Cola Original"]

mi_zip = list(zip(marcas, productos))

espanol=['uno','dos','tres','cuatro','cinco']
portugues=['um','dois','três','quatro','cinco']
ingles=['one','two','three','four','five']

numeros=list(zip(espanol,portugues,ingles))

print(numeros)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango=list[max(lista_numeros),min(lista_numeros)]

print(rango)

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]

rango=max(lista_numeros)-min(lista_numeros)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}

edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades.keys())

print(f'edad minima {edad_minima} ultimo nombre {ultimo_nombre}')

