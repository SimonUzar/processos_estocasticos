import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt

st.set_page_config(page_title="Análise por Estado", layout="wide")

@st.cache_data
def carregarDados():
    df = pd.read_parquet(r"arquivos\MICRODADOS_ENEM_2023.parquet")
    return df


# Filtrar dados com base no estado escolhido
def filtrarAgrupar(df, estado, coluna_x):
    df_filtrado = df[df['SG_UF_PROVA'] == estado]

    # Agrupa por média das notas
    df_agrupado = df_filtrado.groupby(coluna_x)[colunas_notas].mean().reset_index()

    # Otimizando formato do df
    df_melted = df_agrupado.melt(id_vars=coluna_x, var_name='Matéria', value_name='Nota Média')
    return df_melted
# Filtrar dados com base no estado escolhido


# Criação de gráficos em barra
def plotarGraficoBarras(dados, coluna_x, titulo_x):
    fig = px.bar(
        dados, 
        x=coluna_x, 
        y='Nota Média', 
        color='Matéria',
        barmode='group',
        title=f"Médias por {coluna_x} - {titulo_x}",
        labels={coluna_x: titulo_x, 'Nota Média': 'Média das Notas'}
    )

    fig.update_layout(legend_title_text='Matérias')
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

    dados_1 = filtrarAgrupar(df, estado_1, 'Q001')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q001', estado_1), width='stretch', key="q001_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q001')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q001', estado_2), width='stretch', key="q001_estado2")


with abas[1]:
    st.write(f"Pergunta 2 - Formação da mãe, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q002')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q002', estado_1), width='stretch', key="q002_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q002')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q002', estado_2), width='stretch', key="q002_estado2")


with abas[2]:
    st.write(f"Pergunta 3 - Idade, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_FAIXA_ETARIA', estado_1), width='stretch', key="tp_faixa_etaria_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_FAIXA_ETARIA', estado_2), width='stretch', key="tp_faixa_etaria_estado2")


with abas[3]:
    st.write(f"Pergunta 4 - Sexo, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_SEXO')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_SEXO', estado_1), width='stretch', key="tp_sexo_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_SEXO')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_SEXO', estado_2), width='stretch', key="tp_sexo_estado2")


with abas[4]:
    st.write(f"Pergunta 5 - Estado Civil, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_ESTADO_CIVIL', estado_1), width='stretch', key="tp_estado_civil_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_ESTADO_CIVIL', estado_2), width='stretch', key="tp_estado_civil_estado2")


with abas[5]:
    st.write(f"Pergunta 6 - Tipo de Escola, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_ESCOLA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_ESCOLA', estado_1), width='stretch', key="tp_escola_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ESCOLA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_ESCOLA', estado_2), width='stretch', key="tp_escola_estado2")


with abas[6]:
    st.write(f"Pergunta 7 - Tipo de Estudo, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_ENSINO')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_ENSINO', estado_1), width='stretch', key="tp_ensino_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ENSINO')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_ENSINO', estado_2), width='stretch', key="tp_ensino_estado2")


with abas[7]:
    st.write(f"Pergunta 8 - Quantidade de membros familiares, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q005')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q005', estado_1), width='stretch', key="q005_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q005')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q005', estado_2), width='stretch', key="q005_estado2")


with abas[8]:
    st.write(f"Pergunta 9 - Renda Familiar, influencia?")
    
    dados_1 = filtrarAgrupar(df, estado_1, 'Q006')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q006', estado_1), width='stretch', key="q006_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q006')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q006', estado_2), width='stretch', key="q006_estado2")


with abas[9]:
    st.write(f"Pergunta 10 - Treineiros")

    dados_1 = filtrarAgrupar(df, estado_1, 'IN_TREINEIRO')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'IN_TREINEIRO', estado_1), width='stretch', key="in_treineiro_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'IN_TREINEIRO')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'IN_TREINEIRO', estado_2), width='stretch', key="in_treineiro_estado2")



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

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_LINGUA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_LINGUA', estado_1), width='stretch', key="tp_lingua_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_LINGUA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_LINGUA', estado_2), width='stretch', key="tp_lingua_estado2")


with abas[12]:
    st.write(f"Pergunta 13 - Raça, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_COR_RACA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_COR_RACA', estado_1), width='stretch', key="tp_cor_raca_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_COR_RACA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_COR_RACA', estado_2), width='stretch', key="tp_cor_raca_estado2")


with abas[13]:
    st.write(f"Pergunta 14 - Nacionalidade, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_NACIONALIDADE', estado_1), width='stretch', key="tp_nacionalidade_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_NACIONALIDADE', estado_2), width='stretch', key="tp_nacionalidade_estado2")


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

    dados_1 = filtrarAgrupar(df, estado_1, 'Q019')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q019', estado_1), width='stretch', key="q019_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q019')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q019', estado_2), width='stretch', key="q019_estado2")


with abas[16]:
    st.write(f"Pergunta 17 - Tem computador?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q024')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q024', estado_1), width='stretch', key="q024_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q024')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q024', estado_2), width='stretch', key="q024_estado2")
       

with abas[17]:
    st.write(f"Pergunta 18 - Tem acesso à internet?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q025')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q025', estado_1), width='stretch', key="q025_estado1")

    dados_2 = filtrarAgrupar(df, estado_2, 'Q025')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q025', estado_2), width='stretch', key="q025_estado2") 


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

