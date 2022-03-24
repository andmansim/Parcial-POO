class Libro:
    def __init__(self, nombre, autor, titulo, isbn, genero ):
        self.nombre = nombre
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        self.genero = genero

print("Elija el nombre del libro a buscar:")
nomb = input()
print("¿Quién es el autor del libro?")
aut = input()
libro = Libro(nomb, aut)