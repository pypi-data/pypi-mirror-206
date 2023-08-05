#bibliotecas necessárias
import pandas as pd
import numpy as np

from scipy.signal import savgol_filter

from sklearn.base import BaseEstimator, TransformerMixin

"""
==================================================================
Script para extrair features estatísticas de múltiplas time series
==================================================================

Retorna um pandas dataframe com as colunas originais e as novas features calculadas.

:: Parâmetros
-------------
    ** group_columns (requerido): str or list
        Nome das colunas que identifica cada uma das múltiplas séries temporais.  
    ** rolling_window (requerido): int
        Tamanho do período de tempo passado que o algoritmo irá utilizar para realizar os cálculos.
    ** features (requerido): list
        Lista com o nome das features que serão usadas como base para os cálculos estatísticos.

:: Exemplo - calcular estatísticas dos últimos 30 dias das variáveis de temperatura e pressão de cada forno.
-----------
    #Inicialização
    sf = StatFeatures(group_columns="Forno",
                        rolling_window=30,
                        features=["temperatura", "pressao"])

    #fit
    sf.fit(data)

    #transform
    data = sf.transform(data)
"""

class StatFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, group_columns, rolling_window, features):
        self.group_columns = group_columns
        self.rolling_window = rolling_window
        self.features = features


    def statiscal_features(self, data_set, group, n_in, features):

        for feature in features:
            
            #mean
            data_set[feature+'_'+str(n_in)+'_mean'] = data_set.groupby(group)[feature].rolling(
                window=n_in).mean().reset_index(0, 
                                                drop=True)
            
            #max
            data_set[feature+'_'+str(n_in)+'_max'] = data_set.groupby(group)[feature].rolling(
                window=n_in).max().reset_index(0, 
                                                drop=True)

            #min
            data_set[feature+'_'+str(n_in)+'_min'] = data_set.groupby(group)[feature].rolling(
                window=n_in).min().reset_index(0, 
                                                drop=True)
            
            #soma acumulada
            data_set[feature+'_'+str(n_in)+'_SomaAcumulada'] = data_set.groupby(group)[feature].rolling(window=n_in).sum().reset_index(
                0, drop=True)
            
            #feature/soma acumulada
            data_set[feature+'/soma'] = data_set[feature]/(1+data_set[feature+'_'+str(n_in)+'_SomaAcumulada'])
            
            #variance
            data_set[feature+'_'+str(n_in)+'_variance'] = data_set.groupby(group)[feature].rolling(
                window=n_in).var().reset_index(0, 
                                                drop=True)
            #absolute sum of changes
            data_set[f"{feature}_{n_in}_sum_changes"] = data_set.groupby(group)[feature].diff(n_in)
            data_set[f"{feature}_{n_in}_sum_changes"] = abs(data_set[f"{feature}_{n_in}_sum_changes"].fillna(0))
            data_set[f"{feature}_{n_in}_sum_changes"] = data_set.groupby(
                group)[f"{feature}_{n_in}_sum_changes"].rolling(n_in).sum().reset_index(0, 
                                                drop=True)

            #mean absolute sum of changes
            data_set[f"{feature}_{n_in}_meanABS_changes"] = data_set.groupby(group)[feature].diff(n_in)
            data_set[f"{feature}_{n_in}_meanABS_changes"] = abs(data_set[f"{feature}_{n_in}_meanABS_changes"].fillna(0))
            data_set[f"{feature}_{n_in}_meanABS_changes"] = data_set.groupby(
                group)[f"{feature}_{n_in}_meanABS_changes"].rolling(n_in).mean().reset_index(0, 
                                                drop=True)

            #mean of changes
            data_set[f"{feature}_{n_in}_mean_changes"] = data_set.groupby(group)[feature].diff(n_in)
            data_set[f"{feature}_{n_in}_mean_changes"] = data_set[f"{feature}_{n_in}_mean_changes"].fillna(0)
            data_set[f"{feature}_{n_in}_mean_changes"] = data_set.groupby(
                group)[f"{feature}_{n_in}_mean_changes"].rolling(n_in).mean().reset_index(0, 
                                                drop=True)
        
        return data_set
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data = self.statiscal_features(data, self.group_columns, self.rolling_window, self.features)
        return data
    
