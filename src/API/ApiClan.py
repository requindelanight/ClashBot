# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import os
import requests
from dotenv import load_dotenv
###########################################

class ApiClan:
    """Représente l'interation avec un clan via l'API clash of clan.
    Notes:
        - L'API clash of clan est disponible ic : https://developer.clashofclans.com/.
        - J'utilise les requêtes URL afin de récupérer les informations de l'API clash of clan.
        - l'API clash of clan propose également de récupérer les informations avec cURL.
    """

    def __init__(self):
        load_dotenv()
        coc_token = os.getenv('COC_TOKEN')
        self.__headers = {
            "Accept": "application/json",
            "Authorization": "Bearer "+coc_token
        }

    def is_clan(self, response:dict) -> bool:
        """Vérifier si la réponse de la requête a renvoyé un clan.
        Args:
            response: réponse de la requête.
        Returns:
            True si la réponse est un clan sinon False.
        """
        if "reason" in response:
            return False
        return True

    def get_clan(self, clan:str) -> dict:
        """Obtenir les informations concernant un clan.
        Args:
            clan: tag du clan.
        Returns:
            la réponse de la requête.
        """
        response = requests.get(f"https://api.clashofclans.com/v1/clans/%23{clan}", headers=self.__headers)
        return response.json()