class Padre:
    def hablar(self):
        print("Hola")

class Hijo(Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()
mi_nieto.hablar()