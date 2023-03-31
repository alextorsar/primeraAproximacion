import pymysql
from bson import ObjectId


class RecommendationsCreator:

    def __init__(self, df_ratings, df_users, df_restaurants, df_users_operacionales, matrizRecomendaciones):
        self.df_ratings = df_ratings
        self.df_restaurants = df_restaurants
        self.df_users = df_users
        self.df_users_operacionales = df_users_operacionales
        self.matrizRecomendaciones = matrizRecomendaciones
        self.connection = pymysql.connect(host='localhost', port=3306, user='root', password='Vivaladecima10',
                                          db='bd_relacional')

    def guardarRecomendaciones(self):
        self.limpiarRecomendaciones()
        for i in range(len(self.df_users_operacionales)):
            usuarioBuscado = self.df_users[self.df_users['_id'] == self.df_users_operacionales.iloc[i]['_id']]
            self.guardarRecomendacionesUsuario(usuarioBuscado)
        self.connection.close()

    def guardarRecomendacionesUsuario(self, usuario):
        idArtificialUsuario = int(usuario.iloc[0]['id'])
        idBDUsuario = str(usuario.iloc[0]['_id'])
        recomendacionesUsuario = self.matrizRecomendaciones.argsort()[idArtificialUsuario]
        for i, idArtificialRestaurante in enumerate(recomendacionesUsuario[-30:]):
            idBDRestaurante = str((self.df_restaurants[self.df_restaurants['id'] == idArtificialRestaurante]).iloc[0]["_id"])
            indice = self.matrizRecomendaciones[idArtificialUsuario][idArtificialRestaurante]
            self.insertarRecomendacionBD(idBDUsuario, idBDRestaurante, indice)

    def insertarRecomendacionBD(self, idBDUsuario, idBDRestaurante, indice):
        cursor = self.connection.cursor()
        nuevoId = idBDUsuario[10:34]
        nuevoIdRestaurante = idBDRestaurante[10:34]
        try:
            sql = "INSERT INTO `esrecomendadovecinoscercanos` (`usuario_idUsuario`, `restaurante_idrestaurante`, `indiceRecomendacion`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (
                nuevoId,
                nuevoIdRestaurante,
                indice
            ))
            self.connection.commit()
        except Exception as exc:
            print(exc)

    def limpiarRecomendaciones(self):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM `esrecomendadovecinoscercanos`"
            cursor.execute(sql)
            self.connection.commit()
        except Exception as exc:
            print(exc)
