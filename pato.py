
class Avion:
    def __init__(self, modelo, filas, asientos_por_fila):                                   # Constructor
        self.modelo = modelo                                                                # Atributos
        self.filas = filas                                                                          
        self.asientos_por_fila = asientos_por_fila
        self.asientos_disponibles = [[True] * asientos_por_fila for _ in range(filas)]      # Matriz de asientos disponibles



class Vuelo:
    def __init__(self, numero_vuelo, origen, destino, fecha_hora, avion_asignado):      # Constructor
        self.numero_vuelo = numero_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion_asignado = avion_asignado                                        
        self.reservaciones = []                                                         # Lista de reservaciones
        self.asientos_reservados = [[None] * avion_asignado.asientos_por_fila for _ in range(avion_asignado.filas)]     # Matriz de asientos reservados

    def agregar_reservacion(self, reservacion):                                     # Método
        if len(self.reservaciones) < self.avion_asignado.numero_asientos:           # Condición para verificar si hay asientos disponibles
            self.reservaciones.append(reservacion)                                  # Agregar reservación a la lista
            return True                                                             # Retornar True si se agregó la reservación
        return False                                                                # Retornar False si no se agregó la reservación


    def mostrar_pasajeros(self):
        return [reservacion.pasajero for reservacion in self.reservaciones]        # Retornar lista de pasajeros    


    def reservar_asiento(self, fila, columna, pasajero):                    # Método
        if self.asientos_reservados[fila][columna] is None:                 # Condición para verificar si el asiento está disponible
            self.asientos_reservados[fila][columna] = pasajero              # Asignar pasajero al asiento
            return True
        return False


class Pasajero:
    def __init__(self, nombre, numero_pasaporte):
        self.nombre = nombre
        self.numero_pasaporte = numero_pasaporte                           
        self.vuelos_reservados = []                                        # Lista de vuelos reservados

    def agregar_vuelo_reservado(self, vuelo):
        if vuelo not in self.vuelos_reservados:                            # Condición para verificar si el vuelo ya está en la lista
            self.vuelos_reservados.append(vuelo)                           # Agregar vuelo a la lista
            return True
        return False


class Reservacion:
    def __init__(self, numero_reservacion, pasajero, vuelo, fila, columna):    # Constructor
        self.numero_reservacion = numero_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = "reservado"                                           # Estado inicial de la reservación
        self.fila = fila                                                    # Fila del asiento reservado
        self.columna = columna                                              # Columna del asiento reservado

    def cancelar(self):
        self.estado = "cancelado"



vuelos_disponibles = []
def crear_vuelo(numero_vuelo, origen, destino, fecha_hora, avion_asignado):
    vuelo = Vuelo(numero_vuelo, origen, destino, fecha_hora, avion_asignado)    
    vuelos_disponibles.append(vuelo)                                        # Agregar vuelo a la lista de vuelos disponibles


def mostrar_vuelos_disponibles():                                   
    for vuelo in vuelos_disponibles:                                                            # Iterar sobre la lista de vuelos disponibles
        print(" ")
        print(f"Vuelo {vuelo.numero_vuelo}: {vuelo.origen} → {vuelo.destino} ({vuelo.fecha_hora})")  # Imprimir información del vuelo
        print(" ")


pasajeros = []
def agregar_pasajero():
    print(" ")
    nombre = input("Ingrese el nombre del pasajero: ")
    numero_pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
    for pasajero in pasajeros:                                          # Iterar sobre la lista de pasajeros
        if pasajero.numero_pasaporte == numero_pasaporte:               # Condición para verificar si el pasaporte ya está registrado
            print(" ")
            print("Ya existe un pasajero con este número de pasaporte.")
            print(" ")
            return
    nuevo_pasajero = Pasajero(nombre, numero_pasaporte)                 # Crear nuevo pasajero
    pasajeros.append(nuevo_pasajero)
    print(" ")
    print("Pasajero agregado con éxito.")
    print(" ")


def reservar_vuelo():
    numero_pasaporte = input("Ingrese el número de pasaporte del pasajero: ")
    numero_vuelo = input("Ingrese el número del vuelo que desea reservar: ")
    pasajero = None                                                         # Inicializar variable pasajero
    for p in pasajeros:                                                     # Iterar sobre la lista de pasajeros
        if p.numero_pasaporte == numero_pasaporte:                          # Condición para verificar si el pasaporte está registrado
            pasajero = p                                                    # Asignar pasajero a la variable
            break
    vuelo = None
    for v in vuelos_disponibles:                                            # Iterar sobre la lista de vuelos disponibles
        if v.numero_vuelo == numero_vuelo:                                  # Condición para verificar si el vuelo está disponible
            vuelo = v                                                       # Asignar vuelo a la variable 
            break
    if pasajero is None or vuelo is None:                                   # Condicion para verificar si el pasajero o el vuelo no se encuentran 
        print("No se encontró el pasajero o el vuelo.")
        return
    if vuelo in pasajero.vuelos_reservados:                                 # Condicion para verificar si el pasajero se encuentra en vuelos reservados
        print("El pasajero ya ha reservado este vuelo previamente.")
        return
    fila = int(input("Ingrese el número de fila: "))                        
    columna = int(input("Ingrese el número de columna: "))
    if fila < 0 or fila >= vuelo.avion_asignado.filas or columna < 0 or columna >= vuelo.avion_asignado.asientos_por_fila: # Condicion para que el pasajero no registe asientos invalidos 
        print("Asiento inválido.")
        return
    if vuelo.reservar_asiento(fila, columna, pasajero):                     # Si la funcion reservar_asiento del objeto vuelo retorna True, el asiento se puede reservar
        pasajero.agregar_vuelo_reservado(vuelo)                             # Agregamos el vuelo actual a la lista de vuelos reservados por el pasajero
        reservacion = Reservacion(len(vuelo.reservaciones), pasajero, vuelo, fila, columna)     # Creamos un objeto de tipo Reservacion con la información de la reserva
        vuelo.reservaciones.append(reservacion)                             # Agregamos la nueva reservación a la lista de reservaciones del vuelo
        print("Reservación exitosa.")
    else:
        print("El asiento ya está ocupado.")


