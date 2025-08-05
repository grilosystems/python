from pathlib import Path
from os import system
import sys

def clear_screen():
    '''Limpia la pantalla de la terminal.'''
    system('cls')

def contar_recetas():
    '''Cuenta el número de recetas en el directorio Recetas y sus subdirectorios.'''
    ruta_base = Path.cwd()
    ruta = ruta_base / 'Recetas/'
    print("Ruta de acceso de recetas:", ruta)
    numero_recetas = 0
    for txt in Path(ruta).glob("**/*.txt"):
        numero_recetas += 1
    return numero_recetas

def obtener_categorias():
    '''Obtiene las categorías de recetas del directorio Recetas.'''
    ruta = Path.cwd() / 'Recetas/'
    categorias = [categoria.name for categoria in ruta.iterdir() if categoria.is_dir()]
    return categorias

def cargar_categoria(categoria):
    '''Carga las recetas de una categoría específica.'''
    ruta_categoria = Path.cwd() / 'Recetas/' / categoria
    recetas = [receta.name for receta in ruta_categoria.glob("*.txt")]
    return recetas

def mostrar_receta(receta):
    '''Muestra el contenido de una receta específica.'''
    ruta_receta = Path.cwd() / 'Recetas/' / receta
    if ruta_receta.exists():
        with open(ruta_receta, 'r', encoding='utf-8') as file:
            contenido = file.read()
            print(contenido)
    else:
        print(f"La receta {receta} no existe.")

def agregar_receta(categoria, nombre_receta, contenido):
    '''Agrega una nueva receta a una categoría específica.'''
    ruta_categoria = Path.cwd() / 'Recetas/' / categoria
    if not ruta_categoria.exists():
        ruta_categoria.mkdir(parents=True)
    ruta_receta = ruta_categoria / f"{nombre_receta}.txt"
    with open(ruta_receta, 'w', encoding='utf-8') as file:
        file.write('\n'.join(contenido))
    print(f"Receta {nombre_receta} agregada a la categoría {categoria}.")

def eliminar_receta(categoria, receta):
    '''Elimina una receta de una categoría específica.'''
    ruta_receta = Path.cwd() / 'Recetas' / categoria / f"{receta}.txt"
    if ruta_receta.exists():
        ruta_receta.unlink()
        print(f"Receta {receta} eliminada de la categoría {categoria}.")
    else:
        print(f"La receta {receta} no existe en la categoría {categoria}.")

def crear_categoria(nombre_categoria):
    '''Crea una nueva categoría de recetas.'''
    ruta_categoria = Path.cwd() / 'Recetas' / nombre_categoria
    if not ruta_categoria.exists():
        ruta_categoria.mkdir(parents=True)
        print(f"Categoría {nombre_categoria} creada.")
    else:
        print(f"La categoría {nombre_categoria} ya existe.")

def eliminar_categoria(nombre_categoria):
    '''Elimina una categoría de recetas.'''
    ruta_categoria = Path.cwd() / 'Recetas' / nombre_categoria
    if ruta_categoria.exists():
        for receta in ruta_categoria.glob("*.txt"):
            receta.unlink()
        ruta_categoria.rmdir()
        print(f"Categoría {nombre_categoria} eliminada.")
    else:
        print(f"La categoría {nombre_categoria} no existe.")

def menu():
    print("1. Categorías de recetas")
    print("2. Agregar receta")
    print("3. Crear categoría de recetas")
    print("4. Eliminar receta")
    print("5. Eliminar categoría de recetas")
    print("6. Salir")
    choice = input("Seleccione una opción: ")
    return choice

