import pandas as pd

df_csv = pd.read_csv(r"arquivos\MICRODADOS_ENEM_2023.csv", encoding='latin1', sep=';')
df_csv.to_parquet(r"arquivos\MICRODADOS_ENEM_2023.parquet", index=False)

df_parquet = pd.read_parquet(r"arquivos\MICRODADOS_ENEM_2023.parquet")

def removerColunas(df):
    colunas_para_remover = [
        'NU_ANO', 
        'TP_ST_CONCLUSAO', 
        'TP_ANO_CONCLUIU', 
        'CO_MUNICIPIO_ESC', 
        'NO_MUNICIPIO_ESC', 
        'CO_UF_ESC', 
        'SG_UF_ESC', 
        'TP_DEPENDENCIA_ADM_ESC', 
        'TP_LOCALIZACAO_ESC', 
        'TP_SIT_FUNC_ESC', 
        'CO_PROVA_CN',
        'CO_PROVA_CH',
        'CO_PROVA_LC',
        'CO_PROVA_MT',
        'TX_RESPOSTAS_CN',
        'TX_RESPOSTAS_CH',
        'TX_RESPOSTAS_LC',
        'TX_RESPOSTAS_MT',
        'TX_GABARITO_CN',
        'TX_GABARITO_CH',
        'TX_GABARITO_LC',
        'TX_GABARITO_MT',
        'Q003',
        'Q004',
        'Q007',
        'Q008',
        'Q009',
        'Q010',
        'Q011',
        'Q012',
        'Q013',
        'Q014',
        'Q015',
        'Q016',
        'Q017',
        'Q018',
        'Q019',
        'Q020',
        'Q021',
        'Q022',
        'Q023'
    ]
    
    df = df.drop(columns=colunas_para_remover)

    return df


