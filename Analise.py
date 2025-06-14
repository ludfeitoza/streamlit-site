

# Importando as bibliotecas
import pandas as pd
import streamlit as st
import plotly.express as px


st.set_page_config(page_title='Analise de produtos',layout='wide')

# Mostrar na tela o botão que pede o arquivo
arquivo = st.file_uploader("Por favor anexe a tabela de produtos",type=['xlsx'])

if arquivo == None:
    st.write("Anexe o arquivo por favor!")
else:
    # Ler os dados
    # df = pd.read_excel('Produtos.xlsx') # Arquivo fixo
    
    df = pd.read_excel(arquivo) # Permite o usuário subir o arquivo
    
    # Filtro de dados
    colFiltro1, colFiltro2 = st.columns(2)
    maisPesado = df['Peso_Kg'].max()
    
    with colFiltro1:
        minino = st.number_input(label="Minimo",min_value=0,max_value=int(maisPesado))
    
    with colFiltro2:
        maximo = st.number_input(label="Maximo",min_value=0,max_value=int(maisPesado))
    
    # Previa dos dados
    filtrado = df[ (df['Peso_Kg'] > minino) & (df['Peso_Kg'] < maximo) ]
    
    

    # Salvar as metricas em variaveis
    quantidade_produtos = len(filtrado)
    total_kg = filtrado['Peso_Kg'].sum()
    media_kg = filtrado['Peso_Kg'].mean()


    # Fazer o agrupamento por Categoria e contar o id_produto
    produto_categoria = filtrado.groupby('Categoria')["ID_Produto"].count().reset_index()



    # Exibir o titulo da pagina
    st.title("Produtos em estoque")
    
    st.dataframe(filtrado)  
  

    # Exibir as métricas
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de produtos",quantidade_produtos)

    col2.metric("Total do estoque em kg",total_kg)

    col3.metric("Media de peso do produto",media_kg)

    # Exibir o grafico
    st.bar_chart(data=produto_categoria,x='Categoria',y='ID_Produto')