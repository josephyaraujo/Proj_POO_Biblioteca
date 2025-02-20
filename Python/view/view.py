from models.Usuario import Usuario, Usuarios
from models.Emprestimo import Emprestimo, Emprestimos
from models.Exemplar import Exemplar, Exemplares
from models.Livro import Livro, Livros
from models.Genero import Genero, Generos

class View:
    @staticmethod
    def admin_listar():
        return [usuario for usuario in Usuarios.listar() if usuario.get_tipo_usuario() == "ADMIN"]
    @staticmethod
    def admin_inserir(nome, email, fone, senha, tipo_usuario):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if email == usuario.get_email():
                raise ValueError("Email já cadastrado")
            if usuario.get_tipo_usuario() == "ADMIN":
                raise ValueError("Usuário administrador já cadastrado")
        u = Usuario(0, nome, email, fone, senha, tipo_usuario)
        Usuarios.inserir(u)
    @staticmethod
    def admin_atualizar(id, nome, email, fone, senha):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if email == usuario.get_email() and id != usuario.get_id():
                raise ValueError("Email já cadastrado")
            if id == usuario.get_id():        
                u = Usuarios(id, nome, email, fone, senha, "ADMIN")
        Usuarios.atualizar(u)
    @staticmethod
    def admin_excluir(id):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if id == usuario.get_id():
                u = Usuario(id, usuario.get_nome(), usuario.get_email(), usuario.get_fone(), usuario.get_senha(), "ADMIN")
                Usuarios.excluir(u)

    @staticmethod
    def usuario_autenticar(email, senha):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if usuario.get_email() == email and usuario.get_senha() == senha and usuario.get_tipo_usuario() == "CLIENTE":
                raise ValueError("Cliente não tem acesso a essa página")
            if usuario.get_email() == email and usuario.get_senha() == senha:
                return {"id":usuario.get_id(), "nome": usuario.get_nome(), "tipoUsuario": usuario.get_tipo_usuario()}
        return None
    
    @staticmethod
    def cliente_listar():
        return [usuario for usuario in Usuarios.listar() if usuario.get_tipo_usuario() == "CLIENTE"]
    
    @staticmethod
    def funcionario_listar():
        return [usuario for usuario in Usuarios.listar() if usuario.get_tipo_usuario() == "FUNCIONARIO"]
    @staticmethod
    def funcionario_inserir(nome, email, fone, senha, tipo_usuario):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if email == usuario.get_email():
                raise ValueError("Email já cadastrado")
        u = Usuario(0, nome, email, fone, senha, tipo_usuario)
        Usuarios.inserir(u)
    @staticmethod
    def funcionario_atualizar(id, nome, email, fone, senha):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if email == usuario.get_email() and id != usuario.get_id():
                raise ValueError("Email já cadastrado")
            if id == usuario.get_id():        
                u = Usuarios(id, nome, email, fone, senha, "FUNCIONARIO")
        Usuarios.atualizar(u)
    @staticmethod
    def funcionario_excluir(id):
        usuarios = Usuarios.listar()
        for usuario in usuarios:
            if id == usuario.get_id():
                u = Usuario(id, usuario.get_nome(), usuario.get_email(), usuario.get_fone(), usuario.get_senha(), "FUNCIONARIO")
                Usuarios.excluir(u)

    @staticmethod
    def genero_listar():
        return Generos.listar()
    @staticmethod
    def genero_listar_id(id):
        return Generos.listar_id(id)
    @staticmethod
    def genero_inserir(descricao):
        generos = Generos.listar()
        for genero in generos:
            if descricao == genero.get_descricao():
                raise ValueError("Gênero ja cadastrado")
        g = Genero(0, descricao)
        Generos.inserir(g)
    @staticmethod
    def genero_atualizar(id, descricao):
        generos = Generos.listar()
        for genero in generos:
            if descricao == genero.get_descricao():
                raise ValueError("Gênero ja cadastrado")
        g = Genero(id, descricao)
        Generos.atualizar(g)
    @staticmethod
    def genero_excluir(id):
        g = Genero(id, "genero")
        Generos.excluir(g)

    @staticmethod
    def livro_listar():
        return Livros.listar()
    @staticmethod
    def livro_inserir(titulo, autor, ano, id_genero):
        livros = Livros.listar()
        for livro in livros:
            if titulo == livro.get_titulo() and autor == livro.get_autor() and ano == livro.get_ano():
                raise ValueError("Livro já cadastrado")
        l = Livro(0, titulo, autor, ano, id_genero)
        Livros.inserir(l)
    @staticmethod
    def livro_listar_id(id):
        return Livros.listar_id(id)
    @staticmethod
    def livro_atualizar(id, titulo, autor, ano, id_genero):
        livros = Livros.listar()
        for livro in livros:
            if titulo == livro.get_titulo() and autor == livro.get_autor() and ano == livro.get_ano():
                raise ValueError("Livro já cadastrado")
        l = Livro(id, titulo, autor, ano, id_genero)
        Livros.atualizar(l)
    @staticmethod
    def livro_excluir(id):
        l = Livro(id, "livro", 0, 0, None)
        Livros.excluir(l)
        
    @staticmethod
    def exemplar_listar():
        return Exemplares.listar()
    @staticmethod
    def exemplar_inserir(edicao, editora, situacao, idLivro, idGenero):
        exemplares = Exemplares.listar()
        for exemplar in exemplares:
            if edicao == exemplar.get_edicao() and editora == exemplar.get_editora() and idLivro == exemplar.get_idLivro():
                raise ValueError("Exemplar já cadastrado")
        ex = Exemplar(0, edicao, editora, situacao, idLivro, idGenero)
        Exemplares.inserir(ex)
    @staticmethod
    def exemplar_listar_id(id):
        return Exemplares.listar_id(id)
    @staticmethod
    def exemplar_atualizar(id, edicao, editora, situacao, idLivro, idGenero):
        exemplares = Exemplares.listar()
        for exemplar in exemplares:
            if edicao == exemplar.get_edicao() and editora == exemplar.get_editora() and idLivro == exemplar.get_idLivro():
                raise ValueError("Exemplar já cadastrado")
        ex = Exemplar(id, edicao, editora, situacao, idLivro, idGenero)
        Exemplar.atualizar(ex)
    @staticmethod
    def exemplar_excluir(id):
        exemplares = Exemplares.listar()
        for exemplar in exemplares:
            if id == exemplar.get_id():
                ex = Exemplar(id, exemplar.get_edicao(), exemplar.get_editora(), exemplar.get_situcao(), exemplar.get_idLivro(), exemplar.get_idGenero())
                Exemplares.excluir(ex)

    @staticmethod
    def emprestimo_listar():
        return Emprestimos.listar()
    @staticmethod
    def emprestimo_inserir(data, dataDevolucao, prazoExtendido, idExemplar, idUsuario):
        emprestimos = Emprestimos.listar()
        for emprestimo in emprestimos:
            if idExemplar == emprestimo.get_idExemplar() and idUsuario == emprestimo.get_idUsuario():
                raise ValueError("Emprestimo já cadastrado")
        em = Emprestimo(0, data, dataDevolucao, prazoExtendido, idExemplar, idUsuario)
        Emprestimos.inserir(em)
    @staticmethod
    def emprestimo_listar_id(id):
        return Emprestimos.listar_id(id)
    @staticmethod
    def emprestimo_atualizar(id, data, dataDevolucao, prazoExtendido, idExemplar, idUsuario):
        emprestimos = Emprestimos.listar()
        for emprestimo in emprestimos:
            if  idExemplar == emprestimo.get_idExemplar() and idUsuario == emprestimo.get_idUsuario():
                raise ValueError("Emprestimo já cadastrado")
        em = Emprestimo(id, data, dataDevolucao, prazoExtendido, idExemplar, idUsuario)
        Emprestimos.atualizar(em)
    @staticmethod
    def emprestimo_excluir(id):
        emprestimos = Emprestimos.listar()
        for emprestimo in emprestimos:
            if id == emprestimo.get_id():
                em = Emprestimo(id, emprestimo.get_data(), emprestimo.get_data_devolucao(), emprestimo.get_prazo_extendido(), emprestimo.get_id_exemplar(), emprestimo.get_id_usuario())
                Emprestimos.excluir(em)