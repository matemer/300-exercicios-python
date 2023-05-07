class Livros:
    def __init__(self, livro1, **tantofaz):
        self.livro1 = livro1

livrosvar = Livros('Livroexemplo')
livrosvar.tantoligo = 'O hobbit'

print(livrosvar.livro1)
print(livrosvar.tantoligo)