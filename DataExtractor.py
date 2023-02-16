import pandas as pd


class DataExtractor:
    RUTA_JSON_USUARIOS = r'users.json'
    RUTA_JSON_RESTAURANTES = r'restaurants.json'
    RUTA_JSON_REVIEWS = r'reviews.json'

    @staticmethod
    def obtenerDataFrameUsuarios():
        df_users = pd.read_json(DataExtractor.RUTA_JSON_USUARIOS, dtype='U')
        return df_users

    @staticmethod
    def obtenerDataFrameRestaurantes():
        df_restaurantes = pd.read_json(DataExtractor.RUTA_JSON_RESTAURANTES)
        return df_restaurantes

    @staticmethod
    def obtenerDataFrameReviews():
        df_ratings = pd.read_json(DataExtractor.RUTA_JSON_REVIEWS, dtype='U')
        return df_ratings