def transformarColunas(df):
    # Nessa funcao iremos alterar o tamanho das colunas, otimizando o consumo de armazenamento e velocidade de busca

    df['NU_INSCRICAO'] = df['NU_INSCRICAO'].astype('Int64')
    df['NU_ANO'] = df['NU_ANO'].astype('Int16')
    df['TP_FAIXA_ETARIA'] = df['TP_FAIXA_ETARIA'].astype('Int16')
    df['TP_SEXO'] = df['TP_SEXO'].astype('category')
    df['TP_ESTADO_CIVIL'] = df['TP_ESTADO_CIVIL'].astype('Int8')
    df['TP_COR_RACA'] = df['TP_COR_RACA'].astype('Int8')
    df['TP_NACIONALIDADE'] = df['TP_NACIONALIDADE'].astype('Int8')
    df['TP_ST_CONCLUSAO'] = df['TP_ST_CONCLUSAO'].astype('Int8')
    df['TP_ANO_CONCLUIU'] = df['TP_ANO_CONCLUIU'].astype('Int8')
    df['TP_ESCOLA'] = df['TP_ESCOLA'].astype('Int8')
    df['TP_ENSINO'] = df['TP_ENSINO'].astype('Int8')
    df['IN_TREINEIRO'] = df['IN_TREINEIRO'].astype('Int8')
    df['CO_MUNICIPIO_ESC'] = df['CO_MUNICIPIO_ESC'].astype('Int32')
    df['NO_MUNICIPIO_ESC'] = df['NO_MUNICIPIO_ESC'].astype('category')
    df['CO_UF_ESC'] = df['CO_UF_ESC'].astype('Int8')
    df['SG_UF_ESC'] = df['SG_UF_ESC'].astype('category')
    df['TP_DEPENDENCIA_ADM_ESC'] = df['TP_DEPENDENCIA_ADM_ESC'].astype('Int8')
    df['TP_LOCALIZACAO_ESC'] = df['TP_LOCALIZACAO_ESC'].astype('Int8')
    df['TP_SIT_FUNC_ESC'] = df['TP_SIT_FUNC_ESC'].astype('Int8')
    df['CO_MUNICIPIO_PROVA'] = df['CO_MUNICIPIO_PROVA'].astype('Int32')
    df['NO_MUNICIPIO_PROVA'] = df['NO_MUNICIPIO_PROVA'].astype('category')
    df['CO_UF_PROVA'] = df['CO_UF_PROVA'].astype('Int8')
    df['SG_UF_PROVA'] = df['SG_UF_PROVA'].astype('category')
    df['TP_PRESENCA_CN'] = df['TP_PRESENCA_CN'].astype('Int8')
    df['TP_PRESENCA_CH'] = df['TP_PRESENCA_CH'].astype('Int8')
    df['TP_PRESENCA_LC'] = df['TP_PRESENCA_LC'].astype('Int8')
    df['TP_PRESENCA_MT'] = df['TP_PRESENCA_MT'].astype('Int8')
    df['CO_PROVA_CN'] = df['CO_PROVA_CN'].astype('Int16')
    df['CO_PROVA_CH'] = df['CO_PROVA_CH'].astype('Int16')
    df['CO_PROVA_LC'] = df['CO_PROVA_LC'].astype('Int16')
    df['CO_PROVA_MT'] = df['CO_PROVA_MT'].astype('Int16')
    df['NU_NOTA_CN'] = df['NU_NOTA_CN'].astype('float64')
    df['NU_NOTA_CH'] = df['NU_NOTA_CH'].astype('float64')
    df['NU_NOTA_LC'] = df['NU_NOTA_LC'].astype('float64')
    df['NU_NOTA_MT'] = df['NU_NOTA_MT'].astype('float64')
    df['TX_RESPOSTAS_CN'] = df['TX_RESPOSTAS_CN'].astype('category')
    df['TX_RESPOSTAS_CH'] = df['TX_RESPOSTAS_CH'].astype('category')
    df['TX_RESPOSTAS_LC'] = df['TX_RESPOSTAS_LC'].astype('category')
    df['TX_RESPOSTAS_MT'] = df['TX_RESPOSTAS_MT'].astype('category')
    df['TP_LINGUA'] = df['TP_LINGUA'].astype('Int8')
    df['TX_GABARITO_CN'] = df['TX_GABARITO_CN'].astype('category')
    df['TX_GABARITO_CH'] = df['TX_GABARITO_CH'].astype('category')
    df['TX_GABARITO_LC'] = df['TX_GABARITO_LC'].astype('category')
    df['TX_GABARITO_MT'] = df['TX_GABARITO_MT'].astype('category')
    df['TP_STATUS_REDACAO'] = df['TP_STATUS_REDACAO'].astype('Int8')
    df['NU_NOTA_COMP1'] = df['NU_NOTA_COMP1'].astype('Int16')
    df['NU_NOTA_COMP2'] = df['NU_NOTA_COMP2'].astype('Int16')
    df['NU_NOTA_COMP3'] = df['NU_NOTA_COMP3'].astype('Int16')
    df['NU_NOTA_COMP4'] = df['NU_NOTA_COMP4'].astype('Int16')
    df['NU_NOTA_COMP5'] = df['NU_NOTA_COMP5'].astype('Int16')
    df['NU_NOTA_REDACAO'] = df['NU_NOTA_REDACAO'].astype('Int16')
    df['Q001'] = df['Q001'].astype('category')
    df['Q002'] = df['Q002'].astype('category')
    df['Q003'] = df['Q003'].astype('category')
    df['Q004'] = df['Q004'].astype('category')
    df['Q005'] = df['Q005'].astype('Int8')
    df['Q006'] = df['Q006'].astype('category')
    df['Q007'] = df['Q007'].astype('category')
    df['Q008'] = df['Q008'].astype('category')
    df['Q009'] = df['Q009'].astype('category')
    df['Q010'] = df['Q010'].astype('category')
    df['Q011'] = df['Q011'].astype('category')
    df['Q012'] = df['Q012'].astype('category')
    df['Q013'] = df['Q013'].astype('category')
    df['Q014'] = df['Q014'].astype('category')
    df['Q015'] = df['Q015'].astype('category')
    df['Q016'] = df['Q016'].astype('category')
    df['Q017'] = df['Q017'].astype('category')
    df['Q018'] = df['Q018'].astype('category')
    df['Q019'] = df['Q019'].astype('category')
    df['Q020'] = df['Q020'].astype('category')
    df['Q021'] = df['Q021'].astype('category')
    df['Q022'] = df['Q022'].astype('category')
    df['Q023'] = df['Q023'].astype('category')
    df['Q024'] = df['Q024'].astype('category')
    df['Q025'] = df['Q025'].astype('category')

    return df


