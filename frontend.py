import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import os
import gdown

st.set_page_config(page_title="Análise por Estado", layout="wide")

url = 'https://drive.google.com/file/d/1ZL20OgcuLn0FX04UdioyF2AbAvuLKpZ6/view?usp=sharing'
output = 'dados_locais.parquet'

@st.cache_resource
def download_data(url, output_path):
    # Verifica se o arquivo já existe para não baixar de novo desnecessariamente
    if not os.path.exists(output_path):
        with st.spinner("Baixando base de dados... Aguarde."):
            gdown.download(url, output_path, quiet=False)
    return output_path

caminho_arquivo = download_data(url, output)

@st.cache_data
def load_dataframe(path):
    return pd.read_parquet(path)


try:
    df = load_dataframe(caminho_arquivo)
except Exception as e:
    st.error(f"Erro ao processar o arquivo: {e}")


# Filtrar dados com base no estado escolhido
def filtrarAgrupar(df, estado_1, estado_2, coluna_x):
    df_filtrado = df[df['SG_UF_PROVA'].isin([estado_1, estado_2])].copy()
    df_filtrado['SG_UF_PROVA'] = df_filtrado['SG_UF_PROVA'].cat.remove_unused_categories()

    df_medias = df_filtrado.groupby(['SG_UF_PROVA', coluna_x])[colunas_notas].mean().reset_index()

    return df_medias
# Filtrar dados com base no estado escolhido


# Criação de gráficos em barra
def plotarGraficoBarras(dados, coluna_x, nota):
    nota_replaced = nota.replace("NU_NOTA_", "")

    fig = px.bar(
        dados,
        x=coluna_x,
        y=nota,
        color='SG_UF_PROVA',
        barmode='group',
        text_auto='.0f',
        labels={
            coluna_x: "", 
            "SG_UF_PROVA": "UF",
            nota: nota_replaced  # Aqui removemos o NU_NOTA_ do eixo Y
        },
        category_orders={"coluna_x": coluna_x},
        color_discrete_sequence=px.colors.qualitative.Prism
    )

    fig.update_layout(height=290)
    
    return fig
# Criação de gráficos em barra


# Criação de gráficos em linha
def plotarGraficoLinhas(dados, estado):
    dados = dados[dados['SG_UF_PROVA'] == estado]
    dados = dados['NU_NOTA_REDACAO'].value_counts().reset_index()
    dados.columns = ['Nota', 'Quantidade']
    dados = dados.sort_values(by='Nota')

    fig = px.line(
        dados,
        x="Nota", 
        y="Quantidade",
        title=f"Quantidade de Alunos por Nota de Redação - {estado}",
        markers=True,
        labels={'Nota': 'Nota da Redação', 'Quantidade': 'Número de Vezes (Frequência)'}
    )

    fig.update_traces(line_shape='spline') # Deixa a linha mais suave/curvada
    fig.update_layout(hovermode="x")

    return fig
# Criação de gráficos em linha


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

with abas[0]:
    st.write(f"Pergunta 1 - Formação do pai, influencia?")
    
    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q001')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q001', 'NU_NOTA_CN'), width='stretch', key="q001_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q001', 'NU_NOTA_CH'), width='stretch', key="q001_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q001', 'NU_NOTA_LC'), width='stretch', key="q001_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q001', 'NU_NOTA_MT'), width='stretch', key="q001_nu_nota_mt")


with abas[1]:
    st.write(f"Pergunta 2 - Formação da mãe, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q002')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q002', 'NU_NOTA_CN'), width='stretch', key="q002_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q002', 'NU_NOTA_CH'), width='stretch', key="q002_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q002', 'NU_NOTA_LC'), width='stretch', key="q002_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q002', 'NU_NOTA_MT'), width='stretch', key="q002_nu_nota_mt")


with abas[2]:
    st.write(f"Pergunta 3 - Idade, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_FAIXA_ETARIA', 'NU_NOTA_CN'), width='stretch', key="tp_faixa_etaria_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_FAIXA_ETARIA', 'NU_NOTA_CH'), width='stretch', key="tp_faixa_etaria_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_FAIXA_ETARIA', 'NU_NOTA_LC'), width='stretch', key="tp_faixa_etaria_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_FAIXA_ETARIA', 'NU_NOTA_MT'), width='stretch', key="tp_faixa_etaria_nu_nota_mt")


