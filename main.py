import DataExtractor
from VecinosCercanosItemBased.AlgoritmoVecinosCercanosItemBased import AlgoritmoVecinosCercanosItemBased
from VecinosCercanosUserBased.AlgoritmoVecinosCercanosUserBased import AlgoritmoVecinosCercanosUserBased

df_users = DataExtractor.DataExtractor.obtenerDataFrameUsuarios()
df_restaurants = DataExtractor.DataExtractor.obtenerDataFrameRestaurantes()
df_ratings = DataExtractor.DataExtractor.obtenerDataFrameReviews()
df_users_operacionales = DataExtractor.DataExtractor.obtenerDataFrameUsuariosOperacionales()

print("hola")

algoritmos = []
algoritmoVecinosCercanosUserBased = AlgoritmoVecinosCercanosUserBased(df_ratings, df_users, df_restaurants, df_users_operacionales)
algoritmos.append(algoritmoVecinosCercanosUserBased)
algoritmoVecinosCercanosItemBased = AlgoritmoVecinosCercanosItemBased(df_ratings, df_users, df_restaurants)
algoritmos.append(algoritmoVecinosCercanosItemBased)

for algoritmo in algoritmos:
    algoritmo.ejecutarAlgoritmo()
    algoritmo.almacenarRecomendacionesEnBD()