def validarColunas(df):
    # Nessa funcao vamos validar se as colunas estão dentro dos seus respectivos valores
    # Caso o registro não cumpra os requisitos, o mesmo é removido
    # Seguindo o arquivos MICRODADOS_ENEM_DICIONARIO.csv
    # Estaremos validando apenas as colunas que foram utilizadas na análise   

    # Remove na coluna 'NU_INSCRICAO' valores duplicados
    df = df[~df.duplicated(subset=['NU_INSCRICAO'], keep=False)]
    print("Coluna 'NU_INSCRICAO' validada.")
    # 'NU_INSCRICAO'


    # Remove na coluna 'TP_FAIXA_ETARIA' valores menores que 1 ou maiores que 20
    df = df[(df['TP_FAIXA_ETARIA'] >= 1) & (df['TP_FAIXA_ETARIA'] <= 20)]
    print(f"Coluna 'TP_FAIXA_ETARIA' validada.")
    # 'TP_FAIXA_ETARIA'


    # Remove na coluna 'TP_SEXO' valores diferentes de 'F' e 'M'
    allowed_values_tp_sexo = ['F', 'M']
    df = df[df['TP_SEXO'].isin(allowed_values_tp_sexo)]
    print("Coluna 'TP_SEXO' validada.")
    # 'TP_SEXO'


    # Remove na coluna 'TP_ESTADO_CIVIL' valores menores que 0 ou maiores que 4
    df = df[(df['TP_ESTADO_CIVIL'] >= 0) & (df['TP_ESTADO_CIVIL'] <= 4)]
    print("Coluna 'TP_ESTADO_CIVIL' validada.")
    # 'TP_ESTADO_CIVIL'


    # Remove na coluna 'TP_COR_RACA' valores menores que 0 ou maiores que 6
    df = df[(df['TP_COR_RACA'] >= 0) & (df['TP_COR_RACA'] <= 6)]
    print("Coluna 'TP_COR_RACA' validada.")
    # 'TP_COR_RACA'


    # Remove na coluna 'TP_NACIONALIDADE' valores menores que 0 ou maiores que 4
    df = df[(df['TP_NACIONALIDADE'] >= 0) & (df['TP_NACIONALIDADE'] <= 4)]
    print("Coluna 'TP_NACIONALIDADE' validada.")
    # 'TP_NACIONALIDADE'


    # Remove na coluna 'TP_ESCOLA' valores menores que 1 ou maiores que 3
    df = df[(df['TP_ESCOLA'] >= 1) & (df['TP_ESCOLA'] <= 3)]
    print("Coluna 'TP_ESCOLA' validada.")
    # 'TP_ESCOLA'


    # Remove na coluna 'IN_TREINEIRO' valores menores que 0 ou maiores que 1
    df = df[(df['IN_TREINEIRO'] >= 0) & (df['IN_TREINEIRO'] <= 1)]
    print("Coluna 'IN_TREINEIRO' validada.")
    # 'IN_TREINEIRO'


    # Remove na coluna 'SG_UF_PROVA' valores nulos/vazios
    df = df.dropna(subset=['SG_UF_PROVA'])
    print("Coluna 'SG_UF_PROVA' validada.")
    # 'SG_UF_PROVA'


    # Remove na coluna 'TP_PRESENCA_CN' valores menores que 0 ou maiores que 2
    df = df[(df['TP_PRESENCA_CN'] >= 0) & (df['TP_PRESENCA_CN'] <= 2)]
    print("Coluna 'TP_PRESENCA_CN' validada.")
    # 'TP_PRESENCA_CN'


    # Remove na coluna 'TP_PRESENCA_CH' valores menores que 0 ou maiores que 2
    df = df[(df['TP_PRESENCA_CH'] >= 0) & (df['TP_PRESENCA_CH'] <= 2)]
    print("Coluna 'TP_PRESENCA_CH' validada.")
    # 'TP_PRESENCA_CH'


    # Remove na coluna 'TP_PRESENCA_MT' valores menores que 0 ou maiores que 2
    df = df[(df['TP_PRESENCA_MT'] >= 0) & (df['TP_PRESENCA_MT'] <= 2)]
    print("Coluna 'TP_PRESENCA_MT' validada.")
    # 'TP_PRESENCA_MT'


    # Remove na coluna 'TP_PRESENCA_LC' valores menores que 0 ou maiores que 2
    df = df[(df['TP_PRESENCA_LC'] >= 0) & (df['TP_PRESENCA_LC'] <= 2)]
    print("Coluna 'TP_PRESENCA_LC' validada.")
    # 'TP_PRESENCA_LC'


    # Remove na coluna 'NU_NOTA_REDACAO' valores menores que 0 ou maiores que 1000
    df = df[(df['NU_NOTA_REDACAO'] >= 0) & (df['NU_NOTA_REDACAO'] <= 1000)]
    print("Coluna 'NU_NOTA_REDACAO' validada.")
    # 'NU_NOTA_REDACAO'


    # Remove na coluna 'NU_NOTA_CN' valores menores que 0 ou maiores que 1000
    df = df[(df['NU_NOTA_CN'] >= 0) & (df['NU_NOTA_CN'] <= 1000)]
    print("Coluna 'NU_NOTA_CN' validada.")
    # Coluna 'NU_NOTA_CN'


    # Remove na coluna 'NU_NOTA_CH' valores menores que 0 ou maiores que 1000
    df = df[(df['NU_NOTA_CH'] >= 0) & (df['NU_NOTA_CH'] <= 1000)]
    print("Coluna 'NU_NOTA_CH' validada.")
    # Coluna 'NU_NOTA_CH'


    # Remove na coluna 'NU_NOTA_LC' valores menores que 0 ou maiores que 1000
    df = df[(df['NU_NOTA_LC'] >= 0) & (df['NU_NOTA_LC'] <= 1000)]
    print("Coluna 'NU_NOTA_LC' validada.")
    # Coluna 'NU_NOTA_LC'


    # Remove na coluna 'NU_NOTA_MT' valores menores que 0 ou maiores que 1000
    df = df[(df['NU_NOTA_MT'] >= 0) & (df['NU_NOTA_MT'] <= 1000)]
    print("Coluna 'NU_NOTA_MT' validada.")
    # Coluna 'NU_NOTA_MT'

    # Remove na coluna 'TP_LINGUA' valores menores que 0 ou maiores que 1000
    df = df[(df['TP_LINGUA'] >= 0) & (df['TP_LINGUA'] <= 1)]
    print("Coluna 'TP_LINGUA' validada.")
    # 'TP_LINGUA'


    # Remove na coluna 'Q001' valores diferentes de 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
    allowed_values_q001 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    df = df[df['Q001'].isin(allowed_values_q001)]
    print("Coluna 'Q001' validada.")
    # 'Q001'


    # Remove na coluna 'Q002' valores diferentes de 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
    allowed_values_q002 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    df = df[df['Q002'].isin(allowed_values_q002)]
    print("Coluna 'Q002' validada.")
    # 'Q002'


    # Remove na coluna 'Q005' valores menores que 1 ou maiores que 20
    df = df[(df['Q005'] >= 1) & (df['Q005'] <= 20)]
    print("Coluna 'Q005' validada.")
    # 'Q005'


    # Remove na coluna 'Q006' valores diferentes de 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'
    allowed_values_q006 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
    df = df[df['Q006'].isin(allowed_values_q006)]
    print("Coluna 'Q006' validada.")
    # 'Q006'


    # Remove na coluna 'Q019' valores diferentes de 'A', 'B', 'C', 'D', 'E'
    allowed_values_q019 = ['A', 'B', 'C', 'D', 'E']
    df = df[df['Q019'].isin(allowed_values_q019)]
    print("Coluna 'Q019' validada.")
    # 'Q019'


    # Remove na coluna 'Q024' valores diferentes de 'A', 'B', 'C', 'D', 'E'
    allowed_values_q024 = ['A', 'B', 'C', 'D', 'E']
    df = df[df['Q024'].isin(allowed_values_q024)]
    print("Coluna 'Q024' validada.")
    # 'Q024'


    # Remove na coluna 'Q025' valores diferentes de 'A' e 'B'
    allowed_values_q025 = ['A', 'B']
    df = df[df['Q025'].isin(allowed_values_q025)]
    print("Coluna 'Q025' validada.")
    # 'Q025'

    return df


