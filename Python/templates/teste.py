# import json
from models.Livro import Livros

livros = Livros.listar()
for l in livros:
    print(l)
# print(Livros.listar())
