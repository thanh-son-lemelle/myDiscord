import bcrypt
import uuid
import hashlib

from .Model import Model

class Service:
    def __init__(self):
        self.auth = False
        self.model = Model()

    #===========================================================================
    # methodes for authentication
    #===========================================================================

    def login(self, username, password, remember_me=False):

        if self.validate_credentials(username, password):
            if remember_me:
                auth_token = str(uuid.uuid4())
                self.model.save_auth_token(username, auth_token)

            self.auth = True

        else:
            print('Wrong username or password')
        return self.auth

    def validate_credentials(self, username, password):
        user = self.model.get_user_by_username(username)
        if user:
            #! a garder pour quand les mots de passe seront hashés
            # Vérifiez le mot de passe hashé avec bcrypt
            hashed_password = user[1]
            '''if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
                # Mot de passe correct
                return True'''
            if password == hashed_password:
                return True
        # Nom d'utilisateur introuvable ou mot de passe incorrect
        return False

    def logout(self):
        self.auth = False

    def isAuth(self):
        return self.auth
    