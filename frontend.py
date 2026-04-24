import streamlit as st
import pandas as pd
import plotly.express as px
import json
import requests

st.set_page_config(page_title="Análise por Estado", layout="wide")

@st.cache_data
def carregarDados():
    df = pd.read_parquet("arquivos\MICRODADOS_ENEM_2023.parquet")
    return df


@st.cache_data
def carregarFaltantes():
    df = pd.read_parquet("arquivos\MICRODADOS_ENEM_FALTANTES_2023.parquet")
    return df


# Filtrar dados com base no estado escolhido
def filtrarAgrupar(df, estado, coluna_x):
    df_filtrado = df[df['SG_UF_PROVA'] == estado]

    # Agrupa por Q001 e calcula a média das notas
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

    fig.update_layout(legend_title_text='Competências')
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
df_faltantes = carregarFaltantes()

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
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q001', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q001')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q001', estado_2), width='stretch')


with abas[1]:
    st.write(f"Pergunta 2 - Formação da mãe, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q002')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q002', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q002')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q002', estado_2), width='stretch')


with abas[2]:
    st.write(f"Pergunta 3 - Idade, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_FAIXA_ETARIA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_FAIXA_ETARIA', estado_2), width='stretch')


with abas[3]:
    st.write(f"Pergunta 4 - Sexo, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_SEXO')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_SEXO', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_SEXO')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_SEXO', estado_2), width='stretch')


with abas[4]:
    st.write(f"Pergunta 5 - Estado Civil, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_ESTADO_CIVIL', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_ESTADO_CIVIL', estado_2), width='stretch')


with abas[5]:
    st.write(f"Pergunta 6 - Tipo de Escola, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_ESCOLA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_ESCOLA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ESCOLA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_ESCOLA', estado_2), width='stretch')


with abas[6]:
    st.write(f"Pergunta 7 - Tipo de Estudo, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_ENSINO')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_ENSINO', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ENSINO')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_ENSINO', estado_2), width='stretch')


with abas[7]:
    st.write(f"Pergunta 8 - Quantidade de membros familiares, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q005')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q005', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q005')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q005', estado_2), width='stretch')


with abas[8]:
    st.write(f"Pergunta 9 - Renda Familiar, influencia?")
    
    dados_1 = filtrarAgrupar(df, estado_1, 'Q006')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q006', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q006')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q006', estado_2), width='stretch')


with abas[9]:
    st.write(f"Pergunta 10 - Treineiros")

    dados_1 = filtrarAgrupar(df, estado_1, 'IN_TREINEIRO')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'IN_TREINEIRO', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'IN_TREINEIRO')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'IN_TREINEIRO', estado_2), width='stretch')



with abas[10]:
    st.write(f"Pergunta 11 - Quais matéris tem as maiores notas?")


with abas[11]:
    st.write(f"Pergunta 12 - Língua Estrangeira, qual teve maior desempenho?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_LINGUA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_LINGUA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_LINGUA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_LINGUA', estado_2), width='stretch')


with abas[12]:
    st.write(f"Pergunta 13 - Raça, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_COR_RACA')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_COR_RACA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_COR_RACA')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_COR_RACA', estado_2), width='stretch')


with abas[13]:
    st.write(f"Pergunta 14 - Nacionalidade, influencia?")

    dados_1 = filtrarAgrupar(df, estado_1, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'TP_NACIONALIDADE', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'TP_NACIONALIDADE', estado_2), width='stretch')


with abas[14]:
    
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    response = requests.get(url)
    geojson_completo = response.json()

    features_sc = [
        f for f in geojson_completo['features'] 
        if f['properties'].get('sigla') == 'SC'
    ]

    geojson_sc = {
        "type": "FeatureCollection",
        "features": features_sc
    }

    df_teste = pd.DataFrame({
        'SG_UF_PROVA': ['SC'],
        'NOTA': [700]  
    })

    fig = px.choropleth(
        df_teste,
        geojson=geojson_sc,
        locations="SG_UF_PROVA",
        featureidkey="properties.sigla",
        color="NOTA",
        scope="south america",
        title="Foco em Santa Catarina"
    )

    # Ajusta o zoom automaticamente para a única geometria presente (SC)
    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(margin={"r":0,"t":50,"l":0,"b":0})

    st.plotly_chart(fig, use_container_width=True)

    

with abas[15]:
    st.write(f"Pergunta 16 - Tem televisão?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q019')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q019', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q019')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q019', estado_2), width='stretch')


with abas[16]:
    st.write(f"Pergunta 17 - Tem computador?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q024')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q024', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q024')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q024', estado_2), width='stretch')
       

with abas[17]:
    st.write(f"Pergunta 18 - Tem acesso à internet?")

    dados_1 = filtrarAgrupar(df, estado_1, 'Q025')
    st.plotly_chart(plotarGraficoBarras(dados_1, 'Q025', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q025')
    st.plotly_chart(plotarGraficoBarras(dados_2, 'Q025', estado_2), width='stretch') 


with abas[18]:
    st.write(f"Pergunta 19 - Taxa de abstenção")


with abas[19]:
    st.write(f"Pergunta 20 - Notas na redação")

    # Primeiro gráfico
    st.plotly_chart(plotarGraficoLinhas(df, estado_1), width='stretch') 

    # Segundo Gráfico
    st.plotly_chart(plotarGraficoLinhas(df, estado_2), width='stretch') 

