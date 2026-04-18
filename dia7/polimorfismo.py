class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print("Muuuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre
    def hablar(self):
        print("Beeee")

vaca1 = Vaca("Aurora")
oveja1 = Oveja("Nube")

def animal_habla(animal):
    animal.hablar()

animal_habla(oveja1)