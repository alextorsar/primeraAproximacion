import pandas as pd
from sklearn.neighbors import NearestNeighbors

from VecinosCercanosItemBased.CreadorRecomendacionesItemBased import CreadorRecomendacionesItemBased


class AlgoritmoVecinosCercanosItemBased:

    def __init__(self, df_ratings, df_users, df_restaurants):
        self.df_ratings = df_ratings
        self.df_restaurants = df_restaurants
        self.df_users = df_users
        self.indices = None
        self.distances = None

    def ejecutarAlgoritmo(self):
        df_matrix = pd.pivot_table(self.df_ratings, values='stars',
                                   index='restaurantOid', columns='idUsuario').fillna(0)
        ratings = df_matrix.values
        knn = NearestNeighbors(metric='cosine', algorithm='brute')
        knn.fit(ratings)
        self.distances, self.indices = knn.kneighbors(ratings, n_neighbors=1643)
        #self.distances, self.indices = knn.kneighbors(ratings, n_neighbors=1827)

    def almacenarRecomendacionesEnBD(self):
        creadorRecomendaciones =  CreadorRecomendacionesItemBased(self.df_restaurants)
        creadorRecomendaciones.ejecutarInsercion(self.distances, self.indices)
