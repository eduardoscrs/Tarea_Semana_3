
#? Objetivo: Desarrollar un sistema de reservación de vuelos utilizando programación orientada a objetos en Python.


#*crear clases para representar aviones, vuelos, pasajeros y reservaciones.
#*Avión: Representa un avión con: Modelo del avión. Número de asientos.

class Avion:
    def __init__(self, modelo, num_asientos):
        self.modelo = modelo
        self.num_asientos = num_asientos
        
#* Vuelo: Representa un vuelo con: -Número de vuelo. -Origen. -Destino. -Fecha y hora. -Avión asignado. lista de reservaciones.
        #*Crear vuelos y añadirlos a una lista de vuelos disponibles. Mostrar vuelos disponibles.
        #*Reservar un vuelo: Al reservar, se crea una nueva reservación y se añade a la lista de reservaciones del vuelo y del pasajero.
            
class Vuelo:
    def __init__(self, num_vuelo, origen, destino, fecha_hora, avion):
        self.num_vuelo = num_vuelo
        self.origen = origen
        self.destino = destino
        self.fecha_hora = fecha_hora
        self.avion = avion
        self.reservaciones = []
        
        def reservar(self, pasajero): #! falta revisar si el pasajero ya tiene una reservacion en este vuelo o si ya no hay asientos disponibles
            reservacion = Reservacion(len(self.reservaciones)+1, pasajero, self, "reservado")
            self.reservaciones.append(reservacion)
            pasajero.vuelos_reservados.append(reservacion)
            
        def cancelar_reservacion(self, num_reservacion):
            for reservacion in self.reservaciones:
                if reservacion.num_reservacion == num_reservacion:
                    reservacion.estado = "cancelado"
                    print("Reservación cancelada")
                    return
            print("Reservación no encontrada")
                


#*Pasajero: Representa a un pasajero con: -Nombre. -Número de pasaporte. -Lista de vuelos reservados

class Pasajero:
    def __init__(self, nombre, num_pasaporte):
        self.nombre = nombre
        self.num_pasaporte = num_pasaporte
        self.vuelos_reservados = []
        self.reservaciones = []      
        
#* Reservación: Representa una reservación con: -Número de reservación. -Pasajero. -Vuelo. Estado (reservado, cancelado).

class Reservacion:
    def __init__(self, num_reservacion, pasajero, vuelo, estado):
        self.num_reservacion = num_reservacion
        self.pasajero = pasajero
        self.vuelo = vuelo
        self.estado = estado
        
      