with abas[3]:
    st.write(f"Pergunta 4 - Sexo, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_SEXO')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_SEXO', 'NU_NOTA_CN'), width='stretch', key="tp_sexo_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_SEXO', 'NU_NOTA_CH'), width='stretch', key="tp_sexo_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_SEXO', 'NU_NOTA_LC'), width='stretch', key="tp_sexo_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_SEXO', 'NU_NOTA_MT'), width='stretch', key="tp_sexo_nu_nota_mt")


with abas[4]:
    st.write(f"Pergunta 5 - Estado Civil, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESTADO_CIVIL', 'NU_NOTA_CN'), width='stretch', key="tp_estado_civil_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESTADO_CIVIL', 'NU_NOTA_CH'), width='stretch', key="tp_estado_civil_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESTADO_CIVIL', 'NU_NOTA_LC'), width='stretch', key="tp_estado_civil_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESTADO_CIVIL', 'NU_NOTA_MT'), width='stretch', key="tp_estado_civil_nu_nota_mt")


with abas[5]:
    st.write(f"Pergunta 6 - Tipo de Escola, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_ESCOLA')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESCOLA', 'NU_NOTA_CN'), width='stretch', key="tp_escola_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESCOLA', 'NU_NOTA_CH'), width='stretch', key="tp_escola_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESCOLA', 'NU_NOTA_LC'), width='stretch', key="tp_escola_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ESCOLA', 'NU_NOTA_MT'), width='stretch', key="tp_escola_nu_nota_mt")


with abas[6]:
    st.write(f"Pergunta 7 - Tipo de Estudo, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_ENSINO')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ENSINO', 'NU_NOTA_CN'), width='stretch', key="tp_ensino_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ENSINO', 'NU_NOTA_CH'), width='stretch', key="tp_ensino_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ENSINO', 'NU_NOTA_LC'), width='stretch', key="tp_ensino_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_ENSINO', 'NU_NOTA_MT'), width='stretch', key="tp_ensino_nu_nota_mt")


with abas[7]:
    st.write(f"Pergunta 8 - Quantidade de membros familiares, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q005')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q005', 'NU_NOTA_CN'), width='stretch', key="q005_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q005', 'NU_NOTA_CH'), width='stretch', key="q005_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q005', 'NU_NOTA_LC'), width='stretch', key="q005_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q005', 'NU_NOTA_MT'), width='stretch', key="q005_nu_nota_mt")


with abas[8]:
    st.write(f"Pergunta 9 - Renda Familiar, influencia?")
    
    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q006')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q006', 'NU_NOTA_CN'), width='stretch', key="q006_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q006', 'NU_NOTA_CH'), width='stretch', key="q006_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q006', 'NU_NOTA_LC'), width='stretch', key="q006_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q006', 'NU_NOTA_MT'), width='stretch', key="q006_nu_nota_mt")


with abas[9]:
    st.write(f"Pergunta 10 - Treineiros")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'IN_TREINEIRO')
    st.plotly_chart(plotarGraficoBarras(dados, 'IN_TREINEIRO', 'NU_NOTA_CN'), width='stretch', key="in_treineiro_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'IN_TREINEIRO', 'NU_NOTA_CH'), width='stretch', key="in_treineiro_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'IN_TREINEIRO', 'NU_NOTA_LC'), width='stretch', key="in_treineiro_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'IN_TREINEIRO', 'NU_NOTA_MT'), width='stretch', key="in_treineiro_nu_nota_mt")


