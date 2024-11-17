# -*- coding: utf-8 -*-

###########################################
#                 modules                 #
###########################################
from db.connection import connection
###########################################

class UserDB:
    """Représente l'interaction utilisateur avec la base de données."""

    def get_tag(self, id:int) -> str:
        """Obtenir le tag utilisateur clash of clan dans la base de données.
        Args:
            id: identifiant de l'utilisateur discord.
        Returns:
            - Si le tag existe : retourne le tag.
            - Sinon : retourne None.
        """
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT tag FROM user WHERE id=%s", (id,))
        res = cur.fetchone()
        conn.close()
        return None if res == None else res[0]
    
    def set_tag(self, id:int, tag:str) -> None:
        """Modifier le tag utilisateur clash of clan dans la base de données.
        Args:
            id: identifiant de l'utilisateur discord.
            tag: tag utilisateur clash of clan.
        """
        conn = connection()
        cur = conn.cursor()
        cur.execute("UPDATE user SET tag=%s WHERE id=%s", (tag, id,))
        conn.commit()
        conn.close()
    
    def is_user(self, id:int) -> bool:
        """Vérifier si l'utilisateur est présent dans la base de données.
        Args:
            id: identifiant de l'utilisateur discord.
        Returns:
            True si l'utilisateur est dans la base sinon False.
        """
        conn = connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM user WHERE id=%s", (id,))
        res = cur.fetchone()
        conn.close()
        return False if res[0] == 0 else True

    def add_user(self, id:int, tag:str) -> None:
        """Ajouter un utilisateur à la base de données.
        Args:
            id: identifiant de l'utilisateur discord.
            tag: tag utilisateur clash of clan.
        """
        conn = connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO user VALUES (%s, %s)", (id, tag))
        conn.commit()
        conn.close()

    def remove_user(self, id:int) -> None:
        """Supprimer un utilisateur de la base de données.
        Args:
            id: identifiant de l'utilisateur discord.
        """
        conn = connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM user WHERE id=%s", (id,))
        conn.commit()
        conn.close()