import streamlit as st
from templates.manterFuncionarioUI import ManterFuncionarioUI
from templates.manterLivroUI import ManterLivroUI
from templates.manterGeneroUI import ManterGeneroUI
from templates.manterAdminUI import ManterAdminUI
from templates.listarClientesUI import ListarClientesUI
from templates.abrirContaUI import AbrirContaUI
from templates.manterExemplarUI import ManterExemplarUI
from templates.manterEmprestimoUI import ManterEmprestimoUI
from templates.usuarioLoginUI import UsuarioLoginUI
from view.view import View

class IndexUI:
    def menu_visitante():
        UsuarioLoginUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Gerenciamento de funcionários", "Gerenciamento de livros", "Gerenciamento de gênero", "Clientes cadastrados", "Dados pessoais"])
        if op == "Gerenciamento de funcionários": ManterFuncionarioUI.main()
        if op == "Gerenciamento de livros": ManterLivroUI.main()
        if op == "Gerenciamento de gênero": ManterGeneroUI.main()
        if op == "Clientes cadastrados": ListarClientesUI.main()
        if op == "Dados pessoais": ManterAdminUI.main()

    def menu_funcionario():
        op = st.sidebar.selectbox("Menu", ["Gerenciamento de exemplares", "Gerenciamento de empréstimos", "Gerenciamento de livros","Clientes cadastrados", "Consultar disponibilidades"])
        if op == "Gerenciamento de exemplares": ManterExemplarUI.main()
        if op == "Gerenciamento de empréstimos": ManterEmprestimoUI.main()
        if op == "Gerenciamento de livros": ManterLivroUI.main()
        if op == "Clientes cadastrados": ListarClientesUI.main()
        if op == "Consultar disponibilidades": ManterExemplarUI.exemplar_listar()
        
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