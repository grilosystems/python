class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")
    
    def hablar(self):
        print("Hola, soy la madre")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()
mi_nieto.reir()

print(Nieto.__mro__)


class Vertebrado:
    vertebrado = True

class Pez:
    def nadar(self):
        print("El ornitorrinco nada")

class Reptil:
    def poner_huevos(self):
        print("El ornitorrinco pone huevos")

class Ave:
    tiene_pico = True

class Mamifero:
    def amamantar(self):
        print("El ornitorrinco amamanta a sus crías")

class Ornitorrinco(Vertebrado, Pez, Reptil, Ave, Mamifero):
    venenoso = True

    def caminar(self):
        print("El ornitorrinco camina")

ornitorrinco = Ornitorrinco()
print("vertebrado:", ornitorrinco.vertebrado)
print("tiene_pico:", ornitorrinco.tiene_pico)
print("venenoso:", ornitorrinco.venenoso)
ornitorrinco.poner_huevos()
ornitorrinco.nadar()
ornitorrinco.caminar()
ornitorrinco.amamantar()