def opcion_seleccionada(opcion):
    if opcion == '1':
        clear_screen()
        print("Categorías de recetas...")
        numero_categoria = 0
        recetas = []
        categorias = obtener_categorias()
        for categoria in categorias:
                numero_categoria += 1
                print(f"{numero_categoria}. {categoria}")
        numero_categoria += 1
        print(f"{numero_categoria}. Regresar al menú principal")
        choice = input("Seleccione una opción: ")
        if choice.isdigit() and 1 <= int(choice) <= numero_categoria:
            if int(choice) == numero_categoria:
                main()
            else:
                clear_screen()
                numero_receta = 0
                categoria_seleccionada = categorias[int(choice) - 1]
                print(f"Usted ha seleccionado la categoría: {categoria_seleccionada}")
                recetas = cargar_categoria(categoria_seleccionada)
                if not recetas:
                    print(f"No hay recetas en la categoría {categoria_seleccionada}.")
                    input("Presione Enter para regresar al menú principal...")
                    main()
                    return
                print("Seleccione la receta:")
                for receta in recetas:
                    numero_receta += 1
                    print(f"{numero_receta}. {receta.split('.')[0]}")  # Mostrar sin la extensión .txt
                receta_seleccionada = input("Seleccione una receta: ")
                receta_a_mostrar = categoria_seleccionada + '/' + recetas[int(receta_seleccionada) - 1]
                clear_screen()
                print(f"Usted ha seleccionado la receta: {recetas[int(receta_seleccionada) - 1]}")
                mostrar_receta(receta_a_mostrar)
                input("Presione Enter para regresar al menú principal...")
                main()
        else:
            print("Opción no válida. Intente de nuevo.")
    elif opcion == '2':
        print("Agregando receta...")
        clear_screen()
        numero_categoria = 0
        categorias = obtener_categorias()
        for categoria in categorias:
                numero_categoria += 1
                print(f"{numero_categoria}. {categoria}")
        numero_categoria += 1
        print(f"{numero_categoria}. Regresar al menú principal")
        choice = input("Seleccione una opción: ")
        if choice.isdigit() and 1 <= int(choice) <= numero_categoria:
            if int(choice) == numero_categoria:
                main()
            else:
                clear_screen()
                contenido = []
                categoria_seleccionada = categorias[int(choice) - 1]
                print("Introduzca el nombre de la nueva receta:")
                nombre_receta = input("Nombre de la receta: ")
                print("Introduzca el contenido de la receta:")
                for linea in sys.stdin:
                    if linea.strip() == "":
                        break
                    contenido.append(linea.strip())
                agregar_receta(categoria_seleccionada, nombre_receta, contenido)
                input("Presione Enter para regresar al menú principal...")
                main()
        else:
            print("Opción no válida. Intente de nuevo.")
    elif opcion == '3':
        print("Creando categoría de recetas...")
        clear_screen()
        print("Introduzca el nombre de la nueva categoría:")
        nombre_categoria = input("Nombre de la categoría: ")
        crear_categoria(nombre_categoria)
        input("Presione Enter para regresar al menú principal...")
        main()
    elif opcion == '4':
        print("Eliminando receta...")
        clear_screen()
        numero_categoria = 0
        categorias = obtener_categorias()
        for categoria in categorias:
            numero_categoria += 1
            print(f"{numero_categoria}. {categoria}")
        numero_categoria += 1
        print(f"{numero_categoria}. Regresar al menú principal")
        choice = input("Seleccione una opción: ")
        if choice.isdigit() and 1 <= int(choice) <= numero_categoria:
            if int(choice) == numero_categoria:
                main()
            else:
                clear_screen()
                categoria_seleccionada = categorias[int(choice) - 1]
                numero_receta = 0
                print(f"Usted ha seleccionado la categoría: {categoria_seleccionada}")
                recetas = cargar_categoria(categoria_seleccionada)
                print("Seleccione la receta a eliminar:")
                for receta in recetas:
                    numero_receta += 1
                    print(f"{numero_receta}. {receta.split('.')[0]}")
                numero_receta += 1
                print(f"{numero_receta}. Regresar al menú principal")
                receta_seleccionada = input("Seleccione una receta: ")
                if receta_seleccionada.isdigit() and 1 <= int(receta_seleccionada) <= numero_receta:
                    if int(receta_seleccionada) == numero_receta:
                        main()
                    else:
                        clear_screen()
                        receta_seleccionada = recetas[int(receta_seleccionada) - 1].split('.')[0]
                        eliminar_receta(categoria_seleccionada, receta_seleccionada)
                input("Presione Enter para regresar al menú principal...")
                main()
        else:
            print("Opción no válida. Intente de nuevo.")
    elif opcion == '5':
        print("Eliminando categoría de recetas...")
        clear_screen()
        numero_categoria = 0
        categorias = obtener_categorias()
        for categoria in categorias:
            numero_categoria += 1
            print(f"{numero_categoria}. {categoria}")
        numero_categoria += 1
        print(f"{numero_categoria}. Regresar al menú principal")
        choice = input("Seleccione una opción: ")
        if choice.isdigit() and 1 <= int(choice) <= numero_categoria:
            if int(choice) == numero_categoria:
                main()
            else:
                clear_screen()
                categoria_seleccionada = categorias[int(choice) - 1]
                print(f"Usted ha seleccionado la categoría: {categoria_seleccionada}")
                eliminar_categoria(categoria_seleccionada)
                input("Presione Enter para regresar al menú principal...")
                main()
        else:
            print("Opción no válida. Intente de nuevo.")
    elif opcion == '6':
        print("Saliendo del programa.")
        exit()
    else:
        print("Opción no válida. Intente de nuevo.")

def main():
    '''Función principal que inicia el programa.'''
    clear_screen()
    print("Bienvenido al Recetario de cocina")
    print(f"Total de recetas: {contar_recetas()}")
    #while True:
    menu_choice = menu()
    opcion_seleccionada(menu_choice)

main()
