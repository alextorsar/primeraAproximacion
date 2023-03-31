from MotorVecinosCercanos import MotorRecomendacionVecinosCercanos
from RecommendationsCreator import RecommendationsCreator


class AlgoritmoVecinosCercanos:

    def __init__(self, df_ratings, df_users, df_restaurants, df_users_operacionales):
        self.df_ratings = df_ratings
        self.df_restaurants = df_restaurants
        self.df_users = df_users
        self.motor = MotorRecomendacionVecinosCercanos(self.df_ratings)
        self.df_users_operacionales = df_users_operacionales

    def ejecutarAlgoritmo(self):
        self.motor.generarMatrizSimilitudDeUsuarios()
        self.motor.generarMatrizRecomendaciones()


    def almacenarRecomendacionesEnBD(self):
        self.creadorRecomendaciones = RecommendationsCreator(self.df_ratings, self.df_users, self.df_restaurants,
                                                             self.df_users_operacionales, self.motor.obtenerMatrizRecomendaciones())
        self.creadorRecomendaciones.guardarRecomendaciones()

    def obtenerRestaurantesRecomendados(self, idUsuario, numRestaurantes):
        matrizRecomendaciones = self.motor.obtenerMatrizRecomendaciones()
        usuarioBuscado = self.df_users[self.df_users['reviewerId'] == idUsuario]
        idUsuarioBuscado = int(usuarioBuscado.iloc[0]['id']) - 1
        prediccionesOrdenadas = matrizRecomendaciones.argsort()[idUsuarioBuscado]
        return enumerate(prediccionesOrdenadas[(-1 * numRestaurantes):])