with abas[10]:
    st.write(f"Pergunta 11 - Quais matéris tem as maiores notas?")

    # Gráfico 1
    dados_1 = df[df['SG_UF_PROVA'] == estado_1]
    medias = dados_1[colunas_notas].mean().reset_index()
    medias.columns = ['Matéria', 'Nota Média']
    medias = medias.sort_values(by='Nota Média', ascending=True)

    fig = px.bar(
        medias, 
        x='Matéria', 
        y='Nota Média',
        text_auto='.2f',
        color='Matéria',
        title=f"Médias das Notas - {estado_1}"
    )

    fig.update_layout(legend_title_text='Matérias')

    st.plotly_chart(fig, width='stretch', key="media_materia_estado1")
    # Gráfico 1

    
    # Gráfico 2
    dados_2 = df[df['SG_UF_PROVA'] == estado_2]
    medias = dados_2[colunas_notas].mean().reset_index()
    medias.columns = ['Matéria', 'Nota Média']
    medias = medias.sort_values(by='Nota Média', ascending=True)

    fig = px.bar(
        medias, 
        x='Matéria', 
        y='Nota Média',
        text_auto='.2f',
        color='Matéria',
        title=f"Médias das Notas - {estado_2}"
    )

    fig.update_layout(legend_title_text='Matérias')

    st.plotly_chart(fig, width='stretch', key="media_materia_estado2")
    # Gráfico 2


with abas[11]:
    st.write(f"Pergunta 12 - Língua Estrangeira, qual teve maior desempenho?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_LINGUA')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_LINGUA', 'NU_NOTA_CN'), width='stretch', key="tp_lingua_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_LINGUA', 'NU_NOTA_CH'), width='stretch', key="tp_lingua_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_LINGUA', 'NU_NOTA_LC'), width='stretch', key="tp_lingua_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_LINGUA', 'NU_NOTA_MT'), width='stretch', key="tp_lingua_nu_nota_mt")


with abas[12]:
    st.write(f"Pergunta 13 - Raça, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_COR_RACA')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_COR_RACA', 'NU_NOTA_CN'), width='stretch', key="tp_cor_raca_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_COR_RACA', 'NU_NOTA_CH'), width='stretch', key="tp_cor_raca_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_COR_RACA', 'NU_NOTA_LC'), width='stretch', key="tp_cor_raca_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_COR_RACA', 'NU_NOTA_MT'), width='stretch', key="tp_cor_raca_nu_nota_mt")


with abas[13]:
    st.write(f"Pergunta 14 - Nacionalidade, influencia?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_NACIONALIDADE', 'NU_NOTA_CN'), width='stretch', key="tp_nacionalidade_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_NACIONALIDADE', 'NU_NOTA_CH'), width='stretch', key="tp_nacionalidade_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_NACIONALIDADE', 'NU_NOTA_LC'), width='stretch', key="tp_nacionalidade_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'TP_NACIONALIDADE', 'NU_NOTA_MT'), width='stretch', key="tp_nacionalidade_nu_nota_mt")


with abas[14]:
    st.write(f"Pergunta 15 - Melhores munícipios")

    top_n = st.slider("Mostrar quantos municípios?", 5, 50, 15)

    # Gráfico 1
    df_filtrado = df[df['SG_UF_PROVA'] == estado_1]
    df_agrupado = df_filtrado.groupby('NO_MUNICIPIO_PROVA')[colunas_notas].mean()
    df_agrupado['MEDIA_TOTAL'] = df_agrupado.mean(axis=1)

    df_agrupado = df_agrupado.sort_values(by='MEDIA_TOTAL', ascending=False).head(top_n).reset_index()

    df_melted = df_agrupado.melt(
        id_vars='NO_MUNICIPIO_PROVA', 
        value_vars=colunas_notas, 
        var_name='Matéria', 
        value_name='Nota'
    )

    fig = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X('NO_MUNICIPIO_PROVA:N', sort=None, title='Município'),
        y=alt.Y('Nota:Q', title='Média das Notas'),
        color=alt.Color('Matéria:N', title='Matérias'),
        xOffset='Matéria:N'
    ).properties(title= f'Médias por Municípios - {estado_1}', width=700, height=400)

    st.altair_chart(fig, width='stretch', key="municipios_estado1")
    # Gráfico 1


    # Gráfico 2
    df_filtrado = df[df['SG_UF_PROVA'] == estado_2]
    df_agrupado = df_filtrado.groupby('NO_MUNICIPIO_PROVA')[colunas_notas].mean()
    df_agrupado['MEDIA_TOTAL'] = df_agrupado.mean(axis=1)

    df_agrupado = df_agrupado.sort_values(by='MEDIA_TOTAL', ascending=False).head(top_n).reset_index()

    df_melted = df_agrupado.melt(
        id_vars='NO_MUNICIPIO_PROVA', 
        value_vars=colunas_notas, 
        var_name='Matéria', 
        value_name='Nota'
    )

    fig = alt.Chart(df_melted).mark_bar().encode(
        x=alt.X('NO_MUNICIPIO_PROVA:N', sort=None, title='Município'),
        y=alt.Y('Nota:Q', title='Média das Notas'),
        color=alt.Color('Matéria:N', title='Matérias'),
        xOffset='Matéria:N'
    ).properties(title= f'Médias por Municípios - {estado_2}', width=700, height=400)

    st.altair_chart(fig, width='stretch', key="municipios_estado2")
    # Gráfico 2


