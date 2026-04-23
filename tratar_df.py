import pandas as pd

df_csv = pd.read_csv(r"arquivos\MICRODADOS_ENEM_2023.csv", encoding='latin1', sep=';')
df_csv.to_parquet(r"arquivos\MICRODADOS_ENEM_2023.parquet", index=False)

df_parquet = pd.read_parquet(r"arquivos\MICRODADOS_ENEM_2023.parquet")

def transformarColunas():
    # Nessa função iremos alterar o tamanho das colunas, otimizando o consumo de armazenamento e velocidade de busca

    global df_parquet

    df_parquet['NU_INSCRICAO'] = df_parquet['NU_INSCRICAO'].astype('Int64')
    df_parquet['NU_ANO'] = df_parquet['NU_ANO'].astype('Int16')
    df_parquet['TP_FAIXA_ETARIA'] = df_parquet['TP_FAIXA_ETARIA'].astype('Int16')
    df_parquet['TP_SEXO'] = df_parquet['TP_SEXO'].astype('category')
    df_parquet['TP_ESTADO_CIVIL'] = df_parquet['TP_ESTADO_CIVIL'].astype('Int8')
    df_parquet['TP_COR_RACA'] = df_parquet['TP_COR_RACA'].astype('Int8')
    df_parquet['TP_NACIONALIDADE'] = df_parquet['TP_NACIONALIDADE'].astype('Int8')
    df_parquet['TP_ST_CONCLUSAO'] = df_parquet['TP_ST_CONCLUSAO'].astype('Int8')
    df_parquet['TP_ANO_CONCLUIU'] = df_parquet['TP_ANO_CONCLUIU'].astype('Int8')
    df_parquet['TP_ESCOLA'] = df_parquet['TP_ESCOLA'].astype('Int8')
    df_parquet['TP_ENSINO'] = df_parquet['TP_ENSINO'].astype('Int8')
    df_parquet['IN_TREINEIRO'] = df_parquet['IN_TREINEIRO'].astype('bool')
    df_parquet['CO_MUNICIPIO_ESC'] = df_parquet['CO_MUNICIPIO_ESC'].astype('Int32')
    df_parquet['NO_MUNICIPIO_ESC'] = df_parquet['NO_MUNICIPIO_ESC'].astype('category')
    df_parquet['CO_UF_ESC'] = df_parquet['CO_UF_ESC'].astype('Int8')
    df_parquet['SG_UF_ESC'] = df_parquet['SG_UF_ESC'].astype('category')
    df_parquet['TP_DEPENDENCIA_ADM_ESC'] = df_parquet['TP_DEPENDENCIA_ADM_ESC'].astype('Int8')
    df_parquet['TP_LOCALIZACAO_ESC'] = df_parquet['TP_LOCALIZACAO_ESC'].astype('Int8')
    df_parquet['TP_SIT_FUNC_ESC'] = df_parquet['TP_SIT_FUNC_ESC'].astype('Int8')
    df_parquet['CO_MUNICIPIO_PROVA'] = df_parquet['CO_MUNICIPIO_PROVA'].astype('Int32')
    df_parquet['NO_MUNICIPIO_PROVA'] = df_parquet['NO_MUNICIPIO_PROVA'].astype('category')
    df_parquet['CO_UF_PROVA'] = df_parquet['CO_UF_PROVA'].astype('Int8')
    df_parquet['SG_UF_PROVA'] = df_parquet['SG_UF_PROVA'].astype('category')
    df_parquet['TP_PRESENCA_CN'] = df_parquet['TP_PRESENCA_CN'].astype('Int8')
    df_parquet['TP_PRESENCA_CH'] = df_parquet['TP_PRESENCA_CH'].astype('Int8')
    df_parquet['TP_PRESENCA_LC'] = df_parquet['TP_PRESENCA_LC'].astype('Int8')
    df_parquet['TP_PRESENCA_MT'] = df_parquet['TP_PRESENCA_MT'].astype('Int8')
    df_parquet['CO_PROVA_CN'] = df_parquet['CO_PROVA_CN'].astype('Int16')
    df_parquet['CO_PROVA_CH'] = df_parquet['CO_PROVA_CH'].astype('Int16')
    df_parquet['CO_PROVA_LC'] = df_parquet['CO_PROVA_LC'].astype('Int16')
    df_parquet['CO_PROVA_MT'] = df_parquet['CO_PROVA_MT'].astype('Int16')
    df_parquet['NU_NOTA_CN'] = df_parquet['NU_NOTA_CN'].astype('float16')
    df_parquet['NU_NOTA_CH'] = df_parquet['NU_NOTA_CH'].astype('float16')
    df_parquet['NU_NOTA_LC'] = df_parquet['NU_NOTA_LC'].astype('float16')
    df_parquet['NU_NOTA_MT'] = df_parquet['NU_NOTA_MT'].astype('float16')
    df_parquet['TX_RESPOSTAS_CN'] = df_parquet['TX_RESPOSTAS_CN'].astype('category')
    df_parquet['TX_RESPOSTAS_CH'] = df_parquet['TX_RESPOSTAS_CH'].astype('category')
    df_parquet['TX_RESPOSTAS_LC'] = df_parquet['TX_RESPOSTAS_LC'].astype('category')
    df_parquet['TX_RESPOSTAS_MT'] = df_parquet['TX_RESPOSTAS_MT'].astype('category')
    df_parquet['TP_LINGUA'] = df_parquet['TP_LINGUA'].astype('Int8')
    df_parquet['TX_GABARITO_CN'] = df_parquet['TX_GABARITO_CN'].astype('category')
    df_parquet['TX_GABARITO_CH'] = df_parquet['TX_GABARITO_CH'].astype('category')
    df_parquet['TX_GABARITO_LC'] = df_parquet['TX_GABARITO_LC'].astype('category')
    df_parquet['TX_GABARITO_MT'] = df_parquet['TX_GABARITO_MT'].astype('category')
    df_parquet['TP_STATUS_REDACAO'] = df_parquet['TP_STATUS_REDACAO'].astype('Int8')
    df_parquet['NU_NOTA_COMP1'] = df_parquet['NU_NOTA_COMP1'].astype('Int16')
    df_parquet['NU_NOTA_COMP2'] = df_parquet['NU_NOTA_COMP2'].astype('Int16')
    df_parquet['NU_NOTA_COMP3'] = df_parquet['NU_NOTA_COMP3'].astype('Int16')
    df_parquet['NU_NOTA_COMP4'] = df_parquet['NU_NOTA_COMP4'].astype('Int16')
    df_parquet['NU_NOTA_COMP5'] = df_parquet['NU_NOTA_COMP5'].astype('Int16')
    df_parquet['NU_NOTA_REDACAO'] = df_parquet['NU_NOTA_REDACAO'].astype('Int16')
    df_parquet['Q001'] = df_parquet['Q001'].astype('category')
    df_parquet['Q002'] = df_parquet['Q002'].astype('category')
    df_parquet['Q003'] = df_parquet['Q003'].astype('category')
    df_parquet['Q004'] = df_parquet['Q004'].astype('category')
    df_parquet['Q005'] = df_parquet['Q005'].astype('Int8')
    df_parquet['Q006'] = df_parquet['Q006'].astype('category')
    df_parquet['Q007'] = df_parquet['Q007'].astype('category')
    df_parquet['Q008'] = df_parquet['Q008'].astype('category')
    df_parquet['Q009'] = df_parquet['Q009'].astype('category')
    df_parquet['Q010'] = df_parquet['Q010'].astype('category')
    df_parquet['Q011'] = df_parquet['Q011'].astype('category')
    df_parquet['Q012'] = df_parquet['Q012'].astype('category')
    df_parquet['Q013'] = df_parquet['Q013'].astype('category')
    df_parquet['Q014'] = df_parquet['Q014'].astype('category')
    df_parquet['Q015'] = df_parquet['Q015'].astype('category')
    df_parquet['Q016'] = df_parquet['Q016'].astype('category')
    df_parquet['Q017'] = df_parquet['Q017'].astype('category')
    df_parquet['Q018'] = df_parquet['Q018'].astype('category')
    df_parquet['Q019'] = df_parquet['Q019'].astype('category')
    df_parquet['Q020'] = df_parquet['Q020'].astype('category')
    df_parquet['Q021'] = df_parquet['Q021'].astype('category')
    df_parquet['Q022'] = df_parquet['Q022'].astype('category')
    df_parquet['Q023'] = df_parquet['Q023'].astype('category')
    df_parquet['Q024'] = df_parquet['Q024'].astype('category')
    df_parquet['Q025'] = df_parquet['Q025'].astype('category')


