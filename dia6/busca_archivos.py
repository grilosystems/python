from pathlib import Path
from os import system

lista_archivos = Path('C:/Users/User/Desktop/githubs/python/dia6/proyecto/Recetas').glob('**/*.txt')

print(lista_archivos)