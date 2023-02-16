import DataExtractor
from AlgoritmoVecinosCercanos import AlgoritmoVecinosCercanos

df_users = DataExtractor.DataExtractor.obtenerDataFrameUsuarios()
df_restaurants = DataExtractor.DataExtractor.obtenerDataFrameRestaurantes()
df_ratings = DataExtractor.DataExtractor.obtenerDataFrameReviews()

algoritmoVecinosCercanos = AlgoritmoVecinosCercanos(df_ratings, df_users, df_restaurants)
algoritmoVecinosCercanos.ejecutarAlgoritmo()
restaurantesRecomendados = algoritmoVecinosCercanos.obtenerRestaurantesRecomendados('117867348882605384904', 3)

for i, idRes in restaurantesRecomendados:
    restaurante = df_restaurants[df_restaurants['id'] == (idRes + 1)]
    print(restaurante['name'])
