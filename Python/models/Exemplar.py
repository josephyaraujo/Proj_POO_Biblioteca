import json
from models.Modelo import Modelo

class Exemplar:
    def __init__(self, id, edicao, editora, situacao, idLivro, idGenero):
        self.set_id(id)
        self.set_edicao(edicao)
        self.set_editora(editora)
        self.set_situacao(situacao)
        self.set_id_livro(idLivro)
        self.set_id_genero(idGenero)

    def set_id(self, id):
        self.__id = id
    
    def set_edicao(self, edicao):
        if not edicao:
            raise ValueError("Campo edição não pode ser vazio.")
        if edicao < 1:
            raise ValueError("Edição inválida.")
        self.__edicao = edicao
    
    def set_editora(self, editora):
        if not editora:
            raise ValueError("Campo editora não pode ser vazio.")
        self.__editora = editora

    def set_situacao(self, situacao):
        if situacao == "":
            raise ValueError("Campo situação não pode ser vazio.")
        self.__situacao = situacao

    def set_id_livro(self, idLivro):
        if not idLivro:
            raise ValueError("Campo livro não pode ser vazio.")
        self.__id_livro = idLivro

    def set_id_genero(self, idGenero):
        if not idGenero:
            raise ValueError("Campo gênero não pode ser vazio.")
        self.__id_genero = idGenero

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
        from view.view import View
        situacao = "Disponível" if self.get_situacao() else "Emprestado"

        livro = View.livro_listar()
        genero = View.genero_listar()

        nome_livro = next((l.get_titulo() for l in livro if l.get_id() == self.get_id_livro()), "Desconhecido")
        nome_genero = next((g.get_descricao() for g in genero if g.get_id() == self.get_id_genero()), "Desconhecido")
        return f"EDICAO = {self.get_edicao()}  |  EDITORA = {self.get_editora()}  |  SITUACAO = {situacao} | LIVRO = {nome_livro} | GENERO = {nome_genero}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "edicao": self.get_edicao(), "editora" : self.get_editora(), "situacao" : self.get_situacao(), "idLivro" : self.get_id_livro(), "idGenero" : self.get_id_genero()
        }
class Exemplares(Modelo):
    @classmethod
    def salvar(cls):
        with open("../Arquivos/exemplares.json", mode="w") as arquivo:
            json.dump([exemplar.to_dict() for exemplar in cls.objetos], arquivo, indent=6) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("../Arquivos/exemplares.json", mode="r") as arquivo:
                exemplares_json = json.load(arquivo)
                for obj in exemplares_json:
                    e = Exemplar(obj["id"], obj["edicao"], obj["editora"], obj["situacao"], obj["idLivro"], obj["idGenero"])
                    cls.objetos.append(e)    
        except FileNotFoundError:
            pass