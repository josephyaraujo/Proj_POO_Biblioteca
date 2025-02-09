import json
from models.Modelo import Modelo

class Emprestimo:
    def __init__(self, id, data, data_devolucao, prazo_extendido, id_exemplar, id_usuario):
        self.set_id(id)
        self.set_data(data)
        self.set_data_devolucao(data_devolucao)
        self.prazo_extendido(prazo_extendido)
        self.id_exemplar(id_exemplar)
        self.id_usuario(id_usuario)

    def set_id(self, id):
        self.__id = id
    
    def set_data(self, data):
        self.__data = data
    
    def set_data_devolucao(self, data_devolucao):
        self.__data_devolucao = data_devolucao

    def set_prazo_extendido(self, prazo_extendido):
        self.__prazo_extendido = prazo_extendido

    def set_id_exemplar(self, id_exemplar):
        self.__id_exemplar = id_exemplar

    def set_id_usuario(self, id_usuario):
        self.__id_usuario = id_usuario

    def get_id(self):
        return self.__id
    
    def get_data(self):
        return self.__data
    
    def get_data_devolucao(self):
        return self.__data_devolucao

    def get_prazo_extendido(self):
        return self.__prazo_extendido

    def get_id_exemplar(self):
        return self.__id_exemplar

    def get_id_usuario(self):
        return self.__id_usuario
    
    def __str__(self):
        return f"ID = {self.get_id()}  |  Data = {self.get_data()}  |  DATA DEVOLUCAO = {self.get_data_devolucao()}  |  PRAZO EXTENDIDO = {self.get_prazo_extendido()} | ID EXEMPLAR = {self.get_id_exemplar()} | ID USUARIO = {self.get_id_usuario()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "data": self.get_data(), "data devolucao" : self.get_data_devolucao(), "prazo extendido" : self.get_prazo_extendido(), "id exemplar" : self.get_id_exemplar(), "id usuario" : self.get_id_usuario()
        }
    
class Emprestimos(Modelo):
    @classmethod
    def salvar(cls):
        with open("/workspaces/Proj_POO_Biblioteca/Arquivos/emprestimos.json", mode="w") as arquivo:
            json.dump([emprestimo.to_dict() for emprestimo in cls.objetos], arquivo, indent=6) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("/workspaces/Proj_POO_Biblioteca/Arquivos/emprestimos.json", mode="r") as arquivo:
                emprestimos_json = json.load(arquivo)
                for obj in emprestimos_json:
                    e = Emprestimo(obj["id"], obj["data"], obj["dataDevolucao"], obj["prazoExtendido"], obj["idExemplar"], obj["idUsuario"])
                    cls.objetos.append(e)    
        except FileNotFoundError:
            pass