def traduzirColunas(df):
    # Vamos traduzir alguns valores das colunas, dessa forma, fica mais legível nos gráficos

    # TP_FAIXA_ETARIA
    traducao_tp_faixa_etaria = {
        1:	'Menor de 17 anos',
        2:	'17 anos',
        3:	'18 anos',
        4:	'19 anos',
        5:	'20 anos',
        6:	'21 anos',
        7:	'22 anos',
        8:	'23 anos',
        9:	'24 anos',
        10:	'25 anos',
        11:	'Entre 26 e 30 anos',
        12:	'Entre 31 e 35 anos',
        13:	'Entre 36 e 40 anos',
        14:	'Entre 41 e 45 anos',
        15:	'Entre 46 e 50 anos',
        16:	'Entre 51 e 55 anos',
        17:	'Entre 56 e 60 anos',
        18:	'Entre 61 e 65 anos',
        19:	'Entre 66 e 70 anos',
        20:	'Maior de 70 anos',
    }

    df['TP_FAIXA_ETARIA'] = df['TP_FAIXA_ETARIA'].map(traducao_tp_faixa_etaria)
    # TP_FAIXA_ETARIA


    # TP_ESTADO_CIVIL
    traducao_tp_estado_civil = {
        0: 'Não informado',
        1: 'Solteiro(a)',
        2: 'Casado(a)/Mora com companheiro(a)',
        3: 'Divorciado(a)/Desquitado(a)/Separado(a)',
        4: 'Viúvo(a)'
    }

    df['TP_ESTADO_CIVIL'] = df['TP_ESTADO_CIVIL'].map(traducao_tp_estado_civil)
    # TP_ESTADO_CIVIL


    # TP_COR_RACA
    traducao_tp_cor_raca = {
        0: 'Não declarado',
        1: 'Branca',
        2: 'Preta',
        3: 'Parda',
        4: 'Amarela',
        5: 'Indígena',
        6: 'Não dispõe da informacao'
    }

    df['TP_COR_RACA'] = df['TP_COR_RACA'].map(traducao_tp_cor_raca)
    # TP_COR_RACA


    # TP_NACIONALIDADE
    traducao_tp_nacionalidade = {
        0: 'Não informado',
        1: 'Brasileiro(a)',
        2: 'Brasileiro(a) Naturalizado(a)',
        3: 'Estrangeiro(a)',
        4: 'Brasileiro(a) Nato(a), nascido(a) no exterior'
    }

    df['TP_NACIONALIDADE'] = df['TP_NACIONALIDADE'].map(traducao_tp_nacionalidade)
    # TP_NACIONALIDADE


    # TP_ESCOLA
    traducao_tp_escola = {
        1: 'Não Respondeu',
        2: 'Pública',
        3: 'Privada'
    }

    df['TP_ESCOLA'] = df['TP_ESCOLA'].map(traducao_tp_escola)
    # TP_ESCOLA


    # TP_ENSINO
    traducao_tp_ensino = {
        1: 'Ensino Regular',
        2: 'Educacao Especial - Modalidade Substitutiva'
    }

    df['TP_ENSINO'] = df['TP_ENSINO'].map(traducao_tp_ensino)
    # TP_ENSINO


    # IN_TREINEIRO
    traducao_in_treineiro = {
        1: 'Sim',
        0: 'Não'
    }

    df['IN_TREINEIRO'] = df['IN_TREINEIRO'].map(traducao_in_treineiro)
    # IN_TREINEIRO


    # TP_LINGUA
    traducao_tp_lingua = {
        0: 'Inglês',
        1: 'Espanhol',
    }

    df['TP_LINGUA'] = df['TP_LINGUA'].map(traducao_tp_lingua)
    # TP_LINGUA


    # TP_STATUS_REDACAO
    traducao_tp_status_redacao = {
        1: 'Sem problemas',
        2: 'Anulada',
        3: 'Cópia Texto Motivador',
        4: 'Em Branco',
        6: 'Fuga ao Tema',
        7: 'Não atendimento ao tipo textual',
        8: 'Texto Insuficiente',
        9: 'Parte desconectada'
    }

    df['TP_STATUS_REDACAO'] = df['TP_STATUS_REDACAO'].map(traducao_tp_status_redacao)
    # TP_LINGUA


    # Q001 e Q002
    traducao_q001_q002 = {
        'A': 'Nunca estudou',
        'B': 'Não completou a 4ª série/5º ano do Ensino Fundamental',
        'C': 'Completou a 4ª série/5º ano, mas não completou a 8ª série/9º ano do Ensino Fundamental',
        'D': 'Ensino Médio Incompleto',
        'E': 'Ensino Médio Completo',
        'F': 'Completou a Faculdade, mas não completou a Pós-graduacao',
        'G': 'Completou a Pós-graduacao',
        'H': 'Não sei'
    }

    df['Q001'] = df['Q001'].map(traducao_q001_q002)
    df['Q002'] = df['Q002'].map(traducao_q001_q002)
    # Q001 e Q002


    # Q006
    traducao_q006 = {
        'A': 'Nenhuma Renda',
        'B': 'Até R$ 1.320,00',
        'C': 'R$ 1.320,01 - R$ 1.980,00',
        'D': 'R$ 1.980,01 - R$ 2.640,00',
        'E': 'R$ 2.640,01 - R$ 3.300,00',
        'F': 'R$ 3.300,01  - R$ 3.960,00',
        'G': 'R$ 3.960,01  - R$ 5.280,00',
        'H': 'R$ 5.280,01  - R$ 6.600,00',
        'I': 'R$ 6.600,01  - R$ 7.920,00',
        'J': 'R$ 7.920,01  - R$ 9240,00',
        'K': 'R$ 9.240,01  - R$ 10.560,00',
        'L': 'R$ 10.560,01 - R$ 11.880,00',
        'M': 'R$ 11.880,01 - R$ 13.200,00',
        'N': 'R$ 13.200,01 - R$ 15.840,00',
        'O': 'R$ 15.840,01 - R$19.800,00',
        'P': 'R$ 19.800,01 - R$ 26.400,00',
        'Q': 'Acima de R$ 26.400,00'
    }

    df['Q006'] = df['Q006'].map(traducao_q006)
    # Q006


    # Q019
    traducao_q019 = {
        'A': 'Não',
        'B': 'Sim, uma',
        'C': 'Sim, duas',
        'D': 'Sim, três',
        'E': 'Sim, quatro ou mais'
    }

    df['Q019'] = df['Q019'].map(traducao_q019)
    # Q019


    # Q024
    traducao_q024 = {
        'A': 'Não',
        'B': 'Sim, um',
        'C': 'Sim, dois',
        'D': 'Sim, três',
        'E': 'Sim, quatro ou mais'
    }

    df['Q024'] = df['Q024'].map(traducao_q024)
    # Q024


    # Q025
    traducao_q025 = {
        'A': 'Não',
        'B': 'Sim'
    }

    df['Q025'] = df['Q025'].map(traducao_q025)
    # Q025

    return df



