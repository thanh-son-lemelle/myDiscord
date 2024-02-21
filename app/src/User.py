from Db import Db

class User:
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
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

    def userAllmail (self):
        query = 'SELECT mail FROM user'
        return self.db.executeQuery(query)

    def userAllName (self):
        query = 'SELECT name FROM user'
        return self.db.executeQuery(query)

    def allpassword (self):
        query = 'SELECT password FROM user'
        return self.db.executeQuery(query)
