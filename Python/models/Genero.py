import json
from models.Modelo import Modelo

class Genero:
    def __init__(self, id, descricao):
        self.set_id(id)
        self.set_descricao(descricao)

    def set_id(self, id):
        self.__id = id
    
    def set_descricao(self, descricao):
        self.__descricao = descricao

    def get_id(self):
        return self.__id
    
    def get_descricao(self):
        return self.__descricao
    
    def __str__(self):
        return f"ID = {self.get_id()}  | DESCRICAO = {self.get_descricao()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "descricao": self.get_descricao()
        }
    
class Generos(Modelo):
    @classmethod
    def salvar(cls):
        with open("../Arquivos/generos.json", mode="w") as arquivo:
            json.dump([genero.to_dict() for genero in cls.objetos], arquivo, indent=2) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("../Arquivos/generos.json", mode="r") as arquivo:
                generos_json = json.load(arquivo)
                for obj in generos_json:
                    g = Genero(obj["id"], obj["descricao"])
                    cls.objetos.append(g)    
        except FileNotFoundError:
            pass