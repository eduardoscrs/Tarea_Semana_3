from datetime import datetime

class Libro:                                        #se crea la clase libro
    def __init__(self, titulo, autor, isbn):        #se crea el metodo init, que recibe como parametros titulo, autor e isbn
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn                            #se crea el atributo isbn (identificador unico del libro)
        self.disponible = True                      #se crea el atributo disponible, que por defecto es True

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.historial_prestamos = []               #se crea el atributo historial_prestamos, que es una lista vacia

class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = datetime.strptime(fecha_prestamo, '%d-%m-%Y').date()      #se crea el atributo fecha_prestamo, que es un objeto datetime
        self.fecha_devolucion = None

class Catalogo:
    def __init__(self):
        self.libros = []                #se crea el atributo libros, que es una lista vacia

    def agregar_libro(self, libro):                         #se crea el metodo agregar_libro, que recibe como parametro libro
        for existing_libro in self.libros:                  #se itera sobre la lista de libros
            if libro.isbn == existing_libro.isbn:           #si el isbn del libro que se quiere agregar es igual al isbn de un libro que ya esta en el catalogo
                print("\nEl libro ya está en el catálogo.\n")   #se imprime un mensaje de error
                return
        else:
            self.libros.append(libro)                           #si el libro no esta en el catalogo, se agrega a la lista de libros
            print("\nLibro agregado al catálogo.\n")



    def eliminar_libro(self, libro):                #se crea el metodo eliminar_libro, que recibe como parametro libro
        if libro in self.libros:
            self.libros.remove(libro)

    def buscar_libro(self, isbn):               #se crea el metodo buscar_libro, que recibe como parametro isbn
        for libro in self.libros:               #se itera sobre la lista de libros
            if libro.isbn == isbn:              #si el isbn del libro es igual al isbn que se esta buscando
                return libro                    #se retorna el libro
        return None

    def buscar_usuario(self, id_usuario):
        for usuario in usuarios:                    #se itera sobre la lista de usuarios
            if usuario.id_usuario == id_usuario:        #si el id del usuario es igual al id que se esta buscando
                return usuario                  #se retorna el usuario
        return None

    def consultar_libros_disponibles(self):
        return [libro for libro in self.libros if libro.disponible]    #se retorna una lista con los libros disponibles

    def prestar_libro(self, libro, usuario, fecha_prestamo):
        if libro in self.libros and libro.disponible:               #si el libro esta en el catalogo y esta disponible
            prestamo = Prestamo(libro, usuario, fecha_prestamo)     #se crea un objeto prestamo
            libro.disponible = False                #se cambia el atributo disponible del libro a False
            usuario.historial_prestamos.append(prestamo)        #se agrega el prestamo al historial de prestamos del usuario
            return prestamo                                     #se retorna el prestamo

    def devolver_libro(self, prestamo, fecha_devolucion):
        if prestamo in prestamo.usuario.historial_prestamos and not prestamo.fecha_devolucion:      #si el prestamo esta en el historial de prestamos del usuario y no tiene fecha de devolucion
            prestamo.fecha_devolucion = fecha_devolucion    #se le asigna la fecha de devolucion al prestamo
            prestamo.libro.disponible = True            #se cambia el atributo disponible del libro a True

    def historial_prestamos_usuario(self, usuario):
        return usuario.historial_prestamos              #se retorna el historial de prestamos del usuario