"""
=================================================
Classe para criar estatísticas entre agrupamentos
=================================================

Retorna um pandas dataframe com as colunas originais e as novas features calculadas.

:: Parâmetros
    ** group_columns (requerido): list
        Lista com o(s) nome da(s) coluna(s) que identifica(m) cada uma das múltiplas séries temporais.  
    ** features (requerido): list
        Lista com o nome das features que serão usadas como base para os cálculos estatísticos.

:: Exemplo:
-----------
    #Inicialização
    group_features = GroupFeatures(group_columns=["Forno"],
                        features=["temperatura", "pressao"])

    #fit
    group_features.fit(df_train)

    #transform
    df_train = group_features.transform(df_train)
    df_val = group_features.transform(df_val)
    df_test = group_features.transform(df_test)

:: OBSERVAÇÃO:
--------------
    Precisa que a divisão treino, validação e teste seja feita antes do uso dessa classe.
"""
class GroupFeatures(BaseEstimator, TransformerMixin):
    
    def __init__(self, group_columns, features):
        self.group_columns = group_columns
        self.features = features
        
    def group_features(self, gp, vf, data):
        
        mean_names = []
        max_names = []
        min_names = []
        
        for f in vf:
            mean_name = f"{gp[0]}_{f}_mean"
            max_name = f"{gp[0]}_{f}_max"
            min_name = f"{gp[0]}_{f}_min"
            
            mean_names.append(mean_name)
            max_names.append(max_name)
            min_names.append(min_name)
            
        d_mean = dict(zip(vf, mean_names))
        d_max = dict(zip(vf, max_names))
        d_min = dict(zip(vf, min_names))
        
        df_group_mean = pd.DataFrame(data.groupby(gp)[vf[:]].mean().rename(columns=d_mean))
        df_group_mean = df_group_mean.reset_index()
        
        df_group_max = pd.DataFrame(data.groupby(gp)[vf[:]].max().rename(columns=d_max))
        df_group_max = df_group_max.reset_index()
        
        df_group_min = pd.DataFrame(data.groupby(gp)[vf[:]].min().rename(columns=d_min))
        df_group_min = df_group_min.reset_index()
        
        return df_group_mean, df_group_max, df_group_min
    
    def fit(self, X, y=None):
        self.X_group_mean, self.X_group_max, self.X_group_min = self.group_features(self.group_columns, self.features, X)
        return self.X_group_mean, self.X_group_max, self.X_group_min
                                    
    def transform(self, X):
                         
        #criando o dataframe
        X_final = X.merge(self.X_group_mean, on=self.group_columns, how="left")
        X_final = X_final.merge(self.X_group_max, on=self.group_columns, how="left")
        X_final = X_final.merge(self.X_group_min, on=self.group_columns, how="left")
                                    
        for value_feature in self.features:
            X_final[f"{value_feature}/{self.group_columns[0]}_mean"] = X_final[f"{value_feature}"] / X_final[f"{self.group_columns[0]}_{value_feature}_mean"]
            X_final[f"{value_feature}/{self.group_columns[0]}_max"] = X_final[f"{value_feature}"] / X_final[f"{self.group_columns[0]}_{value_feature}_max"]
            X_final[f"{value_feature}/{self.group_columns[0]}_min"] = X_final[f"{value_feature}"] / ((X_final[f"{self.group_columns[0]}_{value_feature}_min"]**2)+10)
                                    
        return X_final
    


"""
=================================================
Função para criar média móvel entre agrupamentos
=================================================

Retorna um pandas dataframe com as colunas originais e as novas features calculadas.

:: Parâmetros
    ** data (requerido): pandas DataFrame
        Dataframe com os dados.
    ** group (requerido): str
        Nome da coluna que identifica cada uma das timeseries  
    ** features (requerido): list
        Lista com o nome das features que serão usadas como base para os cálculos estatísticos.
    ** rolling_window (requeridi): int
        Janela total de tempo que será utilizada para o cálculo das médias.

:: Exemplo:
-----------
    data = group_rolling_mean(data=data, group="Cuba", features=["vazão", "pressão"], 
                                rolling_window=30)
"""
def group_rolling_mean(data, group, features, rolling_window):
    for feature in features:
        data[feature+'_'+str(rolling_window)+'_mean'] = data.groupby(group)[feature].rolling(
            window=rolling_window).mean().reset_index(0, drop=True)
        
    return data


"""
======================================================
Função para criar features lag em múltiplas timeseries
======================================================

Retorna um pandas dataframe com as colunas originais e as novas features calculadas.

:: Parâmetros
    ** data (requerido): pandas DataFrame
        Dataframe com os dados.
    ** group_id (requerido): str
        Nome da coluna que identifica cada uma das timeseries  
    ** features (requerido): list
        Lista com o nome das features que serão usadas como base para os cálculos estatísticos.
    ** lag_min (requerido): int
        Menor janela de tempo que o algoritmo irá buscar o valor.
    ** lag_max (requerido): int
        Maior janela de tempo que o algoritmo irá buscar o valor.

:: Exemplo:
-----------
    data = group_lag_features(data=data, group="Cuba", features=["vazão", "pressão"], 
                                lag_min=1, lag_max=4)
"""
def group_lag_features(data, group_id, features, lag_min, lag_max):
    for lag in range(lag_min, lag_max):
        for f in features:
            data[f"{f}_(t-{lag})"] = data.groupby(group_id)[f].shift(lag).bfill()
            data[f"{f}_diff_(t-{lag})"] = data.groupby(group_id)[f].diff(lag).bfill()

    return data