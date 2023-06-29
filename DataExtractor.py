import json

import pandas as pd
import requests


class DataExtractor:

    base_url = "https://a87d-2-139-75-100.ngrok-free.app"

    @staticmethod
    def obtenerDataFrameUsuarios():
        url = DataExtractor.base_url + "/algoritmo/usuarios/27"
        response = requests.get(url).text
        json_usuarios = json.loads(response)
        return json_usuarios

    @staticmethod
    def obtenerDataFrameRestaurantes():
        url = DataExtractor.base_url + "/restaurantes_Algoritmo/"
        response = requests.get(url).text
        json_restaurantes = json.loads(response)
        return json_restaurantes


    @staticmethod
    def obtenerDataFrameReviews():
        url = DataExtractor.base_url + "/algoritmo/review/27"
        response = requests.get(url).text
        json_reviews = json.loads(response)
        json_reviews = pd.DataFrame(json_reviews)
        return json_reviews


    @staticmethod
    def obtenerDataFrameUsuariosOperacionales():
        url = DataExtractor.base_url + "/algoritmo/usuarios/operacionales/27"
        response = requests.get(url).text
        json_usuariosOperacionales = json.loads(response)
        return json_usuariosOperacionales

