import threading

import pymysql


class CreadorRecomendacionesItemBased:

    def __init__(self, df_restaurants):
        self.df_restaurants = df_restaurants
        self.connection = pymysql.connect(host='192.168.1.21', port=3306, user='administrador', password='password',
                                          db='bd_relacional')

    def insertarRestaurante(self, restaurante1, restaurante2, distancia):
        try:
            sql = "INSERT INTO `similitudrestaurantes` (`restaurante1`, `restaurante2`, `similitud`) VALUES (%s, %s, %s)"
            cursor = self.connection.cursor()
            cursor.execute(sql, (restaurante1, restaurante2, distancia))
            self.connection.commit()
        except Exception as exc:
            print(exc)

    def cerrarConexion(self):
        self.connection.close()

    def ejecutarInsercion(self, matrizDistancias, matrizIndices):
        hilos = []
        self.limpiarRecomendaciones()
        for fila in range(len(matrizIndices)):
            for columna in range(len(matrizIndices[0])):
                hilo = threading.Thread(target=self.ejecutar(fila, columna, matrizIndices, matrizDistancias))
                hilo.start()
                hilos.append(hilo)
        for hilo in hilos:
            hilo.join()
        self.cerrarConexion()

    def limpiarRecomendaciones(self):
        try:
            cursor = self.connection.cursor()
            sql = "DELETE FROM `similitudrestaurantes`"
            cursor.execute(sql)
            self.connection.commit()
        except Exception as exc:
            print(exc)

    def ejecutar(self, fila, columna, matrizIndices, matrizDistancias):
        indiceReal1 = self.df_restaurants[fila]['oid']
        #indiceReal1 = self.df_restaurants.loc[fila][0]
        indiceReal2 = self.df_restaurants[matrizIndices[fila][columna]]['oid']
        #indiceReal2 = self.df_restaurants.loc[matrizIndices[fila][columna]][0]
        #indiceReal1 = indiceReal1["$oid"]
        #indiceReal2 = indiceReal2["$oid"]
        similitud = matrizDistancias[fila][columna]
        self.insertarRestaurante(indiceReal1, indiceReal2, similitud)