def validarColunas():
    # Nessa função vamos validar se as colunas estão dentro dos seus respectivos valores
    # Caso o registro não cumpra os requisitos, o mesmo é removido
    # Seguindo o arquivos MICRODADOS_ENEM_DICIONARIO.csv
    # Estaremos validando apenas as colunas que foram utilizadas na análise   

    global df_parquet

    # Remove na coluna 'NU_INSCRICAO' valores duplicados
    df_parquet = df_parquet[~df_parquet.duplicated(subset=['NU_INSCRICAO'], keep=False)]
    print("Coluna 'NU_INSCRICAO' validada.")
    # 'NU_INSCRICAO'


    # Remove na coluna 'TP_FAIXA_ETARIA' valores menores que 1 ou maiores que 20
    df_parquet = df_parquet[(df_parquet['TP_FAIXA_ETARIA'] >= 1) & (df_parquet['TP_FAIXA_ETARIA'] <= 20)]
    print(f"Coluna 'TP_FAIXA_ETARIA' validada.")
    # 'TP_FAIXA_ETARIA'


    # Remove na coluna 'TP_SEXO' valores diferentes de 'F' e 'M'
    allowed_values_tp_sexo = ['F', 'M']
    df_parquet = df_parquet[df_parquet['TP_SEXO'].isin(allowed_values_tp_sexo)]
    print("Coluna 'TP_SEXO' validada.")
    # 'TP_SEXO'


    # Remove na coluna 'TP_ESTADO_CIVIL' valores menores que 0 ou maiores que 4
    df_parquet = df_parquet[(df_parquet['TP_ESTADO_CIVIL'] >= 0) & (df_parquet['TP_ESTADO_CIVIL'] <= 4)]
    print("Coluna 'TP_ESTADO_CIVIL' validada.")
    # 'TP_ESTADO_CIVIL'


    # Remove na coluna 'TP_COR_RACA' valores menores que 0 ou maiores que 6
    df_parquet = df_parquet[(df_parquet['TP_COR_RACA'] >= 0) & (df_parquet['TP_COR_RACA'] <= 6)]
    print("Coluna 'TP_COR_RACA' validada.")
    # 'TP_COR_RACA'


    # Remove na coluna 'TP_NACIONALIDADE' valores menores que 0 ou maiores que 4
    df_parquet = df_parquet[(df_parquet['TP_NACIONALIDADE'] >= 0) & (df_parquet['TP_NACIONALIDADE'] <= 4)]
    print("Coluna 'TP_NACIONALIDADE' validada.")
    # 'TP_NACIONALIDADE'


    # Remove na coluna 'TP_ESCOLA' valores menores que 1 ou maiores que 3
    df_parquet = df_parquet[(df_parquet['TP_ESCOLA'] >= 1) & (df_parquet['TP_ESCOLA'] <= 3)]
    print("Coluna 'TP_ESCOLA' validada.")
    # 'TP_ESCOLA'


    # Remove na coluna 'IN_TREINEIRO' valores menores que 0 ou maiores que 1
    df_parquet = df_parquet[(df_parquet['IN_TREINEIRO'] >= 0) & (df_parquet['IN_TREINEIRO'] <= 1)]
    print("Coluna 'IN_TREINEIRO' validada.")
    # 'IN_TREINEIRO'


    # Remove na coluna 'SG_UF_PROVA' valores nulos/vazios
    df_parquet = df_parquet.dropna(subset=['SG_UF_PROVA'])
    print("Coluna 'SG_UF_PROVA' validada.")
    # 'SG_UF_PROVA'


    # Remove na coluna 'TP_PRESENCA_CN' valores menores que 0 ou maiores que 2
    df_parquet = df_parquet[(df_parquet['TP_PRESENCA_CN'] >= 0) & (df_parquet['TP_PRESENCA_CN'] <= 2)]
    print("Coluna 'TP_PRESENCA_CN' validada.")
    # 'TP_PRESENCA_CN'


    # Remove na coluna 'TP_PRESENCA_CH' valores menores que 0 ou maiores que 2
    df_parquet = df_parquet[(df_parquet['TP_PRESENCA_CH'] >= 0) & (df_parquet['TP_PRESENCA_CH'] <= 2)]
    print("Coluna 'TP_PRESENCA_CH' validada.")
    # 'TP_PRESENCA_CH'


    # Remove na coluna 'TP_PRESENCA_MT' valores menores que 0 ou maiores que 2
    df_parquet = df_parquet[(df_parquet['TP_PRESENCA_MT'] >= 0) & (df_parquet['TP_PRESENCA_MT'] <= 2)]
    print("Coluna 'TP_PRESENCA_MT' validada.")
    # 'TP_PRESENCA_MT'


    # Remove na coluna 'TP_PRESENCA_LC' valores menores que 0 ou maiores que 2
    df_parquet = df_parquet[(df_parquet['TP_PRESENCA_LC'] >= 0) & (df_parquet['TP_PRESENCA_LC'] <= 2)]
    print("Coluna 'TP_PRESENCA_LC' validada.")
    # 'TP_PRESENCA_LC'


    # Remove na coluna 'NU_NOTA_REDACAO' valores menores que 0 ou maiores que 1000
    df_parquet = df_parquet[(df_parquet['NU_NOTA_REDACAO'] >= 0) & (df_parquet['NU_NOTA_REDACAO'] <= 1000)]
    print("Coluna 'NU_NOTA_REDACAO' validada.")
    # 'NU_NOTA_REDACAO'


    # Remove na coluna 'NU_NOTA_CN' valores menores que 0 ou maiores que 1000
    df_parquet = df_parquet[(df_parquet['NU_NOTA_CN'] >= 0) & (df_parquet['NU_NOTA_CN'] <= 1000)]
    print("Coluna 'NU_NOTA_CN' validada.")
    # Coluna 'NU_NOTA_CN'


    # Remove na coluna 'NU_NOTA_CH' valores menores que 0 ou maiores que 1000
    df_parquet = df_parquet[(df_parquet['NU_NOTA_CH'] >= 0) & (df_parquet['NU_NOTA_CH'] <= 1000)]
    print("Coluna 'NU_NOTA_CH' validada.")
    # Coluna 'NU_NOTA_CH'


    # Remove na coluna 'NU_NOTA_LC' valores menores que 0 ou maiores que 1000
    df_parquet = df_parquet[(df_parquet['NU_NOTA_LC'] >= 0) & (df_parquet['NU_NOTA_LC'] <= 1000)]
    print("Coluna 'NU_NOTA_LC' validada.")
    # Coluna 'NU_NOTA_LC'


    # Remove na coluna 'NU_NOTA_MT' valores menores que 0 ou maiores que 1000
    df_parquet = df_parquet[(df_parquet['NU_NOTA_MT'] >= 0) & (df_parquet['NU_NOTA_MT'] <= 1000)]
    print("Coluna 'NU_NOTA_MT' validada.")
    # Coluna 'NU_NOTA_MT'

    # Remove na coluna 'TP_LINGUA' valores menores que 0 ou maiores que 1000
    df_parquet = df_parquet[(df_parquet['TP_LINGUA'] >= 0) & (df_parquet['TP_LINGUA'] <= 1)]
    print("Coluna 'TP_LINGUA' validada.")
    # 'TP_LINGUA'


    # Remove na coluna 'Q001' valores diferentes de 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
    allowed_values_q001 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    df_parquet = df_parquet[df_parquet['Q001'].isin(allowed_values_q001)]
    print("Coluna 'Q001' validada.")
    # 'Q001'


    # Remove na coluna 'Q002' valores diferentes de 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
    allowed_values_q002 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    df_parquet = df_parquet[df_parquet['Q002'].isin(allowed_values_q002)]
    print("Coluna 'Q002' validada.")
    # 'Q002'


    # Remove na coluna 'Q005' valores menores que 1 ou maiores que 20
    df_parquet = df_parquet[(df_parquet['Q005'] >= 1) & (df_parquet['Q005'] <= 20)]
    print("Coluna 'Q005' validada.")
    # 'Q005'


    # Remove na coluna 'Q006' valores diferentes de 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
    allowed_values_q006 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
    df_parquet = df_parquet[df_parquet['Q006'].isin(allowed_values_q006)]
    print("Coluna 'Q006' validada.")
    # 'Q006'


    # Remove na coluna 'Q019' valores diferentes de 'A', 'B', 'C', 'D', 'E'
    allowed_values_q019 = ['A', 'B', 'C', 'D', 'E']
    df_parquet = df_parquet[df_parquet['Q019'].isin(allowed_values_q019)]
    print("Coluna 'Q019' validada.")
    # 'Q019'


    # Remove na coluna 'Q024' valores diferentes de 'A', 'B', 'C', 'D', 'E'
    allowed_values_q024 = ['A', 'B', 'C', 'D', 'E']
    df_parquet = df_parquet[df_parquet['Q024'].isin(allowed_values_q024)]
    print("Coluna 'Q024' validada.")
    # 'Q024'


    # Remove na coluna 'Q025' valores diferentes de 'A' e 'B'
    allowed_values_q025 = ['A', 'B']
    df_parquet = df_parquet[df_parquet['Q025'].isin(allowed_values_q025)]
    print("Coluna 'Q025' validada.")
    # 'Q025'


