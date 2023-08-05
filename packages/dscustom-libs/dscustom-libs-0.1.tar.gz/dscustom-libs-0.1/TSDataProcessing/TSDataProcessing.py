#bibliotecas necessárias
import pandas as pd
import numpy as np

'''
====================================================================================================
Substituição de missing values em variáveis numéricas em múltiplas séries temporais utilizando ffill
=====================================================================================================

Retorna um pandas dataframe com as colunas tratadas.

:: Parâmetros
-------------
    ** id_column (requerido): str or list
        Nome da coluna que identifica cada uma das múltiplas séries temporais.
    ** features (requerido): list
        Lista com o nome das features categóricas que terão os missing values substituídos.
    ** time_id_column (opcional): str
        Nome da coluna caso exista o desejo de que os valores utilizados na substitução sejam referentes
        a um período específico de tempo (Ex: usar o valor da última semana, do útlimo mês, etc.)

:: Exemplo
-----------
    #Inicialização
    imputer = MissingImputer(id_column="forno_id",
                                features=["var1", "var2"])

    #fit
    imputer.fit(df)

    #transform
    df = imputer.transform(df)
        
'''

from sklearn.base import BaseEstimator, TransformerMixin
# All sklearn Transforms must have the `transform` and `fit` methods

class MissingImputer(BaseEstimator, TransformerMixin):
    def __init__(self, id_column, features, time_id_column=False):
        self.id_column = id_column 
        self.features = features
        self.time_id_column = time_id_column

    def input(self, df, features):
        if self.time_id_column:
            for col in features:
                df[col] = df.groupby([self.id_column, self.time_id_column])[col].ffill()
        else:
            for col in features:
                df[col] = df.groupby([self.id_column])[col].ffill()

        return df

    def fit(self, X, y=None):
        return self 

    def transform(self, X):
        data = X.copy()
        data = self.input(df=data, features=self.features)
        return data
    


'''
=========================================================
Completar timeseries que possuem steps de data faltantes
=========================================================

Retorna um pandas dataframe com as datas completas dentro de um determinado período.

:: Parâmetros
--------------
    ** df (requerido): Pandas DataFrame
        Dataframe com os dados.
    ** date_col (requerido): str
        Nome da coluna que contém os dados de tempo.
    ** group_col (requerido): str
        Nome da coluna que identifica as múltiplas timeseries
    ** frequency (requerido): str, default="D"
        Modo de preenchimento das datas. Se "D", vai preencher os dias faltantes.
        Para mais detalhes, ver: https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#offset-aliases

:: Exemplo
----------
    #aplicação direta da função
    data = completa_serie_temporal(df=data, date_col="Data", group_col="Cuba")
        
'''
def completa_serie_temporal(df, date_col, group_col, frequency="D"):
    
    df = df.set_index(date_col)
    
    df = df.groupby([group_col]).apply(lambda x: x.asfreq(frequency))
    df = df.drop(columns=group_col, axis=1)
    df = df.reset_index()
    
    return df



#função para remover outliers usando método IQR
def remove_outliers_iqr(df, target, multiplier=1.5):
    Q1 = df[target].quantile(0.25)
    Q3 = df[target].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR

    # Filter rows that are not outlier
    df['iqr_outlier'] = 1
    df.loc[(df[target] >= lower_bound) & (df[target] <= upper_bound), 'iqr_outlier'] = 0
    return df

'''
================================
Calcula a variação de timeseries
================================

Retorna um pandas dataframe com uma nova coluna que contém a variação da timeseries. É útil para
converter séries temporais não estacionárias em estacionárias. Para saber sobre séries estacionárias,
ver: https://machinelearningmastery.com/time-series-data-stationary-python/ .

:: Parâmetros
--------------
    ** data (requerido): Pandas DataFrame
        Dataframe com os dados.
    ** group_id (requerido): str
        Nome da coluna que identifica as múltiplas timeseries.
    ** timeseries (requerido): str
        Nome da coluna referente à série temporal a ser transformada.
   
:: Exemplo
----------
    #aplicação direta da função
    data = diff_group_timeseries(data=data, group_id="Linha", timeseries="Temperatura")
        
    
OBSERVAÇÃO: É importante que a função completa_time_series seja utilizada antes desta.
'''
def diff_group_timeseries(data, group_id, timeseries):
    data[f"{timeseries}_variacao"] = data.groupby(group_id)[timeseries].diff().bfill()
    return data