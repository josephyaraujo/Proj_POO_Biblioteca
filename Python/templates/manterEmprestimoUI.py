import streamlit as st
import pandas as pd
from view.view import View
import time
import datetime

class ManterEmprestimoUI:
    @staticmethod
    def main():
        st.header("Gerenciamento de emprestimos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar empréstimos", "Inserir", "Atualizar", "Fechar empréstimo"])

        with tab1:
            ManterEmprestimoUI.emprestimo_listar()
        with tab2:
            ManterEmprestimoUI.emprestimo_inserir()
        with tab3:
            ManterEmprestimoUI.emprestimo_atualizar()
        with tab4:
            ManterEmprestimoUI.emprestimo_excluir()
        

    @classmethod 
    def emprestimo_inserir(cls):
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.warning("Nenhum cliente cadastrado. Cadastre um cliente antes de efetuar um empréstimo.")
            return
        else:
            cliente = st.selectbox("Selecione a conta do cliente", clientes)
        exemplares = View.exemplar_listar()
        if len(exemplares) == 0:
            st.warning("Nenhum exemplar cadastrado. Cadastre um exemplar antes de efetuar um empréstimo.")
            return
        else:
            exemplar = st.selectbox("Selecione o exemplar que o cliente deseja inserir", exemplares)
        data = datetime.datetime.now()
        data_formatada = data.strftime("%d/%m/%Y")
        data_devolucao = st.date_input("Informe a data de encerramento do empréstimo", value = "today")
        data_dev_formatada = data_devolucao.strftime("%d/%m/%Y")
        if st.button("Inserir"):
            try:
                View.emprestimo_inserir(data_formatada, data_dev_formatada, 0, exemplar.get_id(), cliente.get_id())
                st.success("Empréstimo cadastrado")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @staticmethod
    def emprestimo_listar():
        st.header("Emprestimos ativos na biblioteca")
        emprestimos = View.emprestimo_listar()
        exemplares = View.exemplar_listar()
        clientes = View.cliente_listar()
        if len(emprestimos) == 0:
            st.write("Nenhum emprestimo cadastrado")
        else:
            dic = []
            for emprestimo in emprestimos: 
                nome_exemplar = next((e.get_edicao() for e in exemplares if e.get_id() == emprestimo.get_id_exemplar()), "Desconhecido")
                nome_cliente = next((c.get_nome() for c in clientes if c.get_id() == emprestimo.get_id_usuario()), "Desconhecido")

                dic.append({
                    "ID": emprestimo.get_id(),
                    "Data": emprestimo.get_data(),
                    "Data de devolução": emprestimo.get_data_devolucao(),
                    "Dias de prazo extendido": emprestimo.get_prazo_extendido(),
                    "Exemplar": nome_exemplar,
                    "Cliente":nome_cliente
                })

            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    @classmethod 
    def emprestimo_atualizar(cls):
        emprestimos = View.emprestimo_listar()
        exemplares = View.exemplar_listar()
        clientes = View.cliente_listar()
        if len(emprestimos) == 0:
            st.write("Nenhum emprestimo cadastrado")
        else:
            selecionado = st.selectbox("Atualização de emprestimo", emprestimos)
            data_devolucao = st.date_input("Informe a data de devolução", value = "today", key="data_devolucao_atualizar")
            data_dev_formatada = data_devolucao.strftime("%d/%m/%Y")
            exemplares_opcoes = {e.get_edicao(): e for e in exemplares}
            exemplar = st.selectbox("Selecione o exemplar", list(exemplares_opcoes.keys()), 
                                          index=list(exemplares_opcoes.keys()).index(next((e.get_edicao() for e in exemplares if e.get_id() == selecionado.get_id_exemplar()), list(exemplares_opcoes.keys())[0])))
            
            if st.button("Atualizar"):
                try:
                    View.livro_atualizar(selecionado.get_data(), data_dev_formatada, selecionado.get_prazo_extendido(), exemplar.get_id(), selecionado.get_id_usuario())
                    st.success("Empréstimo atualizado")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                

    @classmethod 
    def emprestimo_excluir(cls):
        emprestimos = View.emprestimo_listar()
        if (len(emprestimos) == 0):
            st.write("Nenhum empréstimo cadastrado")
        else:
            selecionado = st.selectbox("Fechamento de empréstimo", emprestimos)
       
            if st.button("Excluir"):
                View.exemplar_excluir(selecionado.get_id())
                st.success("Empréstimo finalizado")
                time.sleep(2)
                st.rerun()