import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class Normalizar:
    def __init__(self, caminho_csv):
        arquivo = pd.read_csv(caminho_csv)
        coluna_sensores = ['sensor_1L', 'sensor_2L', 'sensor_3L', 'sensor_4L', 'sensor_5L', 'sensor_6L',
                           'sensor_1R', 'sensor_2R', 'sensor_3R', 'sensor_4R', 'sensor_5R', 'sensor_6R']
        means = arquivo[coluna_sensores].mean().to_numpy()
        stds = arquivo[coluna_sensores].std().to_numpy()
        np.save('means.npy', means)
        np.save('stds.npy', stds)
        self.means = np.load('means.npy')
        self.stds = np.load('stds.npy')

    def pre_processar(self, window):
        w = (window - self.means)/(self.stds + 1e-8)
        return w.astype(np.float32)

    def criar_janelas(self, dados, labels, window_size=100, passo=50):
        X, y = [], []
        for i in range(0, len(dados) - window_size, passo):
            X.append(dados[i:i + window_size])
            y.append(labels[i + window_size - 1])
        return np.array(X), np.array(y)