with abas[15]:
    st.write(f"Pergunta 16 - Tem televisão?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q019')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q019', 'NU_NOTA_CN'), width='stretch', key="q019_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q019', 'NU_NOTA_CH'), width='stretch', key="q019_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q019', 'NU_NOTA_LC'), width='stretch', key="q019_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q019', 'NU_NOTA_MT'), width='stretch', key="q019_nu_nota_mt")


with abas[16]:
    st.write(f"Pergunta 17 - Tem computador?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q024')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q024', 'NU_NOTA_CN'), width='stretch', key="q024_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q024', 'NU_NOTA_CH'), width='stretch', key="q024_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q024', 'NU_NOTA_LC'), width='stretch', key="q024_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q024', 'NU_NOTA_MT'), width='stretch', key="q024_nu_nota_mt")
  

with abas[17]:
    st.write(f"Pergunta 18 - Tem acesso à internet?")

    dados = filtrarAgrupar(df, estado_1, estado_2, 'Q025')
    st.plotly_chart(plotarGraficoBarras(dados, 'Q025', 'NU_NOTA_CN'), width='stretch', key="q025_nu_nota_cn")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q025', 'NU_NOTA_CH'), width='stretch', key="q025_nu_nota_ch")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q025', 'NU_NOTA_LC'), width='stretch', key="q025_nu_nota_lc")
    st.plotly_chart(plotarGraficoBarras(dados, 'Q025', 'NU_NOTA_MT'), width='stretch', key="q025_nu_nota_mt")


with abas[18]:
    st.write(f"Pergunta 19 - Status redação")
    
    # Gráfico 1
    df_estado_1 = df[df['SG_UF_PROVA'] == estado_1]
    dados_1 = df_estado_1['TP_STATUS_REDACAO'].value_counts().reset_index()
    dados_1.columns = ['Status', 'Quantidade']

    fig = px.bar(
        dados_1, 
        x='Status', 
        y='Quantidade',
        title=f'Quantidade de redações por TP_STATUS_REDACAO - {estado_1}',
        color='Status',
        text_auto=True
    )

    st.plotly_chart(fig, width='stretch', key="tp_status_redacao_estado1")
    # Gráfico 1


    # Gráfico 2
    df_estado_2 = df[df['SG_UF_PROVA'] == estado_2]
    dados_2 = df_estado_2['TP_STATUS_REDACAO'].value_counts().reset_index()
    dados_2.columns = ['Status', 'Quantidade']

    fig = px.bar(
        dados_2, 
        x='Status', 
        y='Quantidade',
        title=f'Quantidade de redações por TP_STATUS_REDACAO - {estado_2}',
        color='Status',
        text_auto=True
    )

    st.plotly_chart(fig, width='stretch', key="tp_status_redacao_estado2")
    # Gráfico 2


with abas[19]:
    st.write(f"Pergunta 20 - Notas na redação")

    # Primeiro gráfico
    st.plotly_chart(plotarGraficoLinhas(df, estado_1), width='stretch', key="nu_nota_redacao_estado1") 

    # Segundo Gráfico
    st.plotly_chart(plotarGraficoLinhas(df, estado_2), width='stretch', key="nu_nota_redacao_estado2") 

