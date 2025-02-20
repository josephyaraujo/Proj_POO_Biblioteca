import json
from models.Modelo import Modelo

class Livro:
    def __init__(self, id, titulo, autor, ano, idGenero):
        self.set_id(id)
        self.set_titulo(titulo)
        self.set_autor(autor)
        self.set_ano(ano)
        self.set_id_genero(idGenero)

    def set_id(self, id):
        self.__id = id
    
    def set_titulo(self, titulo):
        if not titulo:
            raise ValueError("Titulo vazio")
        self.__titulo = titulo
    
    def set_autor(self, autor):
        if not autor:
            raise ValueError("Autor vazio")
        self.__autor = autor

    def set_ano(self, ano):
        if ano <= 1000:
            raise ValueError("Ano inválido")
        self.__ano = ano

    def set_id_genero(self, idGenero):
        if not idGenero:
            raise ValueError("Gênero vazio")
        self.__id_genero = idGenero

    def get_id(self):
        return self.__id
    
    def get_titulo(self):
        return self.__titulo
    
    def get_autor(self):
        return self.__autor

    def get_ano(self):
        return self.__ano
    
    def get_id_genero(self):
        return self.__id_genero
    
    def __str__(self):
        return f"TITULO = {self.get_titulo()}  |  AUTOR = {self.get_autor()}  |  ANO = {self.get_ano()} | GENERO = {self.get_id_genero()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "titulo": self.get_titulo(), "autor" : self.get_autor(), "ano" : self.get_ano(), "idGenero" : self.get_id_genero()
        }
    
class Livros(Modelo):
    @classmethod
    def salvar(cls):
        with open("../Arquivos/livros.json", mode="w") as arquivo:
            json.dump([livro.to_dict() for livro in cls.objetos], arquivo, indent=5) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("../Arquivos/livros.json", mode="r") as arquivo:
                livros_json = json.load(arquivo)
                for obj in livros_json:
                    l = Livro(obj["id"], obj["titulo"], obj["autor"], obj["ano"], obj["idGenero"])
                    cls.objetos.append(l)    
        except FileNotFoundError:
            pass