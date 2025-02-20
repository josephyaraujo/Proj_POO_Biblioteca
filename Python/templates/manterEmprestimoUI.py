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
        
        emprestimos_ativos = [e for e in View.emprestimo_listar() if e.get_id_usuario() == cliente.get_id() and e.get_data_devolucao() >= datetime.datetime.now().strftime("%d/%m/%Y")]
        if len(emprestimos_ativos) >= 3:
            st.warning("Este cliente já possui 3 empréstimos ativos. Não é possível realizar um novo empréstimo.")
            return
    
        exemplares = View.exemplar_listar()
        exemplares_disponiveis = [e for e in exemplares if e.get_situacao() is True]

        if len(exemplares_disponiveis) == 0:
            st.warning("Nenhum exemplar disponível para empréstimo.")
            return
        else:
            exemplar = st.selectbox("Selecione o exemplar que o cliente deseja inserir", exemplares_disponiveis)

        data = datetime.datetime.now()
        data_formatada = data.strftime("%d/%m/%Y")
        data_devolucao = st.date_input("Informe a data de encerramento do empréstimo", value = "today")
        data_dev_formatada = data_devolucao.strftime("%d/%m/%Y")

        if st.button("Confirmar empréstimo"):
            try:
                View.emprestimo_inserir(data_formatada, data_dev_formatada, 0, exemplar.get_id(), cliente.get_id())
                View.exemplar_atualizar(exemplar.get_id(), exemplar.get_edicao(), exemplar.get_editora(), False, exemplar.get_id_livro(), exemplar.get_id_genero())
                st.success("Empréstimo cadastrado")
                time.sleep(2)
                st.rerun()
            except Exception as erro:
                st.error(erro)
            

    @staticmethod
    def emprestimo_listar():
        st.header("Empréstimos ativos na biblioteca")
        emprestimos = View.emprestimo_listar()
        exemplares = View.exemplar_listar()
        clientes = View.cliente_listar()
        livros = View.livro_listar()
        if len(emprestimos) == 0:
            st.write("Nenhum empréstimo cadastrado.")
        else:
            dic = []
            for emprestimo in emprestimos: 
                exemplar = View.exemplar_listar_id(emprestimo.get_id_exemplar())
                livro = next((l.get_titulo() for l in livros if l.get_id() == exemplar.get_id_livro()), "Desconhecido")
                nome_exemplar = next((e.get_edicao() for e in exemplares if e.get_id() == emprestimo.get_id_exemplar()), "Desconhecido")
                nome_cliente = next((c.get_nome() for c in clientes if c.get_id() == emprestimo.get_id_usuario()), "Desconhecido")

                dic.append({
                    "ID": emprestimo.get_id(),
                    "Data": emprestimo.get_data(),
                    "Data de devolução": emprestimo.get_data_devolucao(),
                    "Dias de prazo extendido": emprestimo.get_prazo_extendido(),
                    "Exemplar": f"{livro} (Edição {nome_exemplar})",
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
            
            if st.button("Atualizar"):
                try:
                    View.livro_atualizar(selecionado.get_data(), data_dev_formatada, selecionado.get_prazo_extendido(), selecionado.get_id_exemplar(), selecionado.get_id_usuario())
                    st.success("Empréstimo atualizado")
                    time.sleep(2)
                    st.rerun()
                except Exception as erro:
                    st.error(erro)
                

    @classmethod 
    def emprestimo_excluir(cls):
        emprestimos = View.emprestimo_listar()
        exemplares = View.exemplar_listar()
        if (len(emprestimos) == 0):
            st.write("Nenhum empréstimo cadastrado")
        else:
            selecionado = st.selectbox("Fechamento de empréstimo", emprestimos)
       
            if st.button("Fechar"):
                exemplar = View.exemplar_listar_id(selecionado.get_id_exemplar())
                View.exemplar_excluir(selecionado.get_id())
                View.exemplar_atualizar(exemplar.get_id(), exemplar.get_edicao(), exemplar.get_editora(), True, exemplar.get_id_livro(), exemplar.get_id_genero())
                st.success("Empréstimo finalizado")
                time.sleep(2)
                st.rerun()