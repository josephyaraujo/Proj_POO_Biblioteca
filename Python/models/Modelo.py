from abc import ABC, abstractmethod

class Modelo(ABC):
    objetos = [] #atributos de classe cls - forma de acessar o atributo da classe 

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        
        #calcular o id do objeto
        id = 0
        for objeto in cls.objetos:
            if objeto.get_id() > id: id = objeto.get_id()
        obj.set_id(id + 1)

        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        # percorre a lista procurando o id    
        for objeto in cls.objetos:
            if objeto.get_id() == id: return objeto
        return None

    @classmethod
    def atualizar(cls, obj):
        objeto = cls.listar_id(obj.get_id())
        if objeto != None:
            cls.objetos.remove(objeto)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        objeto = cls.listar_id(obj.get_id())
        if objeto != None:
            cls.objetos.remove(objeto)
            cls.salvar()

    @classmethod
    @abstractmethod
    def salvar(cls):
        #método abstrato
        pass
            
    @classmethod
    @abstractmethod
    def abrir(cls):
        #metódo abstrato
            pass
    
    def to_dict(self):
        pass