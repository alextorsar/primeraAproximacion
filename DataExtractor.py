import json

import pandas as pd
import requests


class DataExtractor:

    base_url = "http://localhost:8000"

    RUTA_JSON_USUARIOS = r'users.json'
    RUTA_JSON_RESTAURANTES = r'restaurants.json'
    RUTA_JSON_REVIEWS = r'reviews.json'
    RUTA_JSON_USUARIOS_OPERACIONALES = "users_operacional.json"

    @staticmethod
    def obtenerDataFrameUsuarios():
        url = DataExtractor.base_url + "/algoritmo/usuarios/27"
        response = requests.get(url).text
        json_usuarios = json.loads(response)
        return json_usuarios
        #df_users = pd.read_json(DataExtractor.RUTA_JSON_USUARIOS, dtype='U')
        #return df_users

    @staticmethod
    def obtenerDataFrameRestaurantes():
        url = DataExtractor.base_url + "/restaurantes_Algoritmo/"
        response = requests.get(url).text
        json_restaurantes = json.loads(response)
        return json_restaurantes
        #df_restaurantes = pd.read_json(DataExtractor.RUTA_JSON_RESTAURANTES)
        #return df_restaurantes

    @staticmethod
    def obtenerDataFrameReviews():
        url = DataExtractor.base_url + "/algoritmo/review/50"
        response = requests.get(url).text
        json_reviews = json.loads(response)
        json_reviews = pd.DataFrame(json_reviews)
        return json_reviews
        #df_ratings = pd.read_json(DataExtractor.RUTA_JSON_REVIEWS, dtype='U')
        #return df_ratings

    @staticmethod
    def obtenerDataFrameUsuariosOperacionales():
        url = DataExtractor.base_url + "/algoritmo/usuarios/operacionales/{count]?count=0"
        response = requests.get(url).text
        json_usuariosOperacionales = json.loads(response)
        return json_usuariosOperacionales
        #df_users_operacionales = pd.read_json(DataExtractor.RUTA_JSON_USUARIOS_OPERACIONALES, dtype='U')
        #print(df_users_operacionales)
        #return df_users_operacionales
