class Perro:
    def ladrar(self):
        print("Guau!")
        
mi_perro = Perro()

mi_perro.ladrar()

class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
        
merlin = Mago()

merlin.lanzar_hechizo()

class Alarma:
    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")
        
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
        
Mascota.respirar()

class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

jugador = Jugador()
jugador.revivir()
print(f"¿El jugador está vivo? {jugador.vivo}")

class Personaje:
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
    def lanzar_flecha(self):
        self.cantidad_flechas -= 1
        