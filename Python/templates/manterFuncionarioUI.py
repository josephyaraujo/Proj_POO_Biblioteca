import streamlit as st
import pandas as pd
from view.view import View
import time

class ManterFuncionarioUI:
    @staticmethod
    def main():
        st.header("Gerenciamento de Funcionários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])

        with tab1:
            ManterFuncionarioUI.funcionario_listar()
        with tab2:
            ManterFuncionarioUI.funcionario_inserir()
        with tab3:
            ManterFuncionarioUI.funcionario_atualizar()
        with tab4:
            ManterFuncionarioUI.funcionario_excluir()
        

    @classmethod 
    def funcionario_inserir(cls):
        nome = st.text_input("Informe o nome", key="nome_funcionario")
        email = st.text_input("Informe o e-mail", key="email_funcionario")
        fone = st.text_input("Informe o fone", key="fone_funcionario")
        senha = st.text_input("Informe a senha", type="password", key="senha_funcionario")

        if st.button("Inserir"):
            try:
                View.funcionario_inserir(nome, email, fone, senha, "FUNCIONARIO")
                st.success("Funcionario adicionado")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @classmethod 
    def funcionario_listar(cls):
        funcionarios = View.funcionario_listar()
        if len(funcionarios) == 0:
            st.write("Nenhum funcionário cadastrado")
        else:
            dic = []
            for obj in funcionarios: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            df.rename(columns={
                '_Usuario__id': "ID",
                '_Usuario__nome':'Nome',
                '_Usuario__email': 'E-mail',
                '_Usuario__fone': 'Fone',
                '_Usuario__senha': 'Senha',
                '_Usuario__tipo_usuario': 'Tipo'
            }, inplace=True)
            st.dataframe(df, hide_index=True)

    @classmethod 
    def funcionario_atualizar(cls):
        funcionarios = View.funcionario_listar()
        if len(funcionarios) == 0:
            st.write("Nenhum funcionário cadastrado")
        else:
            selecionado = st.selectbox("Atualização de funcionários", funcionarios)

            nome = st.text_input("Informe o novo nome", selecionado.get_nome())
            email = st.text_input("Informe o novo e-mail", selecionado.get_email())
            fone = st.text_input("Informe o novo fone", selecionado.get_fone())
            senha = st.text_input("Informe a nova senha", type="password")
            
            if st.button("Atualizar"):
                try:
                    View.funcionario_atualizar(selecionado.get_id(), nome, email, fone, senha)
                    st.success("Informações do funcionário atualizadas")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                


    @classmethod 
    def funcionario_excluir(cls):
        funcionarios = View.funcionario_listar()
        if (len(funcionarios) == 0):
            st.write("Nenhum funcionário cadastrado")
        else:
            selecionado = st.selectbox("Exclusão de funcionário", funcionarios)
       
            if st.button("Excluir"):
                View.funcionario_excluir(selecionado.get_id())
                st.success("Funcionário excluído")
                time.sleep(2)
                st.rerun()