# import json
from models.Livro import Livros, Livro
from models.Genero import Generos, Genero
from models.Usuario import Usuario, Usuarios
from models.EnumUsuarios import EnumUsuarios

import streamlit as st
# from templates.manterClienteUI import ManterClienteUI
# from templates.manterProdutoUI import ManterProdutoUI
# from templates.manterCategoriaUI import ManterCategoriaUI
# from templates.reajustarProdutoUI import ReajustarProduto
# from templates.clienteProdutoUI import ClienteProdutoUI
from templates.abrirContaUI import AbrirContaUI
# from templates.visualizarPedidosUI import VisualizarPedidosUI
from templates.usuarioLoginUI import UsuarioLoginUI
from view.view import View

class IndexUI:
    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no sistema", "Abrir conta"])
        if op == "Entrar no sistema": UsuarioLoginUI.main()
        if op == "Abrir conta": AbrirContaUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de funcionário", "Cadastro de livros", "Cadastro de gênero"])
        if op == "Cadastro de funcionário": ManterFuncionarioUI.main()
        if op == "Cadastro de livros": ManterLivroUI.main()
        if op == "Cadastro de gênero": ManterGeneroUI.main()

    def menu_funcionario():
        op = st.sidebar.selectbox("Menu", ["Cadastro de exemplar", "Cadastro de empréstimo", "Consultar disponibilidades", "Gerenciar prazos", "Cadastro de livros"])
        if op == "Cadastro de exemplar": ManterExemplarUI.exemplar_inserir()
        if op == "Cadastro de empréstimo": ManterEmprestimoUI.emprestimo_inserir()
        if op == "Consultar disponibilidades": ManterExemplarUI.exemplar_listar()
        if op == "Gerenciar prazos": ManterEmprestimoUI.emprestimo_atualizar()
        if op == "Cadastro de livros": ManterLivroUI.livro.inserir()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_tipo_usuario"] == "ADMIN"

            st.sidebar.write("Bem-vindo(a), "+ st.session_state["usuario_nome"])

            if admin:IndexUI.menu_admin()
            else:IndexUI.menu_funcionario()

            IndexUI.sair_do_sistema()

    def main():
        IndexUI.sidebar()

IndexUI.main()