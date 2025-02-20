import json
from models.Modelo import Modelo

class Emprestimo:
    def __init__(self, id, data, dataDevolucao, prazoExtendido, idExemplar, idUsuario):
        self.set_id(id)
        self.set_data(data)
        self.set_data_devolucao(dataDevolucao)
        self.set_prazo_extendido(prazoExtendido)
        self.set_id_exemplar(idExemplar)
        self.set_id_usuario(idUsuario)

    def set_id(self, id):
        self.__id = id
    
    def set_data(self, data):
        if not data:
            raise ValueError("Campo data não pode ser vazio.")
        self.__data = data
    
    def set_data_devolucao(self, dataDevolucao):
        if not dataDevolucao:
            raise ValueError("Campo data de devolução não pode ser vazio.")
        self.__data_devolucao = dataDevolucao

    def set_prazo_extendido(self, prazoExtendido):
        self.__prazo_extendido = prazoExtendido

    def set_id_exemplar(self, idExemplar):
        if not idExemplar:
            raise ValueError("Campo exemplar não pode ser vazio.")
        self.__id_exemplar = idExemplar

    def set_id_usuario(self, idUsuario):
        if not idUsuario:
            raise ValueError("Campo usuário não pode ser vazio.")
        self.__id_usuario = idUsuario

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
        return f"Data = {self.get_data()}  |  DATA DEVOLUCAO = {self.get_data_devolucao()}  |  PRAZO EXTENDIDO = {self.get_prazo_extendido()} | EXEMPLAR = {self.get_id_exemplar()} | USUARIO = {self.get_id_usuario()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "data": self.get_data(), "dataDevolucao" : self.get_data_devolucao(), "prazoExtendido" : self.get_prazo_extendido(), "idExemplar" : self.get_id_exemplar(), "idUsuario" : self.get_id_usuario()
        }
    
class Emprestimos(Modelo):
    @classmethod
    def salvar(cls):
        with open("../Arquivos/emprestimos.json", mode="w") as arquivo:
            json.dump([emprestimo.to_dict() for emprestimo in cls.objetos], arquivo, indent=6) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("../Arquivos/emprestimos.json", mode="r") as arquivo:
                emprestimos_json = json.load(arquivo)
                for obj in emprestimos_json:
                    e = Emprestimo(obj["id"], obj["data"], obj["dataDevolucao"], obj["prazoExtendido"], obj["idExemplar"], obj["idUsuario"])
                    cls.objetos.append(e)    
        except FileNotFoundError:
            pass