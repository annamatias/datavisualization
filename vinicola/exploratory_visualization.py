import pandas as pd

# Transformando dados verticais em colunas, retirando redundancias
# Foi retirado dos arquivos manualmente as colunas "Id" e algumas que vieram com erro, isso pode ser tratado via código tbm, com o drop()


def comercializacao():
    df_comercio = pd.read_csv(
        "/Users/annakarolinymatias/Documents/datavisualization/data_sources/comercializacao_vinho_2021.csv", sep=";")
    colunas_selecionadas = df_comercio.columns
    df_comercio = df_comercio.melt(
        id_vars='PRODUTO', value_vars=colunas_selecionadas, var_name='ANO', value_name='QTD_LITRO')
    return df_comercio


def exportacao():
    df_exportacao = pd.read_csv(
        "/Users/annakarolinymatias/Documents/datavisualization/data_sources/exportacao_vinho_2021.csv", sep=";")
    colunas_selecionadas = df_exportacao.loc[:, ~df_exportacao.columns.str.endswith(
        '.1') & (df_exportacao.columns != 'País')]
    df_qtd = df_exportacao.melt(
        id_vars='País', value_vars=colunas_selecionadas, var_name='ANO', value_name='QTD_LITRO')

    colunas_selecionadas_valor = df_exportacao.filter(regex=r'\.1$')
    df_valor = df_exportacao.melt(
        id_vars='País', value_vars=colunas_selecionadas_valor, var_name='ANO_2', value_name='VALOR_US')

    df_qtd["VALOR_US"] = df_valor["VALOR_US"]
    return df_qtd


def importacao_vinhos():
    df_importacao_vinhos = pd.read_csv(
        "/Users/annakarolinymatias/Documents/datavisualization/data_sources/importacao_vinhos_de_mesa_2021.csv", sep=";")

    colunas_selecionadas = df_importacao_vinhos.loc[:, ~df_importacao_vinhos.columns.str.endswith(
        '.1') & (df_importacao_vinhos.columns != 'País')]
    df_qtd = df_importacao_vinhos.melt(
        id_vars='País', value_vars=colunas_selecionadas, var_name='ANO', value_name='QTD_LITRO')

    colunas_selecionadas_valor = df_importacao_vinhos.filter(regex=r'\.1$')
    df_valor = df_importacao_vinhos.melt(
        id_vars='País', value_vars=colunas_selecionadas_valor, var_name='ANO_2', value_name='VALOR_US')

    df_qtd["VALOR_US"] = df_valor["VALOR_US"]

    return df_qtd.tail(20)


def importacao_espumantes():
    df_importacao_espumantes = pd.read_csv(
        "/Users/annakarolinymatias/Documents/datavisualization/data_sources/importacao_espumantes_2021.csv", sep=";")

    colunas_selecionadas = df_importacao_espumantes.loc[:, ~df_importacao_espumantes.columns.str.endswith(
        '.1') & (df_importacao_espumantes.columns != 'País')]
    df_qtd = df_importacao_espumantes.melt(
        id_vars='País', value_vars=colunas_selecionadas, var_name='ANO', value_name='QTD_LITRO')

    colunas_selecionadas_valor = df_importacao_espumantes.filter(regex=r'\.1$')
    df_valor = df_importacao_espumantes.melt(
        id_vars='País', value_vars=colunas_selecionadas_valor, var_name='ANO_2', value_name='VALOR_US')

    df_qtd["VALOR_US"] = df_valor["VALOR_US"]

    return df_qtd.tail(20)


def producao_vinhos():
    df_producao_vinhos = pd.read_csv(
        "/Users/annakarolinymatias/Documents/datavisualization/data_sources/producao_vinho_2021.csv", sep=";")

    colunas_selecionadas = df_producao_vinhos.columns
    df_producao_vinhos = df_producao_vinhos.melt(
        id_vars='PRODUTO', value_vars=colunas_selecionadas, var_name='ANO', value_name='QTD_LITRO')
    return df_producao_vinhos
