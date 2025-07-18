print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,"naranja")
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv)
print(conjuntos_aislados)

def saludar():
    print("¡Hola mundo!")
    
def bienvenida(nombre_persona):
    print(f"¡Bienvenido {nombre_persona}!")
    

nombre_persona = "Marco"

def cuadrado(un_numero):
    print(un_numero ** 2)
    
un_numero = 2

def cuadrado(un_numero):
    print(un_numero ** 2)
    
un_numero = 2

def usd_a_eur(dolares):
    return dolares * 0.90
    
dolares = 20