def arredondarNotas(df):
    # Arredondar notas, não deixando casas decimais
    df['NU_NOTA_CN'] = df['NU_NOTA_CN'].round(0)
    df['NU_NOTA_CH'] = df['NU_NOTA_CH'].round(0)
    df['NU_NOTA_LC'] = df['NU_NOTA_LC'].round(0)
    df['NU_NOTA_MT'] = df['NU_NOTA_MT'].round(0)
    print("Notas arredondadas.")

    return df


def validarPresencasNotas(df):
    # Nessa funcao vamos manter apenas registros com todas as presenças e notas notas diferente de 0

    # Apenas presentes em todos os dias
    df = df[
        ((df['TP_PRESENCA_CN'] == 1)) &
        ((df['TP_PRESENCA_CH'] == 1)) &
        ((df['TP_PRESENCA_LC'] == 1)) &
        ((df['TP_PRESENCA_MT'] == 1))
    ]

    # Sem notas zeradas
    df = df[
        ((df['NU_NOTA_CN'] > 0)) &
        ((df['NU_NOTA_CH'] > 0)) &
        ((df['NU_NOTA_LC'] > 0)) &
        ((df['NU_NOTA_MT'] > 0)) &
        ((df['NU_NOTA_REDACAO'] > 0))
    ]

    return df


