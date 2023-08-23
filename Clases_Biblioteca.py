# Desarrollar un sistema de gestión para una biblioteca utilizando programación orientada a objetos
# en Python.

# todo Deberás crear clases para representar libros, usuarios, préstamos y el catálogo de la biblioteca
''' 
    El sistema permitirá: 1. Añadir y eliminar libros al catálogo. 2. Registrar usuarios. 3. Prestar y
    devolver libros. 4. Consultar libros disponibles. 5. Ver el historial de préstamos de un usuario.
    Funcionalidades 1. Defina usted las funcionalidades que considere necesarias para el sistema.
    
'''


class libro:                                                    #se crea la clase libro
    def __init__(self, autor, año, titulo, genero, estado):     #se crea el constructor de la clase libro
        self.autor = autor                                      #se crean los atributos de la clase libro
        self.año = año
        self.titulo = titulo
        self.genero = genero
        self.estado = estado

class usuario:                                                  #se crea la clase usuario
    def __init__(self, nombre, apellido, edad):                 #se crea el constructor de la clase usuario
        self.nombre = nombre                                    #se crean los atributos de la clase usuario
        self.apellido = apellido
        self.edad = edad
        self.libros_prestados = []

class prestamo:                                                                             #se crea la clase prestamo        
    def __init__(self, nombre, apellido, titulo, autor, fecha_prestamo, fecha_devolucion):  #se crea el constructor de la clase usuario
        self.usuario = usuario                                                              #se crean los atributos de la clase usuario
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
                
class catalogo:                                 #se crea la clase catalogo
    def __init__(self, libros):                 #se crea el constructor de la clase catalogo
        self.libros = libros                    #se crean los atributos de la clase catalogo
        
    def agregar_libro(self, libro):             #se crea el metodo agregar libro
        self.libros.append(libro)
        
    def eliminar_libro(self, libro):        #se crea el metodo eliminar libro
        self.libros.remove(libro)
        
    def consultar_libros(self):             #se crea el metodo consultar libros    
        for libro in self.libros:            #se crea un ciclo for para recorrer la lista de libros
            if libro.estado == "disponible": #se crea una condicion para imprimir solo los libros disponibles
                print(libro.titulo)          #se imprime el titulo del libro
                
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