import json
from models.Modelo import Modelo
from enum import Enum
import re

class Usuario:
    def __init__(self, id, nome, email, fone, senha, tipo_usuario):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_tipo_usuario(tipo_usuario)

    def set_id(self, id):
        self.__id = id
    
    def set_nome(self, nome):
        if not nome:
            raise ValueError("Nome vazio")
        self.__nome = nome
    
    def set_email(self, email):
        if not email:
            raise ValueError("Email vazio")
        regex = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
        if (re.match(regex, email)):
            self.__email = email
        else:
            raise ValueError("Email inválido. Formato válido xxxxxxx@gmail.com")

    def set_fone(self, fone):
        if not fone:
            raise ValueError("Telefone vazio")
        regex = r'^\(\d{2}\) \d{5}-\d{4}$'
        if (re.match(regex, fone)):
            self.__fone = fone
        else:
            raise ValueError("Formato de telefone inválido. Formato válido (xx) xxxxx-xxxx")

    def set_senha(self, senha):
        if not senha:
            raise ValueError("Senha vazia")
        self.__senha = senha

    def set_tipo_usuario(self, tipo_usuario):
        self.__tipo_usuario = tipo_usuario

    def get_id(self):
        return self.__id
    
    def get_nome(self):
        return self.__nome
    
    def get_email(self):
        return self.__email

    def get_fone(self):
        return self.__fone

    def get_senha(self):
        return self.__senha

    def get_tipo_usuario(self):
        return self.__tipo_usuario
    
    def __str__(self):
        return f"ID = {self.get_id()}  |  NOME = {self.get_nome()}  |  EMAIL = {self.get_email()}  |  FONE = {self.get_fone()} | SENHA = {self.get_senha()} | TIPO USUARIO = {self.get_tipo_usuario()}"
    
    def to_dict(self):
        return {
            "id": self.get_id(), "nome": self.get_nome(), "email" : self.get_email(), "fone" : self.get_fone(), "senha" : self.get_senha(), "tipoUsuario" : self.get_tipo_usuario()
        }
    
class Usuarios(Modelo):
    @classmethod
    def salvar(cls):
        with open("../Arquivos/usuarios.json", mode="w") as arquivo:
            json.dump([usuarios.to_dict() for usuarios in cls.objetos], arquivo, indent=6) #vars - converte um objeto em dicionario
            #dump - pega a lista de obejtos e salva no arquivo
            
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("../Arquivos/usuarios.json", mode="r") as arquivo:
                usuarios_json = json.load(arquivo)
                for obj in usuarios_json:
                    u = Usuario(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"], obj["tipoUsuario"])
                    cls.objetos.append(u)    
        except FileNotFoundError:
            pass