def metricasColunas(df):
    # Criando uma lista com as colunas que possuem variáveis numericas
    colunas_numericas = ['NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC', 'NU_NOTA_MT', 'NU_NOTA_REDACAO']

    medidas_estatisticas = {}
    for col in colunas_numericas:
        medidas_estatisticas[col] = {
            'Média': df[col].mean(),
            'Mediana': df[col].median(),
            'Moda': df[col].mode()[0],
            'Desvio Padrão': df[col].std(),
            'Variância': df[col].var(),
            'Mínimo': df[col].min(),
            'Máximo': df[col].max(),
            '1º Quartil': df[col].quantile(0.25),
            '3º Quartil': df[col].quantile(0.75),
            'Amplitude': df[col].max() - df[col].min(),
            'Assimetria': df[col].skew(),
            'Curtose': df[col].kurtosis(),
            'Coeficiente de Pearson': 3*(df[col].mean() - df[col].median())/df[col].std()
        }

    # Exibindo as medidas estatísticas
    for col, medidas in medidas_estatisticas.items():
        print(f'Coluna: {col}')
        for medida, valor in medidas.items():
            print(f'{medida}: {valor:.2f}')
        print()


df_parquet = transformarColunas(df_parquet)

df_parquet = validarColunas(df_parquet)

df_parquet = validarPresencasNotas(df_parquet)

df_parquet = arredondarNotas(df_parquet)

metricasColunas(df_parquet)

df_parquet = traduzirColunas(df_parquet)

df_parquet = removerColunas(df_parquet)

# Salvando arquivos
df_parquet.to_parquet(r"arquivos\MICRODADOS_ENEM_2023.parquet", index=False)
