from datetime import datetime

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_prestamos = []

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.strptime(fecha_prestamo, '%d-%m-%Y').date()
        self.fecha_devolucion = None

class Catalogo:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        for existing_libro in self.libros:
            if libro.isbn == existing_libro.isbn:
                print("\nEl libro ya está en el catálogo.\n")
                return
        else:
            self.libros.append(libro)
            print("\nLibro agregado al catálogo.\n")



    def eliminar_libro(self, libro):
        if libro in self.libros:
            self.libros.remove(libro)

    def buscar_libro(self, isbn):
        for libro in self.libros:
            if libro.isbn == isbn:
                return libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def consultar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]

    def prestar_libro(self, libro, usuario, fecha_prestamo):
        if libro in self.libros and libro.disponible:
            prestamo = Prestamo(libro, usuario, fecha_prestamo)
            libro.disponible = False
            usuario.historial_prestamos.append(prestamo)
            return prestamo

    def devolver_libro(self, prestamo, fecha_devolucion):
        if prestamo in prestamo.usuario.historial_prestamos and not prestamo.fecha_devolucion:
            prestamo.fecha_devolucion = fecha_devolucion
            prestamo.libro.disponible = True

    def historial_prestamos_usuario(self, usuario):
        return usuario.historial_prestamos

def mostrar_menu():
    print("=" * 60)
    print("\n ¡Bienvenido al Sistema de Gestión de Biblioteca! \n")
    print("=" * 60)
    print("1. Agregar un libro al catálogo")
    print("2. Eliminar un libro del catálogo")
    print("3. Registrar un nuevo usuario")
    print("4. Eliminar un usuario")
    print("5. Revisar usuarios")
    print("6. Prestar un libro")
    print("7. Devolver un libro")
    print("8. Consultar los libros disponibles")
    print("9. Ver historial de préstamos de un usuario")
    print("0. Salir")
    print("=" * 60)
    return input("Seleccione una opción: ")

catalogo = Catalogo()
usuarios = []


while True:
    opcion = mostrar_menu()

    if opcion == "1":
        titulo = input("\nIngrese el título del libro: \n")
        autor = input("\nIngrese el autor del libro: \n")
        isbn = input("\nIngrese el ISBN del libro: \n")
        nuevo_libro = Libro(titulo, autor, isbn)
        catalogo.agregar_libro(nuevo_libro)


    elif opcion == "2":
        isbn = input("\nIngrese el ISBN del libro a eliminar: \n")
        libro = catalogo.buscar_libro(isbn)
        if libro:
            catalogo.eliminar_libro(libro)
            print("\nLibro eliminado del catálogo.\n")
        else:
            print("\nLibro no encontrado en el catálogo.\n")

    elif opcion == "3":
        nombre_usuario = input("\nIngrese el nombre del usuario: \n")
        id_usuario = input("\nIngrese el ID del usuario: \n")
        nuevo_usuario = Usuario(nombre_usuario, id_usuario)
        usuarios.append(nuevo_usuario)
        print("\nUsuario registrado.\n")

    elif opcion == "4":
        id_usuario = input("\nIngrese el ID del usuario a eliminar: \n")
        usuario = catalogo.buscar_usuario(id_usuario)
        if usuario:
            usuarios.remove(usuario)
            print("\nUsuario eliminado.\n")
        else:
            print("\nUsuario no encontrado.\n")

    elif opcion == "5":
        print("\nUsuarios registrados:")
        for usuario in usuarios:
            print(f"\nNombre: {usuario.nombre} - ID: {usuario.id_usuario}\n")

    elif opcion == "6":
        isbn = input("\nIngrese el ISBN del libro a prestar: \n")
        libro = catalogo.buscar_libro(isbn)
        if libro:
            id_usuario = input("\nIngrese el ID del usuario: \n")
            usuario = catalogo.buscar_usuario(id_usuario)
            if usuario:
                fecha_prestamo = input("\nIngrese la fecha de préstamo: \n")
                try:
                    datetime.strptime(fecha_prestamo, '%d-%m-%Y') 
                except ValueError:
                    print("\nFormato de fecha incorrecto. Use dd-mm-aaaa.\n")
                    continue
                prestamo = catalogo.prestar_libro(libro, usuario, fecha_prestamo)
                prestamo = catalogo.prestar_libro(libro, usuario, fecha_prestamo)
                if prestamo:
                    print("\nLibro prestado.\n")
                else:
                    print("\nEl libro no está disponible para préstamo.\n")
            else:
                print("\nUsuario no registrado.\n")
        else:
            print("\nLibro no encontrado en el catálogo.\n")

    elif opcion == "7":
        isbn = input("\nIngrese el ISBN del libro a devolver: \n")
        libro = catalogo.buscar_libro(isbn)
        if libro:
            id_usuario = input("\nIngrese el ID del usuario: \n")
            usuario = catalogo.buscar_usuario(id_usuario)
            if usuario:
                for prestamo in usuario.historial_prestamos:
                    if prestamo.libro.isbn == isbn and not prestamo.fecha_devolucion:
                        fecha_devolucion = input("Ingrese la fecha de devolución: \n")
                        catalogo.devolver_libro(prestamo, fecha_devolucion)
                        print("\nLibro devuelto.\n")
                        break
                else:
                    print("\nEl usuario no tiene un préstamo activo de este libro.\n")
            else:
                print("\nUsuario no registrado.\n")
        else:
            print("\nLibro no encontrado en el catálogo.\n")

    elif opcion == "8":
        libros_disponibles = catalogo.consultar_libros_disponibles()
        if libros_disponibles:
            for libro in libros_disponibles:
                print(f"\nLibro: {libro.titulo} - Autor: {libro.autor}")
        else:
            print("\nNo hay libros disponibles en este momento.\n")

    elif opcion == "9":
        id_usuario = input("\nIngrese el ID del usuario: \n")
        usuario = catalogo.buscar_usuario(id_usuario)
        if usuario:
            historial_prestamos = catalogo.historial_prestamos_usuario(usuario)
            if historial_prestamos:
                for prestamo in historial_prestamos:
                    print(f"\nLibro: {prestamo.libro.titulo} - Fecha de préstamo: {prestamo.fecha_prestamo}\n")
            else:
                print("\nEl usuario no tiene historial de préstamos.")
        else:
            print("\nUsuario no registrado. \n")

    elif opcion == "0":
        print("\n¡Hasta luego!\n")
        break

    else:
        print("\nOpción incorrecta. Por favor, seleccione una opción válida.\n")