def ver_reservaciones_pasajero():
    print(" ")
    numero_pasaporte = input("Ingrese el número de pasaporte del pasajero: ") # se solicita al usuario su numero de pasaporte
    pasajero = None                                                           # 
    for p in pasajeros:                                                       # itera por la lista para buscar el pasajero con el numero ingresado
        if p.numero_pasaporte == numero_pasaporte:                            # se verifica si el numero de pasaporte coincide con el numero ingresado
            pasajero = p                                                      # si encuentra un pasajero con el numero ingresado, se asigna a la variable pasajero y se rompe el ciclo
            break
    if pasajero is None:                                                      # verifica si no se enconntró ningun pasajero con el numero de pasaporte ingresado
        print(" ")
        print("No se encontró el pasajero.")                                  # imprime por pantalla que no se encontro ningun pasajero asociado
        print(" ")
        return
    if not pasajero.vuelos_reservados:                                        # verifica si el pasajero no tiene vuelos reservados
        print(" ")
        print("El pasajero no tiene reservaciones.")                          # imprime por pantalla que no tiene reservaciones
        print(" ")
        return
    print(" ")
    print(f"Reservaciones para el pasajero {pasajero.nombre} ({pasajero.numero_pasaporte}):")
    print(" ")
    for vuelo in pasajero.vuelos_reservados:                                                                    # recorre todos los vuelos reservados por el pasajero             
        for reservacion in vuelo.reservaciones:                                                                 # recorre a traves de las reservaciones en el vuelo actual          
            if reservacion.pasajero == pasajero:                                                                # verifica si la reservacion actual corresponde al pasajero actual             
                print(f"Vuelo {vuelo.numero_vuelo}: {vuelo.origen} → {vuelo.destino} ({vuelo.fecha_hora})")     # muestra por pantalla el numero de vuelo, origen, destino ,fecha y hora
                print(f"Asiento: Fila {reservacion.fila}, Columna {reservacion.columna}")                       # muestra el asiento reservado 


def ver_pasajeros_en_vuelo(): 
    print(" ")
    numero_vuelo = input("Ingrese el número del vuelo: ")                       # se solicita al usuario el numero de vuelo
    vuelo = None                                                                # se inicia vuelo sin valor 
    for v in vuelos_disponibles:                                                # recorre por vuelos disponibles para buscar el vuelo con el numero ingresado
        if v.numero_vuelo == numero_vuelo:                                      # verifica si el numero actual coincide con el ingresado
            vuelo = v                                                           # si eso ocurre, asigna ese vuelo a la variable vuelo y se rompe el ciclo
            break
    if vuelo is None:                                                           # verifica si no se encontro ningun vuelo con el numero ingresado
        print(" ")                                                              # si eso ocurre imprime por pantalla que no hay ningun vuelo asociado
        print("No se encontró el vuelo.")
        print(" ")
        return
    if not vuelo.reservaciones:                                                 # verifica si el vuelo no tiene reservaciones
        print(" ")
        print("No hay pasajeros en este vuelo.")                                # si eso ocurre imprime por pantalla que no hay pasajeros en ese vuelo
        print(" ")
        return
    print(" ")
    print(f"Pasajeros en el vuelo {vuelo.numero_vuelo} ({vuelo.origen} → {vuelo.destino}):")    # Muestra el número, origen y destino del vuelo para indicar que se mostrarán los pasajeros
    for pasajero in vuelo.mostrar_pasajeros():                                      # recorre a traves de la lista de pasajeros obtenida utilizando el metodo mostrar pasajeros() del objeto vuelo
        print(" ")
        print(f"Nombre: {pasajero.nombre}, Pasaporte: {pasajero.numero_pasaporte}") # Muestra el nombre y número de pasaporte del pasajero actual.
        print(" ")


def ver_todos_los_pasajeros():
    print(" ")
    print("Lista de todos los pasajeros:")
    print(" ")
    for pasajero in pasajeros:                                # recorre la lista pasajeros e imprime informacion sobre cada pasajero 
        print(f"Nombre: {pasajero.nombre}, Pasaporte: {pasajero.numero_pasaporte}") # muestra el nombre y el numero de pasaporte de cada pasajero
        print(" ")


def mostrar_menu():                                                         # funcion que muestra el menu dentro del bucle principal
    print('''
==================================================
Bienvenidos a la Aereolínea
==================================================

1. Agregar Pasajero:
2. Mostrar Vuelos Disponibles:
3. Reservar Vuelo:
4. Ver Reservaciones:
5. Ver Lista de Pasajeros en un Vuelo:
6. Ver los pasajeros agregados:
7. Salir 

        ''')

avion1 = Avion("bbbbb", 25, 6)                                              # avion de ejemplo
avion2 = Avion("aaaaa", 25, 6)                                              # avion de ejemplo

crear_vuelo("1", "temuco", "santiago", "2023-09-01 08:00", avion1)          # vuelo de ejemplo
crear_vuelo("2", "santiago", "temuco", "2023-09-02 10:00", avion2)          # vuelo de ejemplo


while True:                                                                 # dependiendo de la opcion ingresada por el usuario, el bucle llama a las funciones solicitadas
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

        print("Opción no válida. Por favor, selecciona una opción válida.") # si el numero ingresado no corresponde, debe volver a digitar un numero hasta que funcione
