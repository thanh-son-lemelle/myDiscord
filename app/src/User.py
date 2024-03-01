from .Db import Db

class User:
    def __init__(self) -> None:
        self.db = Db()
        
    def create(self, name, firstname, password, mail):
        query = "INSERT INTO user (name, firstname, password, mail) VALUES (%s, %s, %s, %s)"
        params = (name, firstname, password, mail)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM user'
        return self.db.executeQuery(query)
    
    def update(self, id, name, firstname, password, mail):
        query = 'UPDATE user SET name=%s, firstname=%s, password=%s, mail=%s WHERE id=%s'
        params = (name, firstname, password, mail, id)
        self.db.executeQuery(query, params)
    
    def delete(self, id):
        query = 'DELETE FROM user WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def userName (self, id):
        query = 'SELECT name FROM user WHERE id=%s'
        params =(id,)
        return self.db.executeQuery(query, params)
    
    def allowAccess(self, mail, password):
        query = 'SELECT * FROM user WHERE mail=%s AND password=%s'
        params = (mail, password)
        return self.db.executeQuery(query, params)
    
    def getUserMail(self, mail):
        query = 'SELECT mail FROM user WHERE mail=%s'
        params = (mail,)
    
    #===========================================================================
    # methodes for authentication Service
    #===========================================================================
    
    def get_user_by_username(self, username):
        query = "SELECT * FROM `user` WHERE `name` = %s"
        params = (username,)
        result = self.db.executeQuery(query, params)
        if result:
            return result[0]
        else:
            return None
    
    def get_user_by_mail(self, mail):
        query = 'SELECT * FROM user WHERE mail=%s'
        params = (mail,)
        return self.db.executeQuery(query, params)
    
    def save_auth_token(self, usermail, token):
        query = "UPDATE `user` SET `auth_token` = %s WHERE `mail` = %s"
        params = (token, usermail)
        self.db.executeQuery(query, params)

    def check_auth_token(self, token):
        query = "SELECT * FROM `user` WHERE `auth_token` = %s"
        params = (token,)
        return self.db.executeQuery(query, params)
    

    def get_userName (self):
        query = 'SELECT name FROM user'
        return self.db.executeQuery(query)