def arredondarNotas():
    global df_parquet

    # Arredondar notas, não deixando casas decimais
    df_parquet['NU_NOTA_CN'] = df_parquet['NU_NOTA_CN'].round(0)
    df_parquet['NU_NOTA_CH'] = df_parquet['NU_NOTA_CH'].round(0)
    df_parquet['NU_NOTA_LC'] = df_parquet['NU_NOTA_LC'].round(0)
    df_parquet['NU_NOTA_MT'] = df_parquet['NU_NOTA_MT'].round(0)

    print("Notas arredondadas.")


def validarPresencasNotas():
    # Nessa função vamos manter apenas registros com todas as presenças e notas notas diferente de 0

    global df_parquet

    # Apenas presentes em todos os dias
    df_parquet = df_parquet[
    ((df_parquet['TP_PRESENCA_CN'] == 1)) &
    ((df_parquet['TP_PRESENCA_CH'] == 1)) &
    ((df_parquet['TP_PRESENCA_LC'] == 1)) &
    ((df_parquet['TP_PRESENCA_MT'] == 1))
    ]

    # Sem notas zeradas
    df_parquet = df_parquet[
    ((df_parquet['NU_NOTA_CN'] != 0)) &
    ((df_parquet['NU_NOTA_CH'] != 0)) &
    ((df_parquet['NU_NOTA_LC'] != 0)) &
    ((df_parquet['NU_NOTA_MT'] != 0)) &
    ((df_parquet['NU_NOTA_REDACAO'] != 0))
    ]


