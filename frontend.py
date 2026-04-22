import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise por Estado", layout="wide")

@st.cache_data
def carregarDados():
    # Substitua pelo caminho do seu arquivo .parquet
    df = pd.read_parquet("MICRODADOS_ENEM_2023.parquet")
    return df

# Filtrar dados com base no estado escolhido
def filtrarAgrupar(df, estado, coluna_x):
    df_filtrado = df[df['SG_UF_PROVA'] == estado]

    # Agrupa por Q001 e calcula a média das notas
    df_agrupado = df_filtrado.groupby(coluna_x)[colunas_notas].mean().reset_index()

    # Otimizando formato do df
    df_melted = df_agrupado.melt(id_vars=coluna_x, var_name='Matéria', value_name='Nota Média')
    return df_melted

# --- 3. Função Genérica de Criação de Gráficos ---
def plotarGrafico(dados, coluna_x, titulo_x):
    fig = px.bar(
        dados, 
        x=coluna_x, 
        y='Nota Média', 
        color='Matéria',
        barmode='group',
        title=f"Médias por {coluna_x} - {titulo_x}",
        labels={coluna_x: titulo_x, 'Nota Média': 'Média das Notas'}
    )

    fig.update_layout(legend_title_text='Competências')
    return fig

df = carregarDados()

# Combobox dos estados
col1, col2 = st.columns(2)

with col1:
    estado_1 = st.selectbox("Selecione o primeiro Estado", sorted(df['SG_UF_PROVA'].unique()), key="uf1")

with col2:
    estado_2 = st.selectbox("Selecione o segundo Estado", sorted(df['SG_UF_PROVA'].unique()), index=1, key="uf2")
# Combobox dos estados


# Abas das perguntas
nomes_das_abas = [str(i) for i in range(1, 21)]

abas = st.tabs(nomes_das_abas)
# Abas das perguntas

colunas_notas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT']

col_g1, col_g2 = st.columns(2)

with abas[0]:
    st.write(f"Pergunta 1 - Formação do pai, influencia?")

    
    dados_l = filtrarAgrupar(df, estado_1, 'Q001')
    st.plotly_chart(plotarGrafico(dados_l, 'Q001', estado_1), width='stretch')

    
    dados_2 = filtrarAgrupar(df, estado_2, 'Q001')
    st.plotly_chart(plotarGrafico(dados_2, 'Q001', estado_2), width='stretch')

with abas[1]:
  
