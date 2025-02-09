# import json
from Livro import Livros, Livro
from Genero import Generos, Genero

livros = Livros.listar()
for l in livros:
    print(l)
# print(Livros.listar())

g = Genero(0, "terror")
Generos.inserir(g)