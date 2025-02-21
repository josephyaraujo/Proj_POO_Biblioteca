import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterLivroUI:
    @staticmethod
    def main():
        st.header("Gerenciamento de Livros")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterLivroUI.livro_listar()
        with tab2:
            ManterLivroUI.livro_inserir()
        with tab3:
            ManterLivroUI.livro_atualizar()
        with tab4:
            ManterLivroUI.livro_excluir()
        

    @classmethod 
    def livro_inserir(cls):
        titulo = st.text_input("Informe o titulo do livro")
        autor = st.text_input("Informe o autor do livro")
        ano = st.number_input("Informe o ano de lançamento", value = 1900, step = 1)
        generos = View.genero_listar()
        if len(generos) == 0:
            st.warning("Nenhum gênero cadastrado. Cadastre um gênero antes de inserir um livro.")
            return
        else:
            genero = st.selectbox("Selecione o gênero do livro", generos)

        if st.button("Inserir"):
            try:
                View.livro_inserir(titulo, autor, ano, genero.get_id())
                st.success("Livro adicionado na biblioteca")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @staticmethod
    def livro_listar():
        st.header("Livros presente na biblioteca")
        livros = View.livro_listar()
        generos = View.genero_listar()
        if len(livros) == 0:
            st.write("Nenhum livro cadastrado")
        else:
            dic = []
            for livro in livros: 
                nome_genero = next((g.get_descricao() for g in generos if g.get_id() == livro.get_id_genero()), "Desconhecido")

                dic.append({
                    "ID": livro.get_id(),
                    "Título": livro.get_titulo(),
                    "Autor": livro.get_autor(),
                    "Ano": livro.get_ano(),
                    "Gênero": nome_genero
                })

            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @classmethod 
    def livro_atualizar(cls):
        livros = View.livro_listar()
        generos = View.genero_listar()
        if len(livros) == 0:
            st.write("Nenhum livro cadastrado")
        else:
            selecionado = st.selectbox("Atualização de livros", livros)

            titulo = st.text_input("Informe o titulo", selecionado.get_titulo())
            autor = st.text_input("Informe o autor", selecionado.get_autor())
            ano = st.number_input("Informe o ano", value = selecionado.get_ano(), step = 1)
            generos = View.genero_listar()
            genero = st.selectbox("Selecione o gênero do livro", generos, key="livro_atualizar")

            if st.button("Atualizar"):
                try:
                    View.livro_atualizar(selecionado.get_id(), titulo, autor, ano, genero.get_id())
                    st.success("Livro atualizado")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                

    @classmethod 
    def livro_excluir(cls):
        livros = View.livro_listar()
        if (len(livros) == 0):
            st.write("Nenhum livro cadastrado")
        else:
            selecionado = st.selectbox("Exclusão de livro", livros)
       
            if st.button("Excluir"):
                View.livro_excluir(selecionado.get_id())
                st.success("Livro excluído")
                time.sleep(2)
                st.rerun()