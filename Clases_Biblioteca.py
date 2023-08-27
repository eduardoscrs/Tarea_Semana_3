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
        self.libros.append(libro)

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
