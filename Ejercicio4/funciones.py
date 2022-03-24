class Libro:
    def __init__(self, titulo, autor, isbn, genero ):
        self.autor = autor
        self.titulo = titulo
        self.isbn = isbn
        self.genero = genero

print("Elija el nombre del libro a buscar:")
tit = input()
print("¿Quién es el autor del libro?")
aut = input()
print("¿De qué género es?")
gen = input()
print("¿Cuál es el isbn?")
isbn = input()

libro = Libro(tit, aut, isbn, gen)