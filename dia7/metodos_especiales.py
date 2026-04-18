class CD:

    def __init__(self, titulo, artista, canciones):
        self.titulo = titulo
        self.artista = artista
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.artista} con {self.canciones} canciones"   
    
    def __len__(self):
        return self.canciones
    
    def __del__(self):
        print(f"El CD {self.titulo} ha sido eliminado") 
    
mi_cd = CD("Pink Floyd", "The Wall", 24)
print(mi_cd)
print(len(mi_cd))

# Eliminar instance
del mi_cd