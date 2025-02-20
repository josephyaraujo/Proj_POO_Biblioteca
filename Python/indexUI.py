# import json
from models.Livro import Livros, Livro
from models.Genero import Generos, Genero
from models.Usuario import Usuario, Usuarios
from models.EnumUsuarios import EnumUsuarios

import streamlit as st
from templates.manterFuncionarioUI import ManterFuncionarioUI
from templates.manterLivroUI import ManterLivroUI
from templates.manterGeneroUI import ManterGeneroUI
from templates.manterAdminUI import ManterAdminUI
from templates.listarClientesUI import ListarClientesUI
from templates.abrirContaUI import AbrirContaUI
from templates.manterExemplarUI import ManterExemplarUI
from templates.usuarioLoginUI import UsuarioLoginUI
from view.view import View

class IndexUI:
    def menu_visitante():
        UsuarioLoginUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de funcionário", "Cadastro de livros", "Cadastro de gênero", "Clientes cadastrados", "Dados pessoais"])
        if op == "Cadastro de funcionário": ManterFuncionarioUI.main()
        if op == "Cadastro de livros": ManterLivroUI.main()
        if op == "Cadastro de gênero": ManterGeneroUI.main()
        if op == "Clientes cadastrados": ListarClientesUI.main()
        if op == "Dados pessoais": ManterAdminUI.main()

    def menu_funcionario():
        op = st.sidebar.selectbox("Menu", ["Cadastro de exemplar", "Cadastro de empréstimo", "Cadastro de livros","Clientes", "Consultar disponibilidades", "Gerenciar prazos"])
        if op == "Cadastro de exemplar": ManterExemplarUI.main()
        if op == "Cadastro de empréstimo": ManterEmprestimoUI.main()
        if op == "Cadastro de livros": ManterLivroUI.main()
        if op == "Clientes cadastrados": ListarClientesUI.main()
        if op == "Consultar disponibilidades": ManterExemplarUI.exemplar_listar()
        if op == "Gerenciar prazos": ManterEmprestimoUI.emprestimo_atualizar()
        
    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            del st.session_state["usuario_tipo"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_tipo"] == "ADMIN"

            st.sidebar.write("Bem-vindo(a), "+ st.session_state["usuario_nome"])

            if admin:
                IndexUI.menu_admin()
            else:
                IndexUI.menu_funcionario()

            IndexUI.sair_do_sistema()

    def main():
        if not View.admin_listar():
            st.warning("Nenhum administrador cadastrado. Crie uma conta de administrador para continuar.")
            AbrirContaUI.main()
            return
        IndexUI.sidebar()

IndexUI.main()