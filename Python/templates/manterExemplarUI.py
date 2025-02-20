import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterExemplarUI:
    @staticmethod
    def main():
        st.header("Gerenciamento de exemplares")
        tab1, tab2, tab3 = st.tabs(["Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterExemplarUI.exemplar_inserir()
        with tab2:
            ManterExemplarUI.exemplar_atualizar()
        with tab3:
            ManterExemplarUI.exemplar_excluir()
        

    @classmethod 
    def exemplar_inserir(cls):
        edicao = st.number_input("Informe a edicao do exemplar", value = 0, step = 1)
        editora = st.text_input("Informe a editora do exemplar")
        situacao = st.selectbox("Informe a situação", options=["Disponível", "Indisponível"])
        situacao_booleano = True if situacao == "Disponível" else False
        livros = View.livro_listar()
        if len(livros) == 0:
            st.warning("Nenhum livro cadastrado. Cadastre um livro antes de inserir um exemplar.")
            return
        else:
            livro = st.selectbox("Selecione o livro do exemplar que você deseja inserir", livros)
        
        if st.button("Inserir"):
            try:
                View.exemplar_inserir(edicao, editora, situacao_booleano, livro.get_id(), livro.get_id_genero())
                st.success("Exemplar adicionado na biblioteca")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @staticmethod
    def exemplar_listar():
        st.header("Exemplares presentes na biblioteca")
        exemplares = View.exemplar_listar()
        livros = View.livro_listar()
        generos = View.genero_listar()
        if len(exemplares) == 0:
            st.write("Nenhum exemplar cadastrado")
        else:
            dic = []
            for exemplar in exemplares: 
                nome_livro = next((l.get_titulo() for l in livros if l.get_id() == exemplar.get_id_livro()), "Desconhecido")
                nome_genero = next((g.get_descricao() for g in generos if g.get_id() == exemplar.get_id_genero()), "Desconhecido")

                dic.append({
                    "ID": exemplar.get_id(),
                    "Edicao": exemplar.get_edicao(),
                    "Editora": exemplar.get_editora(),
                    "Situacao": "Disponível" if exemplar.get_situacao() else "Emprestado",
                    "Livro": nome_livro,
                    "Gênero":nome_genero
                })

            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @classmethod 
    def exemplar_atualizar(cls):
        exemplares = View.exemplar_listar()
        livros = View.livro_listar()
        if len(exemplares) == 0:
            st.write("Nenhum exemplar cadastrado")
        else:
            selecionado = st.selectbox("Atualização de exemplar", exemplares)

            edicao = st.number_input("Informe a edição", selecionado.get_edicao(), key="edicao_atualizar")
            editora = st.text_input("Informe a editora", selecionado.get_editora(), key="editora_atualizar")
            situacao = st.selectbox("Informe a situação", options=["Disponível", "Indisponível"], key="situacao_atualizar")
            situacao_booleano = True if situacao == "Disponível" else False
            livro_opcoes = {l.get_titulo(): l for l in livros}
            livro = st.selectbox("Selecione o livro do exemplar", list(livro_opcoes.keys()), 
                                          index=list(livro_opcoes.keys()).index(next((l.get_titulo() for l in livros if l.get_id() == selecionado.get_id_livro()), list(livro_opcoes.keys())[0])))

            if st.button("Atualizar informações"):
                try:
                    View.exemplar_atualizar(selecionado.get_id(), edicao, editora, situacao_booleano, livro.get_id(), livro.get_id_genero())
                    st.success("Exemplar atualizado")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                

    @classmethod 
    def exemplar_excluir(cls):
        exemplares = View.exemplar_listar()
        if (len(exemplares) == 0):
            st.write("Nenhum exemplar cadastrado")
        else:
            selecionado = st.selectbox("Exclusão de exemplar", exemplares)
       
            if st.button("Excluir"):
                View.exemplar_excluir(selecionado.get_id())
                st.success("Exemplar excluído")
                time.sleep(2)
                st.rerun()