def metricasColunas():
    global df_parquet

    # Criando uma lista com as colunas que possuem variáveis numericas
    colunas_numericas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

    medidas_estatisticas = {}
    for col in colunas_numericas:
        medidas_estatisticas[col] = {
            'Média': df_parquet[col].mean(),
            'Mediana': df_parquet[col].median(),
            'Moda': df_parquet[col].mode()[0],
            'Desvio Padrão': df_parquet[col].std(),
            'Variância': df_parquet[col].var(),
            'Mínimo': df_parquet[col].min(),
            'Máximo': df_parquet[col].max(),
            '1º Quartil': df_parquet[col].quantile(0.25),
            '3º Quartil': df_parquet[col].quantile(0.75),
            'Amplitude': df_parquet[col].max() - df_parquet[col].min(),
            'Assimetria': df_parquet[col].skew(),
            'Curtose': df_parquet[col].kurtosis(),
            'Coeficiente de Pearson': 3*(df_parquet[col].mean() - df_parquet[col].median())/df_parquet[col].std()
        }

    # Exibindo as medidas estatísticas
    for col, medidas in medidas_estatisticas.items():
        print(f'Coluna: {col}')
        for medida, valor in medidas.items():
            print(f'{medida}: {valor:.2f}')
        print()


def apenasFaltantes():
    # Vamos separar para um dataframe de faltantes, para verificarmos a taxa de abstenção

    colunas_presenca = [
    'TP_PRESENCA_CN', 
    'TP_PRESENCA_CH', 
    'TP_PRESENCA_LC', 
    'TP_PRESENCA_MT'
    ]

    df_faltantes = df_parquet[(df_parquet[colunas_presenca] == 0).any(axis=1)]

    df_faltantes.to_parquet(r"arquivos\MICRODADOS_ENEM_FALTANTES_2023.parquet", index=False)


transformarColunas()

validarColunas()

apenasFaltantes()

validarPresencasNotas()

arredondarNotas()

metricasColunas()

# Separando em dois dataframes
df_parquet = df_parquet[df_parquet['SG_UF_PROVA'] == 'SC']
df_brasil = df_parquet[df_parquet['SG_UF_PROVA'] != 'SC']


df_parquet.to_parquet(r"arquivos\MICRODADOS_ENEM_SC_2023.parquet", index=False)
df_brasil.to_parquet(r"arquivos\MICRODADOS_ENEM_BRASIL_2023.parquet", index=False)

