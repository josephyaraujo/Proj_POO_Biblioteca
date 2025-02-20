import streamlit as st
from view.view import View 
import time

class UsuarioLoginUI:
    def main():
        st.header("Entrar no sistema")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password", key="senha_entrar")

        if st.button("Entrar"):
            try:
                usuario = View.usuario_autenticar(email, senha)
                if usuario == None:
                    st.error("E-mail ou senha inválidos")
                else:
                    st.session_state["usuario_id"] = usuario["id"]
                    st.session_state["usuario_nome"] = usuario["nome"]
                    st.session_state["usuario_tipo"] = usuario["tipoUsuario"]
                    time.sleep(2)
                    st.rerun()
            except Exception as erro:
                st.error(erro)
            st.session_state["usuario_email"] = email
            