import pandas as pd

def transformarArquivo():
    df_csv = pd.read_csv(csv_file_path, encoding='latin1', sep=',')
    df_csv.to_parquet(output_parquet_file_path, index=False)


def transformarColunas():
    df_parquet['NU_INSCRICAO'] = df_parquet['NU_INSCRICAO'].astype('int32')
    df_parquet['NU_ANO'] = df_parquet['NU_ANO'].astype('int16')
    df_parquet['TP_FAIXA_ETARIA'] = df_parquet['TP_FAIXA_ETARIA'].astype('int16')
    df_parquet['TP_SEXO'] = df_parquet['TP_SEXO'].astype('category')
    df_parquet['TP_ESTADO_CIVIL'] = df_parquet['TP_ESTADO_CIVIL'].astype('int8')
    df_parquet['TP_COR_RACA'] = df_parquet['TP_COR_RACA'].astype('int8')
    df_parquet['TP_NACIONALIDADE'] = df_parquet['TP_NACIONALIDADE'].astype('int8')
    df_parquet['TP_ST_CONCLUSAO'] = df_parquet['TP_ST_CONCLUSAO'].astype('int8')
    df_parquet['TP_ANO_CONCLUIU'] = df_parquet['TP_ANO_CONCLUIU'].astype('int8')
    df_parquet['TP_ESCOLA'] = df_parquet['TP_ESCOLA'].astype('int8')
    df_parquet['TP_ENSINO'] = df_parquet['TP_ENSINO'].astype('int8')
    df_parquet['IN_TREINEIRO'] = df_parquet['IN_TREINEIRO'].astype('bool')
    df_parquet['CO_MUNICIPIO_ESC'] = df_parquet['CO_MUNICIPIO_ESC'].astype('int32')
    df_parquet['NO_MUNICIPIO_ESC'] = df_parquet['NO_MUNICIPIO_ESC'].astype('category')
    df_parquet['CO_UF_ESC'] = df_parquet['CO_UF_ESC'].astype('int8')
    df_parquet['SG_UF_ESC'] = df_parquet['SG_UF_ESC'].astype('category')
    df_parquet['TP_DEPENDENCIA_ADM_ESC'] = df_parquet['TP_DEPENDENCIA_ADM_ESC'].astype('int8')
    df_parquet['TP_LOCALIZACAO_ESC'] = df_parquet['TP_LOCALIZACAO_ESC'].astype('int8')
    df_parquet['TP_SIT_FUNC_ESC'] = df_parquet['TP_SIT_FUNC_ESC'].astype('int8')
    df_parquet['CO_MUNICIPIO_PROVA'] = df_parquet['CO_MUNICIPIO_PROVA'].astype('int32')
    df_parquet['NO_MUNICIPIO_PROVA'] = df_parquet['NO_MUNICIPIO_PROVA'].astype('category')
    df_parquet['CO_UF_PROVA'] = df_parquet['CO_UF_PROVA'].astype('int8')
    df_parquet['SG_UF_PROVA'] = df_parquet['SG_UF_PROVA'].astype('category')
    df_parquet['TP_PRESENCA_CN'] = df_parquet['TP_PRESENCA_CN'].astype('int8')
    df_parquet['TP_PRESENCA_CH'] = df_parquet['TP_PRESENCA_CH'].astype('int8')
    df_parquet['TP_PRESENCA_LC'] = df_parquet['TP_PRESENCA_LC'].astype('int8')
    df_parquet['TP_PRESENCA_MT'] = df_parquet['TP_PRESENCA_MT'].astype('int8')
    df_parquet['CO_PROVA_CN'] = df_parquet['CO_PROVA_CN'].astype('int8')
    df_parquet['CO_PROVA_CH'] = df_parquet['CO_PROVA_CH'].astype('int8')
    df_parquet['CO_PROVA_LC'] = df_parquet['CO_PROVA_LC'].astype('int8')
    df_parquet['CO_PROVA_MT'] = df_parquet['CO_PROVA_MT'].astype('int8')
    df_parquet['NU_NOTA_CN'] = df_parquet['NU_NOTA_CN'].astype('float32')
    df_parquet['NU_NOTA_CH'] = df_parquet['NU_NOTA_CH'].astype('float32')
    df_parquet['NU_NOTA_LC'] = df_parquet['NU_NOTA_LC'].astype('float32')
    df_parquet['NU_NOTA_MT'] = df_parquet['NU_NOTA_MT'].astype('float32')
    df_parquet['TX_RESPOSTAS_CN'] = df_parquet['TX_RESPOSTAS_CN'].astype('category')
    df_parquet['TX_RESPOSTAS_CH'] = df_parquet['TX_RESPOSTAS_CH'].astype('category')
    df_parquet['TX_RESPOSTAS_LC'] = df_parquet['TX_RESPOSTAS_LC'].astype('category')
    df_parquet['TX_RESPOSTAS_MT'] = df_parquet['TX_RESPOSTAS_MT'].astype('category')
    df_parquet['TP_LINGUA'] = df_parquet['TP_LINGUA'].astype('int8')
    df_parquet['TX_GABARITO_CN'] = df_parquet['TX_GABARITO_CN'].astype('category')
    df_parquet['TX_GABARITO_CH'] = df_parquet['TX_GABARITO_CH'].astype('category')
    df_parquet['TX_GABARITO_LC'] = df_parquet['TX_GABARITO_LC'].astype('category')
    df_parquet['TX_GABARITO_MT'] = df_parquet['TX_GABARITO_MT'].astype('category')
    df_parquet['TP_STATUS_REDACAO'] = df_parquet['TP_STATUS_REDACAO'].astype('int8')
    df_parquet['NU_NOTA_COMP1'] = df_parquet['NU_NOTA_COMP1'].astype('int8')
    df_parquet['NU_NOTA_COMP2'] = df_parquet['NU_NOTA_COMP2'].astype('int8')
    df_parquet['NU_NOTA_COMP3'] = df_parquet['NU_NOTA_COMP3'].astype('int8')
    df_parquet['NU_NOTA_COMP4'] = df_parquet['NU_NOTA_COMP4'].astype('int8')
    df_parquet['NU_NOTA_COMP5'] = df_parquet['NU_NOTA_COMP5'].astype('int8')
    df_parquet['NU_NOTA_REDACAO'] = df_parquet['NU_NOTA_REDACAO'].astype('int8')
    df_parquet['Q001'] = df_parquet['Q001'].astype('category')
    df_parquet['Q002'] = df_parquet['Q002'].astype('category')
    df_parquet['Q003'] = df_parquet['Q003'].astype('category')
    df_parquet['Q004'] = df_parquet['Q004'].astype('category')
    df_parquet['Q005'] = df_parquet['Q005'].astype('int8')
    df_parquet['Q006'] = df_parquet['Q006'].astype('category')
    df_parquet['Q007'] = df_parquet['Q007'].astype('category')
    df_parquet['Q008'] = df_parquet['Q008'].astype('category')
    df_parquet['Q009'] = df_parquet['Q009'].astype('category')
    df_parquet['Q0010'] = df_parquet['Q0010'].astype('category')
    df_parquet['Q0011'] = df_parquet['Q0011'].astype('category')
    df_parquet['Q0012'] = df_parquet['Q0012'].astype('category')
    df_parquet['Q0013'] = df_parquet['Q0013'].astype('category')
    df_parquet['Q0014'] = df_parquet['Q0014'].astype('category')
    df_parquet['Q0015'] = df_parquet['Q0015'].astype('category')
    df_parquet['Q0016'] = df_parquet['Q0016'].astype('category')
    df_parquet['Q0017'] = df_parquet['Q0017'].astype('category')
    df_parquet['Q0018'] = df_parquet['Q0018'].astype('category')
    df_parquet['Q0019'] = df_parquet['Q0019'].astype('category')
    df_parquet['Q0020'] = df_parquet['Q0020'].astype('category')
    df_parquet['Q0021'] = df_parquet['Q0021'].astype('category')
    df_parquet['Q0022'] = df_parquet['Q0022'].astype('category')
    df_parquet['Q0023'] = df_parquet['Q0023'].astype('category')
    df_parquet['Q0024'] = df_parquet['Q0024'].astype('category')
    df_parquet['Q0025'] = df_parquet['Q0025'].astype('category')


