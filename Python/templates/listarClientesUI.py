import streamlit as st
import pandas as pd
from view.view import View

class ListarClientesUI:
    @staticmethod
    def main():
        st.header("Clientes cadastrados")
        clientes = View.cliente_listar()
        if len(clientes) == 0:
            st.write("Nenhum cliente cadastrado")
        else:
            dic = []
            for obj in clientes: dic.append(obj.__dict__)
            df = pd.DataFrame(dic)
            df.rename(columns={
                '_Usuario__id': "ID",
                '_Usuario__nome':'Nome',
                '_Usuario__email': 'E-mail',
                '_Usuario__fone': 'Fone',
                '_Usuario__senha': 'Senha',
                '_Usuario__tipo_usuario': 'Cargo'
            }, inplace=True)
            st.dataframe(df, hide_index=True)