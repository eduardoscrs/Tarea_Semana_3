Indicaciones Tarea

Tarea Semana 3 de Programación 2, POO

En grupos de hasta tres personas, deberán desarrollar las actividades propuestas en el lenguaje de
programación de su elección. Los códigos y resultados deben ser alojados en un repositorio público,
preferiblemente en GitHub.

Fecha de entrega: Miércoles 30/08.

1.1 Sistema de Reservación para una Aerolínea
Objetivo:
Desarrollar un sistema de reservación de vuelos utilizando programación orientada a objetos en
Python.
Descripción:
Deberás crear clases para representar aviones, vuelos, pasajeros y reservaciones. El sistema permitirá a los usuarios:
1. Consultar vuelos disponibles.
2. Reservar un vuelo.
3. Cancelar una reservación.
4. Ver las reservaciones de un pasajero.
5. Ver la lista de pasajeros en un vuelo.
Clases a desarrollar:
1. Avion: Representa un avión con:
  • Modelo del avión.
  • Número de asientos.
  • Vuelo: Representa un vuelo con:
2. Número de vuelo.
  • Origen.
  • Destino.
  • Fecha y hora.
  • Avión asignado.
1
• Lista de reservaciones.
• Pasajero: Representa a un pasajero con:
3. Nombre.
  • Número de pasaporte.
  • Lista de vuelos reservados.
  • Reservacion: Representa una reservación con:
4. Número de reservación.
  • Pasajero.
  • Vuelo.
  • Estado (reservado, cancelado).
Funcionalidades:
1. Crear vuelos y añadirlos a una lista de vuelos disponibles. Mostrar vuelos disponibles.
2. Reservar un vuelo: Al reservar, se crea una nueva reservación y se añade a la lista de reservaciones del vuelo y del pasajero.
3. Cancelar una reservación: Cambia el estado de una reservación a “cancelado”.
4. Mostrar todas las reservaciones de un pasajero.
5. Mostrar la lista de pasajeros de un vuelo.
6. Validar que no se puedan sobrepasar el número de asientos de un avión al realizar reservaciones.
7. Validar que un pasajero no pueda reservar el mismo vuelo más de una vez.

1.2 Sistema de Gestión para una Biblioteca
Objetivo:
Desarrollar un sistema de gestión para una biblioteca utilizando programación orientada a objetos
en Python.
Descripción:
Deberás crear clases para representar libros, usuarios, préstamos y el catálogo de la biblioteca. El
sistema permitirá: 1. Añadir y eliminar libros al catálogo. 2. Registrar usuarios. 3. Prestar y
devolver libros. 4. Consultar libros disponibles. 5. Ver el historial de préstamos de un usuario.
Funcionalidades 1. Defina usted las funcionalidades
