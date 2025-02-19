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
        u = Usuario(id, "", "", "", "", "")
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
        u = Usuario(id, "", "", "", "", "")
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
        g = Genero(id, "")
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
    def livro_atualizar(id, titulo, autor, ano, id_genero):
        livros = Livros.listar()
        for livro in livros:
            if titulo == livro.get_titulo() and autor == livro.get_autor() and ano == livro.get_ano():
                raise ValueError("Livro já cadastrado")
        l = Livro(id, titulo, autor, ano, id_genero)
        Livros.atualizar(l)
    @staticmethod
    def livro_excluir(id):
        l = Livro(id, "", 0, 0, None)
        Livros.excluir(l)
        
    # @staticmethod
    # def venda_inserir(carrinho, total, id_cliente):
    #     compra = False
    #     for venda in Vendas.listar():
    #         if venda.get_id_cliente() == id_cliente and venda.get_carrinho() == False:  
    #             compra = True
    #             break
    #     if compra == False:
    #         v = Venda(0, None, carrinho, total, id_cliente)
    #         Vendas.inserir(v)
    # @staticmethod
    # def venda_confirmar(id_cliente):
    #     for venda in Vendas.listar():
    #         if venda.get_id_cliente() == id_cliente and venda.get_carrinho() == False:
    #             id = venda.get_id()
    #             data = venda.get_data()
    #             carrinho = True
    #             total = venda.get_total()
    #             id_cliente = venda.get_id_cliente()
    #             v = Venda(id, data, carrinho, total, id_cliente,)
    #             Vendas.atualizar(v)
    #             v = Venda(0, None, False, 0, id_cliente)
    #             Vendas.inserir(v)
    # @staticmethod
    # def venda_listar():
    #     return Vendas.listar()
    # @staticmethod
    # def venda_listar_id(id):
    #     return Vendas.listar_id(id)
    # @staticmethod
    # def venda_atualizar(id, data, carrinho, total, id_cliente):
    #     v = Venda(id, data, carrinho, total, id_cliente)
    #     Vendas.atualizar(v)
    # @staticmethod
    # def venda_excluir(id):
    #     v = Venda(id, "", "", "", "")
    #     Vendas.excluir(v)
    
 
    # @staticmethod
    # def venda_item_listar():
    #     return Venda_itens.listar()
    # @staticmethod
    # def venda_item_listar_id( id):
    #     return Venda_itens.listar_id(id)
    # @staticmethod
    # def venda_item_inserir(q, p, id_venda, id_produto):
    #     v = Venda_item(0, q, p, id_venda, id_produto)
    #     Venda_itens.inserir(v)
    # @staticmethod
    # def venda_item_atualizar(id, q, p, id_venda, id_produto):
    #     v = Venda_item(id, q, p, id_venda, id_produto)
    #     Venda_itens.atualizar(v)
    # @staticmethod
    # def venda_item_excluir(id):
    #     v = Venda_item(id, "", "", "", "")
    #     Venda_itens.excluir(v)

    