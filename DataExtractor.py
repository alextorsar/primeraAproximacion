import pandas as pd


class DataExtractor:
    RUTA_JSON_USUARIOS = r'RUTA JSON USUARIOS'
    RUTA_JSON_RESTAURANTES = r'RUTA JSON RESTAURANTES'
    RUTA_JSON_REVIEWS = r'RUTA JSON REVIEWS'

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
