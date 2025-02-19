import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterAdminUI:
    @staticmethod
    def main():
        st.header("Página pessoal")
        tab1, tab2, tab3 = st.tabs(["Dados", "Atualizar informações", "Excluir conta"])

        with tab1:
            ManterAdminUI.admin_info()
        with tab2:
            ManterAdminUI.admin_atualizar()
        with tab3:
            ManterAdminUI.admin_excluir()

    @classmethod 
    def admin_info(cls):
        admin = View.admin_listar()
        dados_admin = {
            "ID": [admin[0].get_id()],
            "Nome": [admin[0].get_nome()],
            "E-mail": [admin[0].get_email()],
            "Fone": [admin[0].get_fone()]
        }
        df = pd.DataFrame(dados_admin)
        st.dataframe(df, hide_index=True)

    @classmethod 
    def admin_atualizar(cls):
        admin = View.admin_listar()
        nome = st.text_input("Informe o nome", admin[0].get_nome())
        email = st.text_input("Informe o e-mail", admin[0].get_email())
        fone = st.text_input("Informe o fone", admin[0].get_fone())
        senha = st.text_input("Informe a senha", type="password", key="senha_admin")
            
        if st.button("Atualizar"):
            try:
                View.admin_atualizar(admin.get_id(), nome, email, fone, senha, "ADMIN")
                st.success("Informações atualizadas")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
                


    @classmethod 
    def admin_excluir(cls):
        admin = View.admin_listar()
        ManterAdminUI.admin_info()

        if st.button("Excluir conta"):
            View.admin_excluir(admin[0].get_id())
            st.success("Admin excluído")
            time.sleep(2)
            st.rerun()