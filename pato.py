class Avion:
    def __init__(self, modelo, numero_asientos):
        self.modelo = modelo
        self.numero_asientos = numero_asientos


class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha_hora, avion_asignado):
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion_asignado = avion_asignado
        self.reservaciones = []


    def agregar_reservacion(self, reservacion):
        if len(self.reservaciones) < self.avion_asignado.numero_asientos:
            self.reservaciones.append(reservacion)
            return True
        return False


    def mostrar_pasajeros(self):
        return [reservacion.pasajero for reservacion in self.reservaciones]


class Pasajero:
    def __init__(self, nombre, numero_pasaporte):
        self.nombre = nombre
        self.numero_pasaporte = numero_pasaporte
        self.vuelos_reservados = []

    def agregar_vuelo_reservado(self, vuelo):
        if vuelo not in self.vuelos_reservados:
            self.vuelos_reservados.append(vuelo)
            return True
        return False


class Reservacion:
    def __init__(self, numero_reservacion, pasajero, vuelo):
        self.numero_reservacion = numero_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "reservado"


    def cancelar(self):
        self.estado = "cancelado"



vuelos_disponibles = []
def crear_vuelo(numero_vuelo, origen, destino, fecha_hora, avion_asignado):
    vuelo = Vuelo(numero_vuelo, origen, destino, fecha_hora, avion_asignado)
    vuelos_disponibles.append(vuelo)


def mostrar_vuelos_disponibles():
    for vuelo in vuelos_disponibles:
        print(" ")
        print(f"Vuelo {vuelo.numero_vuelo}: {vuelo.origen} → {vuelo.destino} ({vuelo.fecha_hora})")
        print(" ")


pasajeros = []
def agregar_pasajero():
    print(" ")
    nombre = input("Ingrese el nombre del pasajero: ")
    numero_pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
    for pasajero in pasajeros:
        if pasajero.numero_pasaporte == numero_pasaporte:
            print(" ")
            print("Ya existe un pasajero con este número de pasaporte.")
            print(" ")
            return
    nuevo_pasajero = Pasajero(nombre, numero_pasaporte)
    pasajeros.append(nuevo_pasajero)
    print(" ")
    print("Pasajero agregado con éxito.")
    print(" ")


def reservar_vuelo():
    print(" ")
    numero_pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
    numero_vuelo = input("Ingrese el número del vuelo que desea reservar: ")
    pasajero = None
    for p in pasajeros:
        if p.numero_pasaporte == numero_pasaporte:
            pasajero = p
            break
    vuelo = None
    for v in vuelos_disponibles:
        if v.numero_vuelo == numero_vuelo:
            vuelo = v
            break
    if pasajero is None or vuelo is None:
        print(" ")
        print("No se encontró el pasajero o el vuelo.")
        print(" ")
        return
    if vuelo in pasajero.vuelos_reservados:
        print(" ")
        print("El pasajero ya ha reservado este vuelo previamente.")
        print(" ")
        return
    if vuelo.agregar_reservacion(Reservacion(len(vuelo.reservaciones) + 1, pasajero, vuelo)):
        pasajero.agregar_vuelo_reservado(vuelo)
        print(" ")
        print("Reservación exitosa.")
        print(" ")
    else:
        print(" ")
        print("No hay asientos disponibles en este vuelo.")
        print(" ")


def ver_reservaciones_pasajero():
    print(" ")
    numero_pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
    pasajero = None
    for p in pasajeros:
        if p.numero_pasaporte == numero_pasaporte:
            pasajero = p
            break
    if pasajero is None:
        print(" ")
        print("No se encontró el pasajero.")
        print(" ")
        return
    if not pasajero.vuelos_reservados:
        print(" ")
        print("El pasajero no tiene reservaciones.")
        print(" ")
        return
    print(" ")
    print(f"Reservaciones para el pasajero {pasajero.nombre} ({pasajero.numero_pasaporte}):")
    print(" ")
    for vuelo in pasajero.vuelos_reservados:
        print(" ")
        print(f"Vuelo {vuelo.numero_vuelo}: {vuelo.origen} → {vuelo.destino} ({vuelo.fecha_hora})")
        print(" ")


def ver_pasajeros_en_vuelo():
    print(" ")
    numero_vuelo = input("Ingrese el número del vuelo: ")
    vuelo = None
    for v in vuelos_disponibles:
        if v.numero_vuelo == numero_vuelo:
            vuelo = v
            break
    if vuelo is None:
        print(" ")
        print("No se encontró el vuelo.")
        print(" ")
        return
    if not vuelo.reservaciones:
        print(" ")
        print("No hay pasajeros en este vuelo.")
        print(" ")
        return
    print(" ")
    print(f"Pasajeros en el vuelo {vuelo.numero_vuelo} ({vuelo.origen} → {vuelo.destino}):")
    for pasajero in vuelo.mostrar_pasajeros():
        print(" ")
        print(f"Nombre: {pasajero.nombre}, Pasaporte: {pasajero.numero_pasaporte}")
        print(" ")


def ver_todos_los_pasajeros():
    print(" ")
    print("Lista de todos los pasajeros:")
    print(" ")
    for pasajero in pasajeros:
        print(f"Nombre: {pasajero.nombre}, Pasaporte: {pasajero.numero_pasaporte}")
        print(" ")


def mostrar_menu():
    print('''
==================================================
Bienvenidos a la Aereolínea
==================================================
1. Agregar Pasajero:
2. Mostrar Vuelos Disponibles:
3. Reservar Vuelo:
4. Ver Reservaciones:
5. Ver Lista de Pasajeros en un Vuelo:
7. Ver los pasajeros agregados:
6. Salir 
        ''')

avion1 = Avion("Boeing 737", 150)
avion2 = Avion("Airbus A320", 180)

crear_vuelo("uno", "temuco", "santiago", "2023-09-01 08:00", avion1)
crear_vuelo("dos", "santiago", "temuco", "2023-09-02 10:00", avion2)


while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")
    if opcion == "1":
        agregar_pasajero()
        pass
    elif opcion == "2":
        mostrar_vuelos_disponibles()
    elif opcion == "3":
        reservar_vuelo()
        pass
    elif opcion == "4":
        ver_reservaciones_pasajero()
        pass
    elif opcion == "5":
        ver_pasajeros_en_vuelo()
        pass
    elif opcion == "6":
        ver_todos_los_pasajeros()
        pass
    elif opcion == "7":
        print("¡Muchas gracias por visitarnos, hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")