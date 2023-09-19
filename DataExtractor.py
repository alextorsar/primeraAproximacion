import json

import pandas as pd
import requests


class DataExtractor:

    base_url = "http://localhost:8000"

    @staticmethod
    def obtenerDataFrameUsuarios():
        url = DataExtractor.base_url + "/algoritmo/usuarios/25"
        response =  requests.get(url).text
        json_usuarios = json.loads(response)
        return json_usuarios

    @staticmethod
    def obtenerDataFrameRestaurantes():
        url = DataExtractor.base_url + "/algoritmo/restaurantes/25"
        response = requests.get(url).text
        json_restaurantes = json.loads(response)
        return json_restaurantes


    @staticmethod
    def obtenerDataFrameReviews():
        url = DataExtractor.base_url + "/algoritmo/review/25"
        response =  requests.get(url).text
        json_reviews = json.loads(response)
        json_reviews = pd.DataFrame(json_reviews)
        return json_reviews


    @staticmethod
    def obtenerDataFrameUsuariosOperacionales():
        url = DataExtractor.base_url + "/algoritmo/usuarios/operacionales/25"
        response = requests.get(url).text
        json_usuariosOperacionales = json.loads(response)
        return json_usuariosOperacionales

