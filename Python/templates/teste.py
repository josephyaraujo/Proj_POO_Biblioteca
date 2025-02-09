# import json
from models.Livro import Livros, Livro

livros = Livros.listar()
for l in livros:
    print(l)
# print(Livros.listar())
