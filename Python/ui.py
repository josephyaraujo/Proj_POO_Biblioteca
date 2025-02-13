# import json
from models.Livro import Livros, Livro
from models.Genero import Generos, Genero
from models.Usuario import Usuario, Usuarios
from models.EnumUsuarios import EnumUsuarios
livros = Livros.listar()
for l in livros:
    print(l)


u = Usuario(0, "josephy", "josephy@gmail.com", "(84) 98888-8888", "jo1234", "CLIENTE")
Usuarios.inserir(u)

u = Usuario(0, "manu", "manu@gmail.com", "(84) 98888-8888", "manu1234", "ADMIN")
Usuarios.inserir(u)
# g = Genero(0, "terror")
#Generos.inserir(g)

#g2 = Genero(0, "romance")
#Generos.inserir(g2)


generos = Generos.listar()
for g in generos:
    print(g)