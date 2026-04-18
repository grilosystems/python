class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, numero_cuenta):
        super().__init__(nombre, apellido, edad)
        self.numero_cuenta = numero_cuenta
        self.balance = 0
    
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Edad: {self.edad}, Número de Cuenta: {self.numero_cuenta}, Balance: ${self.balance}"

    def depositar(self, monto):
        if monto > 0:
            self.balance += monto
            print(f"Depósito exitoso. Nuevo balance: ${self.balance}")
        else:
            print("El monto a depositar debe ser positivo.")

    def retirar(self, monto):
        if monto > 0:
            if self.balance >= monto:
                self.balance -= monto
                print(f"Retiro exitoso. Nuevo balance: ${self.balance}")
            else:
                print("Fondos insuficientes para realizar el retiro.")
        else:
            print("El monto a retirar debe ser positivo.")

    def __del__(self):
        print(f"El cliente {self.nombre} {self.apellido} ha sido eliminado del sistema.")

def crear_cliente():
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    edad = int(input("Ingrese la edad del cliente: "))
    numero_cuenta = input("Ingrese el número de cuenta del cliente: ")
    return Cliente(nombre, apellido, edad, numero_cuenta)

def inicio():
    while True:
        print("\n--- Menú de Banco ---")
        print("1. Crear cliente")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Imprimir información del cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            cliente = crear_cliente()
            print("Cliente creado exitosamente.")
        elif opcion == '2':
            if 'cliente' in locals():
                monto = float(input("Ingrese el monto a depositar: "))
                cliente.depositar(monto)
            else:
                print("No hay cliente creado. Por favor, cree un cliente primero.")
        elif opcion == '3':
            if 'cliente' in locals():
                monto = float(input("Ingrese el monto a retirar: "))
                cliente.retirar(monto)
            else:
                print("No hay cliente creado. Por favor, cree un cliente primero.")
        elif opcion == '4':
            if 'cliente' in locals():
                print(cliente)
            else:
                print("No hay cliente creado. Por favor, cree un cliente primero.")
        elif opcion == '5':
            if 'cliente' in locals():
                del cliente  # Eliminar el cliente antes de salir
                
            print("Gracias por usar el sistema bancario. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    inicio()
