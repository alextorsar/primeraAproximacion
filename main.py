import DataExtractor
from AlgoritmoVecinosCercanos import AlgoritmoVecinosCercanos

df_users = DataExtractor.DataExtractor.obtenerDataFrameUsuarios()
df_restaurants = DataExtractor.DataExtractor.obtenerDataFrameRestaurantes()
df_ratings = DataExtractor.DataExtractor.obtenerDataFrameReviews()
df_users_operacionales = DataExtractor.DataExtractor.obtenerDataFrameUsuariosOperacionales()


algoritmoVecinosCercanos = AlgoritmoVecinosCercanos(df_ratings, df_users, df_restaurants, df_users_operacionales)
algoritmoVecinosCercanos.ejecutarAlgoritmo()
algoritmoVecinosCercanos.almacenarRecomendacionesEnBD()



