##############################################################################################
#                                       Avion  
##############################################################################################
from datetime import datetime
class Avion:
    def __init__(self, modelo):
        self.modelo = modelo
        self.num_filas = 24
        self.num_columnas = 6
        self.asientos_disponibles = [[True] * self.num_columnas for _ in range(self.num_filas)]
Avion_1 = Avion("Airbus A320")
Avion_2 = Avion("Embraer E195")
Avion_3 = Avion("Boeing 737")

        #se crea una lista de listas vacias, donde cada lista interior representa una fila de asientos
        #el numero de columnas del interior, se repetira segun el numero total columnas que hayan en el avion 

##############################################################################################
#                                       Vuelos 
##############################################################################################

class Vuelo:
    def __init__(self, num_vuelo, origen, destino, fecha_hora, avion):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion = avion
        self.reservaciones = []
        self.asientos_asignados = [[None] * avion.num_columnas for _ in range(avion.num_filas)]
        #asigna a la matriz como None ya que ningun pasajero esta usando ese asiento 
        
    def reservar(self, pasajero, fila, columna):
        if fila < 1 or fila > self.avion.num_filas or columna < 1 or columna > self.avion.num_columnas: #si el numero ingresado por el usuario es menor a uno, entonces
            print("La fila o columna elegida no es válida.")
            return
        
        if self.asientos_asignados[fila - 1][columna - 1] is not None: #si el asiento asignado no es None(indicando que esta ocupado), entonces:
            print("El asiento ya está ocupado.")
            return
        
        reservacion = Reservacion(len(self.reservaciones) + 1, pasajero, self, "reservado")
        self.reservaciones.append(reservacion)
        self.asientos_asignados[fila - 1][columna - 1] = pasajero
        pasajero.vuelos_reservados.append(reservacion)
        self.avion.asientos_disponibles[fila - 1][columna - 1] = False
        
    def cancelar_reservacion(self, num_reservacion):
        for reservacion in self.reservaciones:
            if reservacion.num_reservacion == num_reservacion:
                reservacion.estado = "cancelado"
                fila, columna = reservacion.pasajero.obtener_asiento(self)
                self.asientos_asignados[fila - 1][columna - 1] = None
                print("Reservación cancelada.")
                return
        print("Reservación no encontrada.")



##############################################################################################
#                                       pasajeros
##############################################################################################


class Pasajero:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.vuelos_reservados = []
        self.reservaciones = []
        
    def obtener_asiento(self, vuelo):
        for fila in range(len(vuelo.asientos_asignados)):
            for columna in range(len(vuelo.asientos_asignados[fila])):
                if vuelo.asientos_asignados[fila][columna] == self:
                    return fila + 1, columna + 1
        return None, None

##############################################################################################
#                                       reservacion
##############################################################################################

class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo, estado):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = estado

##############################################################################################
#                                       Menu
##############################################################################################
def mostrar_menu():
    print(" ")
    print("1. registrar pasajero")
    print("2. Reservar vuelo")
    print("3. Cancelar reservación")
    print("4. consultar vuelos disponibles")
    print("5. ver reservaciones")
    print("6. ver lista de pasajeros del vuelo")
    print("7. Salir")
    print(" ")
    return input("seleccione una opción: ")
    

Vuelo_1 = Vuelo("AR 1240", "Chile", "New York", "12-08-2023 14:00", Avion_1)
Vuelo_2 = Vuelo("LA 1311", "Peru", "China", "08-04-2023 13:30", Avion_2)
Vuelo_3 = Vuelo("AK 4200", "Colombia", "Espana", "01-12-2023 16:00", Avion_3)

def mostrar_vuelos_disponibles():
    print("")
    print("Vuelos disponibles:")
    print("1. AR 1240 Chile New York 12-08-2023 14:00 avion1: Airbus A320")
    print("2. LA 1311 Peru China 08-04-2023 13:30 avion2: Embraer E195")
    print("3. AK 4200 Colombia España 01-12-2023 16:00 avion3: Boeing 737")

def mostrar_reservaciones(pasajero):
    print("Reservaciones para", pasajero.nombre)
    for reservacion in pasajero.reservaciones:
        print("Vuelo:", reservacion.vuelo.num_vuelo)
        print("Estado:", reservacion.estado)
        print("Origen:", reservacion.vuelo.origen)
        print("Destino:", reservacion.vuelo.destino)
        print("Fecha y Hora:", reservacion.vuelo.fecha_hora)
        print("")

def mostrar_lista_pasajeros(vuelo):
    print("Pasajeros en el vuelo", vuelo.num_vuelo)
    for pasajero in vuelo.reservaciones:
        print(pasajero.pasajero.nombre)

def main():
    pasajeros = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            nombre = input("Ingrese su nombre y apellido: ")
            num_pasaporte = input("Ingrese su numero de pasaporte: ")
            nuevo_pasajero = Pasajero(nombre, num_pasaporte)
            pasajeros.append(nuevo_pasajero)
            print("Pasajero registrado con éxito.")

        elif opcion == "2":
            num_pasaporte = input("Ingrese su numero de pasaporte: ")

            # Buscar el pasajero en la lista por número de pasaporte
            pasajero = None
            for p in pasajeros:
                if p.num_pasaporte == num_pasaporte:
                    pasajero = p
                    break

            if pasajero is None:
                print("Pasajero no encontrado.")
            else:
                print("Pasajero encontrado:", pasajero.nombre)
                mostrar_vuelos_disponibles()
                opcion_vuelo = input("Elija el número de vuelo: ")

                vuelo_seleccionado = None
                if opcion_vuelo == "1":
                    vuelo_seleccionado = Vuelo_1
                elif opcion_vuelo == "2":
                    vuelo_seleccionado = Vuelo_2
                elif opcion_vuelo == "3":
                    vuelo_seleccionado = Vuelo_3
                else:
                    print("Opción inválida. Seleccione una opción válida.")
                    continue

                fila = int(input("Elija la fila del asiento: "))
                columna = int(input("Elija la columna del asiento: "))

                if not vuelo_seleccionado.avion.asientos_disponibles[fila - 1][columna - 1]:
                    print("El asiento ya está ocupado.")
                else:
                    vuelo_seleccionado.reservar(pasajero, fila, columna)
                    print("Reservación realizada con éxito.")

        elif opcion == "3":
            num_reservacion = int(input("Ingrese el número de reservación a cancelar: "))
            pasajero.cancelar_reservacion(num_reservacion)

        elif opcion == "4":
            mostrar_vuelos_disponibles()

        elif opcion == "5":
            mostrar_reservaciones(pasajero)

        elif opcion == "6":
            opcion_vuelo = input("Ingrese el número de vuelo: ")
            if opcion_vuelo == "1":
                mostrar_lista_pasajeros(Vuelo_1)
            elif opcion_vuelo == "2":
                mostrar_lista_pasajeros(Vuelo_2)
            elif opcion_vuelo == "3":
                mostrar_lista_pasajeros(Vuelo_3)
            else:
                print("Opción inválida. Seleccione una opción válida.")

        elif opcion == "7":
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida. Seleccione una opción válida.")

if __name__ == "__main__":
    main()



