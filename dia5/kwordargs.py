def suma(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total

print(suma(x=3, y=5, z=2))

def cantidad_atributos(**kwargs):
    return len(kwargs)

def lista_atributos(**kwargs):
    return [value for value in kwargs.values()]

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key,val in kwargs.items():
        print(f"{key}: {val}")
        
describir_persona("María", color_ojos="azules", color_pelo="rubio")