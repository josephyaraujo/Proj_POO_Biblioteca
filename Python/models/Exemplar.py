import json
from Modelo import Modelo

class Exemplar:
    def __init__(self, id, edicao, editora, situacao, id_livro, id_genero):
        self.set_id(id)
        self.set_edicao(edicao)
        self.set_editora(editora)
        self.set_situacao(situacao)
        self.set_id_livro(id_livro)
        self.set_id_genero(id_genero)

    def set_id(self, id):
        self.__id = id
    
    def set_edicao(self, edicao):
        self.__edicao = edicao
    
    def set_editora(self, editora):
        self.__editora = editora

    def set_situacao(self, situacao):
        self.__situacao = situacao

    def set_id_livro(self, id_livro):
        self.__id_livro = id_livro

    def set_id_genero(self, id_genero):
        self.__id_genero = id_genero

    def get_id(self):
        return self.__id
    
    def get_edicao(self):
        return self.__edicao
    
    def get_editora(self):
        return self.__editora

    def get_situacao(self):
        return self.__situacao

    def get_id_livro(self):
        return self.__id_livro

    def get_id_genero(self):
        return self.__id_genero
    
    def __str__(self):
        return f"ID = {self.get_id()}  |  EDICAO = {self.get_edicao()}  |  EDITORA = {self.get_editora()}  |  SITUACAO = {self.get_situacao()} | ID LIVRO = {self.get_id_livro()} | ID GENERO = {self.get_id_genero()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "edicao": self.get_edicao(), "editora" : self.get_editora(), "situacao" : self.get_situacao(), "id livro" : self.get_id_livro(), "id genero" : self.get_id_genero()
        }
class Exemplares(Modelo):
    @classmethod
    def salvar(cls):
        with open("/workspaces/Proj_POO_Biblioteca/Arquivos/exemplares.json", mode="w") as arquivo:
            json.dump([exemplar.to_dict() for exemplar in cls.objetos], arquivo, indent=6) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("/workspaces/Proj_POO_Biblioteca/Arquivos/exemplares.json", mode="r") as arquivo:
                exemplares_json = json.load(arquivo)
                for obj in exemplares_json:
                    e = Exemplar(obj["id"], obj["edicao"], obj["editora"], obj["situacao"], obj["idLivro"], obj["idGenero"])
                    cls.objetos.append(e)    
        except FileNotFoundError:
            pass