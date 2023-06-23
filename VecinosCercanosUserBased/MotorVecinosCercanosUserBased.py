import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split


class MotorRecomendacionVecinosCercanos:

    def __init__(self, df_ratings):
        self.df_ratings = df_ratings
        self.df_matrix = pd.pivot_table(self.df_ratings, values='stars',
                                        index='idUsuario', columns='idRestaurante').fillna(0)
        self.ratings = self.df_matrix.values
        self.ratings_train, self.ratings_test = train_test_split(self.ratings, test_size=0.2, random_state=42)
        self.sim_matrix = None
        self.users_predictions = None

    def obtenerPorcentajeDispersion(self):
        sparsity = float(len(self.ratings.nonzero()[0]))
        sparsity /= (self.ratings.shape[0] * self.ratings.shape[1])
        sparsity *= 100
        return sparsity

    def obtenerConjuntoTest(self):
        return self.ratings_test

    def obtenerConjuntoEntrenamiento(self):
        return self.ratings_train

    def generarMatrizSimilitudDeUsuarios(self):
        self.sim_matrix = 1 - sklearn.metrics.pairwise.cosine_distances(self.ratings)

    def generarMatrizRecomendaciones(self):
        self.users_predictions = self.sim_matrix.dot(self.ratings) / np.array([np.abs(self.sim_matrix).sum(axis=1)]).T

    def obtenerMatrizRecomendaciones(self):
        return self.users_predictions
