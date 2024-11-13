from itertools import product, combinations
from tqdm import tqdm

from scipy.stats import zscore # para calcular el z-score
from sklearn.neighbors import LocalOutlierFactor # para detectar outliers usando el método LOF
from sklearn.ensemble import IsolationForest # para detectar outliers usando el metodo IF
from sklearn.neighbors import NearestNeighbors # para calcular la epsilon


def gestion_nulos_lof(df, col_numericas, list_neighbors, lista_contaminacion):
    
    combinaciones = list(product(list_neighbors, lista_contaminacion))
    
    for neighbors, contaminacion in tqdm(combinaciones):
        lof = LocalOutlierFactor(n_neighbors=neighbors, 
                                 contamination=contaminacion,
                                 n_jobs=-1)
        df[f"outliers_lof_{neighbors}_{contaminacion}"] = lof.fit_predict(df[col_numericas])

    return df