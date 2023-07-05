import pandas as pd


def read_csv(path="/Users/annakarolinymatias/Documents/datavisualization/data_sources/exportacao_vinho_2021.csv"):
    return pd.read_csv(path, sep=";")


def select_cols(df):
    select_cols = ['País', '2006', '2006.1', '2007', '2007.1', '2008', '2008.1', '2009', '2009.1',
                   '2010', '2010.1', '2011', '2011.1', '2012', '2012.1', '2013', '2013.1',
                   '2014', '2014.1', '2015', '2015.1', '2016', '2016.1', '2017', '2017.1',
                   '2018', '2018.1', '2019', '2019.1', '2020', '2020.1', '2021', '2021.1']
    return df.loc[:, select_cols]


def transformation(df):
    # df["país_origem"] = ["Brasil"] ver como colocar uma nova coluna com esse valor
    df.rename(columns={'País': 'país_destino'}, inplace=True)
    return df