def mostrar_menu():
    print("-" * 60)
    print("\n ¡Bienvenido al Sistema de Gestión de Biblioteca! \n")
    print("-" * 60)
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
    print("." * 60)
    print()
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
        libro = catalogo.buscar_libro(isbn)             #se busca el libro en el catalogo
        if libro:                                       #si el libro esta en el catalogo
            catalogo.eliminar_libro(libro)              #se elimina el libro del catalogo
            print("\nLibro eliminado del catálogo.\n")  #se imprime un mensaje de exito
        else:
            print("\nLibro no encontrado en el catálogo.\n")        #si el libro no esta en el catalogo, se imprime un mensaje de error

    elif opcion == "3":
        nombre_usuario = input("\nIngrese el nombre del usuario: \n")   #se pide el nombre del usuario
        id_usuario = input("\nIngrese el ID del usuario: \n")           #se pide el id del usuario
        nuevo_usuario = Usuario(nombre_usuario, id_usuario)             #se crea el usuario
        usuarios.append(nuevo_usuario)                                  #se agrega el usuario a la lista de usuarios
        print("\nUsuario registrado.\n")                                #se imprime un mensaje de exito

    elif opcion == "4":
        id_usuario = input("\nIngrese el ID del usuario a eliminar: \n")
        usuario = catalogo.buscar_usuario(id_usuario)                       #se busca el usuario en el catalogo
        if usuario:                                                         #si el usuario esta en el catalogo
            usuarios.remove(usuario)                                        #se elimina el usuario de la lista de usuarios
            print("\nUsuario eliminado.\n")
        else:
            print("\nUsuario no encontrado.\n")

    elif opcion == "5":
        print("\nUsuarios registrados:")                
        for usuario in usuarios:                                                    #se itera sobre la lista de usuarios
            print(f"\nNombre: {usuario.nombre} - ID: {usuario.id_usuario}\n")       #se imprime el nombre y el id de cada usuario

    elif opcion == "6":
        isbn = input("\nIngrese el ISBN del libro a prestar: \n")    #se pide el isbn del libro a prestar
        libro = catalogo.buscar_libro(isbn)                         #se busca el libro en el catalogo
        if libro:                                                   #si el libro esta en el catalogo
            id_usuario = input("\nIngrese el ID del usuario: \n")       #se pide el id del usuario
            usuario = catalogo.buscar_usuario(id_usuario)               #se busca el usuario en el catalogo
            if usuario:                                                     #si el usuario esta en el catalogo
                fecha_prestamo = input("\nIngrese la fecha de préstamo: \n")    #se pide la fecha de prestamo
                try:                                                                    #se intenta convertir la fecha a un objeto datetime
                    datetime.strptime(fecha_prestamo, '%d-%m-%Y')                       #si la fecha es valida, se crea el objeto datetime
                except ValueError:                                                          #si la fecha no es valida, se imprime un mensaje de error
                    print("\nFormato de fecha incorrecto. Use dd-mm-aaaa.\n")
                    continue                                                                        #se vuelve al inicio del ciclo
                prestamo = catalogo.prestar_libro(libro, usuario, fecha_prestamo)                   #se crea el prestamo
                if prestamo:                                                            #si el prestamo se creo correctamente
                    print("\nLibro prestado.\n")                                        #se imprime un mensaje de exito
                else:   
                    print("\nEl libro no está disponible para préstamo.\n")         #si el prestamo no se creo correctamente, se imprime un mensaje de error
            else:
                print("\nUsuario no registrado.\n")                     #si el usuario no esta en el catalogo, se imprime un mensaje de error
        else:
            print("\nLibro no encontrado en el catálogo.\n")            #si el libro no esta en el catalogo, se imprime un mensaje de error

    elif opcion == "7":
        isbn = input("\nIngrese el ISBN del libro a devolver: \n")
        libro = catalogo.buscar_libro(isbn)                     #se busca el libro en el catalogo
        if libro:                                                       #si el libro esta en el catalogo
            id_usuario = input("\nIngrese el ID del usuario: \n")       #se pide el id del usuario
            usuario = catalogo.buscar_usuario(id_usuario)               #se busca el usuario en el catalogo
            if usuario:                                                     #si el usuario esta en el catalogo
                for prestamo in usuario.historial_prestamos:          #se itera sobre el historial de prestamos del usuario
                    if prestamo.libro.isbn == isbn and not prestamo.fecha_devolucion:   #si el isbn del libro es igual al isbn del libro del prestamo y el prestamo no tiene fecha de devolucion
                        fecha_devolucion = input("Ingrese la fecha de devolución: \n")  #se pide la fecha de devolucion
                        catalogo.devolver_libro(prestamo, fecha_devolucion)         #se devuelve el libro
                        print("\nLibro devuelto.\n")                    #se imprime un mensaje de exito
                        break                       #se termina el ciclo
                else:
                    print("\nEl usuario no tiene un préstamo activo de este libro.\n")  #si el usuario no tiene un prestamo activo de este libro, se imprime un mensaje de error
            else:
                print("\nUsuario no registrado.\n")                    #si el usuario no esta en el catalogo, se imprime un mensaje de error
        else:
            print("\nLibro no encontrado en el catálogo.\n")        #si el libro no esta en el catalogo, se imprime un mensaje de error

    elif opcion == "8":
        libros_disponibles = catalogo.consultar_libros_disponibles()    #se obtiene la lista de libros disponibles
        if libros_disponibles:                                      #si hay libros disponibles
            for libro in libros_disponibles:                        #se itera sobre la lista de libros disponibles
                print(f"\nLibro: {libro.titulo} - Autor: {libro.autor}")    #se imprime el titulo y el autor de cada libro
        else:
            print("\nNo hay libros disponibles en este momento.\n")     #si no hay libros disponibles, se imprime un mensaje de error

    elif opcion == "9":
        id_usuario = input("\nIngrese el ID del usuario: \n")       #se pide el id del usuario
        usuario = catalogo.buscar_usuario(id_usuario)            #se busca el usuario en el catalogo
        if usuario:                                         #si el usuario esta en el catalogo
            historial_prestamos = catalogo.historial_prestamos_usuario(usuario)   #se obtiene el historial de prestamos del usuario
            if historial_prestamos:                                             #si el usuario tiene historial de prestamos                     
                for prestamo in historial_prestamos:                            #se itera sobre el historial de prestamos
                    print(f"\nLibro: {prestamo.libro.titulo} - Fecha de préstamo: {prestamo.fecha_prestamo}\n")  #se imprime el titulo del libro y la fecha de prestamo
            else:       
                print("\nEl usuario no tiene historial de préstamos.")      #si el usuario no tiene historial de prestamos, se imprime un mensaje de error
        else:
            print("\nUsuario no registrado. \n")        #si el usuario no esta en el catalogo, se imprime un mensaje de error

    elif opcion == "0":
        print("\n¡Hasta luego!\n")
        break

    else:
        print("\nOpción incorrecta. Por favor, seleccione una opción válida.\n")