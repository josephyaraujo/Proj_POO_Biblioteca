import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterGeneroUI:
    @staticmethod
    def main():
        st.header("Gerenciamento de genero")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterGeneroUI.genero_listar()
        with tab2:
            ManterGeneroUI.genero_inserir()
        with tab3:
            ManterGeneroUI.genero_atualizar()
        with tab4:
            ManterGeneroUI.genero_excluir()
        

    @classmethod 
    def genero_inserir(cls):
        descricao = st.text_input("Informe a descricao do genero")

        if st.button("Inserir"):
            try:
                View.genero_inserir(descricao)
                st.success("Gênero cadastrado")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @classmethod 
    def genero_listar(cls):
        generos = View.genero_listar()
        if len(generos) == 0:
            st.write("Nenhum genero cadastrado")
        else:
            dic = []
            for obj in generos: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            df.rename(columns={
                '_Genero__id': "ID",
                '_Genero__descricao':'Descrição',
            }, inplace=True)
            st.dataframe(df, hide_index=True)

    @classmethod 
    def genero_atualizar(cls):
        generos = View.genero_listar()
        if len(generos) == 0:
            st.write("Nenhum genero cadastrado")
        else:
            selecionado = st.selectbox("Atualização de generos", generos)

            descricao = st.text_input("Informe a descrição", selecionado.get_descricao())

            if st.button("Atualizar"):
                try:
                    View.genero_atualizar(selecionado.get_id(), descricao)
                    st.success("Genero atualizado")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                

    @classmethod 
    def genero_excluir(cls):
        generos = View.genero_listar()
        if (len(generos) == 0):
            st.write("Nenhum genero cadastrado")
        else:
            selecionado = st.selectbox("Exclusão de genero", generos)
       
            if st.button("Excluir"):
                View.genero_excluir(selecionado.get_id())
                st.success("Gênero excluído")
                time.sleep(2)
                st.rerun()