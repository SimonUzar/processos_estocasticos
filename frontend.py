import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Análise por Estado", layout="wide")

@st.cache_data
def carregarDados():
    df = pd.read_parquet("arquivos\MICRODADOS_ENEM_2023.parquet")
    return df


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

    
    dados_l = filtrarAgrupar(df, estado_1, 'Q001')
    st.plotly_chart(plotarGrafico(dados_l, 'Q001', estado_1), width='stretch')

    
    dados_2 = filtrarAgrupar(df, estado_2, 'Q001')
    st.plotly_chart(plotarGrafico(dados_2, 'Q001', estado_2), width='stretch')


with abas[1]:
    st.write(f"Pergunta 2 - Formação da mãe, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'Q002')
    st.plotly_chart(plotarGrafico(dados_l, 'Q002', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q002')
    st.plotly_chart(plotarGrafico(dados_2, 'Q002', estado_2), width='stretch')


with abas[2]:
    st.write(f"Pergunta 3 - Idade, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_FAIXA_ETARIA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_FAIXA_ETARIA')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_FAIXA_ETARIA', estado_2), width='stretch')


with abas[3]:
    st.write(f"Pergunta 4 - Sexo, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_SEXO')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_SEXO', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_SEXO')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_SEXO', estado_2), width='stretch')


with abas[4]:
    st.write(f"Pergunta 5 - Estado Civil, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_ESTADO_CIVIL', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ESTADO_CIVIL')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_ESTADO_CIVIL', estado_2), width='stretch')


with abas[5]:
    st.write(f"Pergunta 6 - Tipo de Escola, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_ESCOLA')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_ESCOLA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ESCOLA')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_ESCOLA', estado_2), width='stretch')


with abas[6]:
    st.write(f"Pergunta 7 - Tipo de Estudo, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_ENSINO')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_ENSINO', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_ENSINO')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_ENSINO', estado_2), width='stretch')


with abas[7]:
    st.write(f"Pergunta 8 - Quantidade de membros familiares, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'Q005')
    st.plotly_chart(plotarGrafico(dados_l, 'Q005', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q005')
    st.plotly_chart(plotarGrafico(dados_2, 'Q005', estado_2), width='stretch')


with abas[8]:
    st.write(f"Pergunta 9 - Renda Familiar, influencia?")
    
    dados_l = filtrarAgrupar(df, estado_1, 'Q006')
    st.plotly_chart(plotarGrafico(dados_l, 'Q006', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q006')
    st.plotly_chart(plotarGrafico(dados_2, 'Q006', estado_2), width='stretch')


with abas[9]:
    st.write(f"Pergunta 10 - Treineiros")

    dados_l = filtrarAgrupar(df, estado_1, 'IN_TREINEIRO')
    st.plotly_chart(plotarGrafico(dados_l, 'IN_TREINEIRO', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'IN_TREINEIRO')
    st.plotly_chart(plotarGrafico(dados_2, 'IN_TREINEIRO', estado_2), width='stretch')



with abas[10]:
    st.write(f"Pergunta 11 - Quais matéris tem as maiores notas?")


with abas[11]:
    st.write(f"Pergunta 12 - Língua Estrangeira, qual teve maior desempenho?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_LINGUA')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_LINGUA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_LINGUA')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_LINGUA', estado_2), width='stretch')


with abas[12]:
    st.write(f"Pergunta 13 - Raça, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_COR_RACA')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_COR_RACA', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_COR_RACA')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_COR_RACA', estado_2), width='stretch')


with abas[13]:
    st.write(f"Pergunta 14 - Nacionalidade, influencia?")

    dados_l = filtrarAgrupar(df, estado_1, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGrafico(dados_l, 'TP_NACIONALIDADE', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'TP_NACIONALIDADE')
    st.plotly_chart(plotarGrafico(dados_2, 'TP_NACIONALIDADE', estado_2), width='stretch')


with abas[14]:
    st.write(f"Pergunta 15 - Local da Prova, influencia?")

    # 1. Filtrar apenas o estado de Santa Catarina
    df_sc = df[df['SG_UF_PROVA'] == 'SC'].copy()

    # 2. Agrupar por município para contar candidatos
    df_municipios_sc = df_sc.groupby('NO_MUNICIPIO_PROVA').size().reset_index(name='CANDIDATOS')

    # 3. Ordenar para os municípios com mais candidatos aparecerem primeiro
    df_municipios_sc = df_municipios_sc.sort_values(by='CANDIDATOS', ascending=False)

    # 4. Criar um gráfico de barras (Heatmap de volume)
    fig = px.bar(
        df_municipios_sc.head(20), # Mostra os 20 maiores municípios
        x='CANDIDATOS',
        y='NO_MUNICIPIO_PROVA',
        orientation='h', # Barra horizontal para facilitar leitura dos nomes
        color='CANDIDATOS',
        color_continuous_scale='Reds',
        title='Top 20 Municípios com mais Candidatos em Santa Catarina',
        labels={'NO_MUNICIPIO_PROVA': 'Município', 'CANDIDATOS': 'Total de Inscritos'}
    )

    # Ajustar o layout para que os nomes não fiquem cortados
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    fig.show()

    

with abas[15]:
    st.write(f"Pergunta 16 - Tem televisão?")

    dados_l = filtrarAgrupar(df, estado_1, 'Q019')
    st.plotly_chart(plotarGrafico(dados_l, 'Q019', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q019')
    st.plotly_chart(plotarGrafico(dados_2, 'Q019', estado_2), width='stretch')


with abas[16]:
    st.write(f"Pergunta 17 - Tem computador?")

    dados_l = filtrarAgrupar(df, estado_1, 'Q024')
    st.plotly_chart(plotarGrafico(dados_l, 'Q024', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q024')
    st.plotly_chart(plotarGrafico(dados_2, 'Q024', estado_2), width='stretch')
       

with abas[17]:
    st.write(f"Pergunta 18 - Tem acesso à internet?")

    dados_l = filtrarAgrupar(df, estado_1, 'Q025')
    st.plotly_chart(plotarGrafico(dados_l, 'Q025', estado_1), width='stretch')

    dados_2 = filtrarAgrupar(df, estado_2, 'Q025')
    st.plotly_chart(plotarGrafico(dados_2, 'Q025', estado_2), width='stretch') 


with abas[18]:
    st.write(f"Pergunta 19 - Taxa de abstenção")


with abas[19]:
    st.write(f"Pergunta 20 - Notas na redação")
