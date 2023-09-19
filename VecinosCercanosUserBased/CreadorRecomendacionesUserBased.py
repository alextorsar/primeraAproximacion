import threading

import pymysql


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
        hilos = []
        self.limpiarRecomendaciones()
        for i in range(len(self.df_users_operacionales)):
            for j in range(len(self.df_users)):
                if self.df_users[j]['oid'] == self.df_users_operacionales[i]['oid']:
                    usuarioBuscado = self.df_users[j]
                    hilo = threading.Thread(target=self.guardarRecomendacionesUsuario(usuarioBuscado))
                    hilos.append(hilo)
                    hilo.start()
        for hilo in hilos:
            hilo.join()
        self.connection.close()

    def guardarRecomendacionesUsuario(self, usuario):
        hilos = []
        idArtificialUsuario = int(usuario['idArtificial'])
        idBDUsuario = str(usuario['oid'])
        recomendacionesUsuario = self.matrizRecomendaciones.argsort()[idArtificialUsuario]
        for i, idArtificialRestaurante in enumerate(recomendacionesUsuario[(-1*len(self.df_restaurants)):]):
            for j in range(len(self.df_restaurants)):
                if(self.df_restaurants[j]['id'] == idArtificialRestaurante):
                    idBDRestaurante = str(self.df_restaurants[j]['oid'])
                    indice = self.matrizRecomendaciones[idArtificialUsuario][idArtificialRestaurante]
                    hilo = threading.Thread(self.insertarRecomendacionBD(idBDUsuario, idBDRestaurante, indice))
                    hilos.append(hilo)
                    hilo.start()
        for hilo in hilos:
            hilo.join()



    def insertarRecomendacionBD(self, idBDUsuario, idBDRestaurante, indice):
        cursor = self.connection.cursor()
        try:
            sql = "INSERT INTO `esrecomendadovecinoscercanos` (`usuario_idUsuario`, `restaurante_idrestaurante`, `indiceRecomendacion`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (
                idBDUsuario,
                idBDRestaurante,
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