def arredondarNotas():
    # Arredondar notas, não deixando casas decimais
    df_parquet['NU_NOTA_CN'] = df_parquet['NU_NOTA_CN'].round(0)
    df_parquet['NU_NOTA_CH'] = df_parquet['NU_NOTA_CH'].round(0)
    df_parquet['NU_NOTA_LC'] = df_parquet['NU_NOTA_LC'].round(0)
    df_parquet['NU_NOTA_MT'] = df_parquet['NU_NOTA_MT'].round(0)


def validarColunas():
    # Nessa seção vamos validar se as colunas estão dentro dos seus respectivos valores
    # Caso o registro não cumpra os requisitos, o mesmo é removido
    # Seguindo o arquivos MICRODADOS_ENEM_DICIONARIO.csv
    # Estaremos validando apenas as colunas que foram utilizadas na análise

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


def validarPresencasNotas():
    # Remove registros onde 'NU_NOTA_CN' é nulo E 'TP_PRESENCA_CN' é igual a 1
    df_parquet = df_parquet[
    ~((df_parquet['NU_NOTA_CN'].isnull()) &
      (df_parquet['TP_PRESENCA_CN'] == 1))
    ]
    print("Relação 'NU_NOTA_CN' | 'TP_PRESENCA_CN' validada.")
    # 'NU_NOTA_CN' | 'TP_PRESENCA_CN'
    
    
    # Remove registros onde 'NU_NOTA_CH' é nulo E 'TP_PRESENCA_CH' é igual a 1
    df_parquet = df_parquet[
    ~((df_parquet['NU_NOTA_CH'].isnull()) &
      (df_parquet['TP_PRESENCA_CH'] == 1))
    ]
    print("Relação 'NU_NOTA_CH' | 'TP_PRESENCA_CH' validada.")
    # 'NU_NOTA_CH' | 'TP_PRESENCA_CH'
    
    
    # Remove registros onde 'NU_NOTA_LC' é nulo E 'TP_PRESENCA_LC' é igual a 1
    df_parquet = df_parquet[
    ~((df_parquet['NU_NOTA_LC'].isnull()) &
      (df_parquet['TP_PRESENCA_LC'] == 1))
    ]
    print("Relação 'NU_NOTA_LC' | 'TP_PRESENCA_LC' validada.")
    # 'NU_NOTA_LC' | 'TP_PRESENCA_LC'
    
    
    # Remove registros onde 'NU_NOTA_MT' é nulo E 'TP_PRESENCA_MT' é igual a 1
    df_parquet = df_parquet[
    ~((df_parquet['NU_NOTA_MT'].isnull()) &
      (df_parquet['TP_PRESENCA_MT'] == 1))
    ]
    print("Relação 'NU_NOTA_MT' | 'TP_PRESENCA_MT' validada.")
    # 'NU_NOTA_MT' | 'TP_PRESENCA_MT'


csv_file_path = 'MICRODADOS_ENEM_2023.csv'
output_parquet_file_path = 'MICRODADOS_ENEM_2023.parquet'

# Lê o .csv e muda para .parquet
transformarArquivo()

# Lê o arquivo .parquet
df_parquet = pd.read_parquet('MICRODADOS_ENEM_2023.parquet')


# Otimiza o tamanho das colunas
transformarColunas()


validarColunas()
validarPresencasNotas()
arredondarNotas()

# Separando em dois dataframes
df_sc = df_parquet[df_parquet['SG_UF_PROVA'] == 'SC']
df_brasil = df_parquet[df_parquet['SG_UF_PROVA'] != 'SC']


print(f"Tipo: {df_parquet['Q004']}")
