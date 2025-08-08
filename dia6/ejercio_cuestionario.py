
from pathlib import Path

# Definir la ruta al directorio del cuestionario
ruta = Path('C:/Users/Usuario/Desktop/Curso Python') / 'Cuestionario Día 6' / 'Pregunta 1'
carpeta = ruta.parents[3]

print(carpeta)