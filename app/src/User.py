from Db import Db

class User:
    def __init__(self) -> None:
        self.db = Db(
                        host = '10.10.82.210',
                        user = 'lakhezoum',
                        passwd = ':)?uX3v2E8mH',
                        db = 'myDiscord'
                    )
        
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
        return self.db.executeQuery(query, params)
