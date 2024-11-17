# -*- coding: utf-8 -*-

###########################################
#                libraries                #
###########################################
import os
import requests
from dotenv import load_dotenv
###########################################

class ApiPlayer:
    """Représente l'interation avec un joueur via l'API clash of clan.
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

    def is_player(self, response:dict) -> bool:
        """Vérifier si la réponse de la requête a renvoyé un joueur.
        Args:
            response: réponse de la requête.
        Returns:
            True si la réponse est un joueur sinon False.
        """
        if "reason" in response:
            return False
        return True

    def is_player_have_clan(self, response:str) -> bool:
        """Vérifier si un joueur a un clan.
        Args:
            player: tag du joueur.
        Returns:
            True si le joueur a un clan sinon False.
        """
        if self.is_player(response):
            return False if response["clan"] == {} else True
        return False

    def get_player(self, player:str) -> dict:
        """Obtenir les informations concernant un joueur.
        Args:
            player: tag du joueur.
        Returns:
            la réponse de la requête.
        """
        response = requests.get(f"https://api.clashofclans.com/v1/players/%23{player}", headers=self.__headers)
        return response.json()