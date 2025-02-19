import streamlit as st
import pandas as pd
from view.view import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir conta no sistema")
        AbrirContaUI.inserir()
    
    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        tipo_usuario = st.selectbox("Qual tipo você deseja cadastrar?",("CLIENTE", "ADMIN", "FUNCIONARIO"),)
        if st.button("Inserir"):
            View.usuario_inserir(nome, email, fone, senha, tipo_usuario)
            st.success("Conta criada")
            time.sleep(2)
            st.rerun