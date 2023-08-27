class Libro:
    def __init__(self, autor, año, titulo, genero, estado):
        self.autor = autor
        self.año = año
        self.titulo = titulo
        self.genero = genero
        self.estado = estado

class Usuario:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.libros_prestados = []

class Prestamo:
    def __init__(self, usuario, libro, fecha_prestamo, fecha_devolucion):
        self.usuario = usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

class Catalogo:
    def __init__(self, libros):
        self.libros = libros

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro):
        self.libros.remove(libro)

    def consultar_libros(self):
        for libro in self.libros:
            if libro.estado == "disponible":
                print(libro.titulo)

    def prestar_libro(self, libro, usuario):
        if libro.estado == "disponible":
            libro.estado = "prestado"
            usuario.libros_prestados.append(libro)
            print("El libro ha sido prestado")
        else:
            print("El libro no está disponible")

    def devolver_libro(self, libro, usuario):
        if libro.estado == "prestado":
            libro.estado = "disponible"
            usuario.libros_prestados.remove(libro)
            print("El libro ha sido devuelto")
        else:
            print("El libro no está prestado")

def mostrar_menu():
    print("Bienvenido al sistema de gestión de la biblioteca")
    print("1. Añadir libro")
    print("2. Eliminar libro")
    print("3. Consultar libros disponibles")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Salir")
    opcion = int(input("Ingrese una opción: "))
    print()

    return opcion

libros = []
catalogo = Catalogo(libros)

while True:
    opcion = mostrar_menu()

    if opcion == 1:
        autor = input("Ingrese el autor del libro: ")
        año = input("Ingrese el año del libro: ")
        titulo = input("Ingrese el titulo del libro: ")
        genero = input("Ingrese el genero del libro: ")
        estado = "disponible"
        libro = Libro(autor, año, titulo, genero, estado)
        catalogo.agregar_libro(libro)
        print("El libro ha sido agregado")
        print()

    elif opcion == 2:
        titulo = input("Ingrese el titulo del libro a eliminar: ")
        for libro in libros:
            if libro.titulo == titulo:
                catalogo.eliminar_libro(libro)
                print("El libro ha sido eliminado")
                print()

    elif opcion == 3:
        print("Estos son los libros disponibles:")
        catalogo.consultar_libros()
        print()
        
    elif opcion == 4:
        titulo = input("Ingrese el titulo del libro a prestar: ")
        for libro in libros:
            if libro.titulo == titulo:
                catalogo.prestar_libro(libro)
                print("El libro ha sido prestado")
                print()
                
    elif opcion == 5:
        titulo = input("Ingrese el titulo del libro a devolver: ")
        for libro in libros:
            if libro.titulo == titulo:
                catalogo.devolver_libro(libro)
                print("El libro ha sido devuelto")
                print()

    elif opcion == 6:
        print("Gracias por utilizar el sistema de gestión de la biblioteca")
        break
