from .Db import DB

class Utilisateur:
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, nom, prenom, password, mail):
        query = "INSERT INTO user (nom, prenom, password, mail) VALUES (%s, %s, %s, %s)"
        params = (nom, prenom, password, mail)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM user'
        return self.db.executeQuery(query)
    
    def update(self, id, nom, prenom, password, mail):
        query = 'UPDATE user SET nom=%s, prenom=%s, password=%s, mail=%s WHERE id=%s'
        params = (nom, prenom, password, mail, id)
        self.db.executeQuery(query, params)
    
    def delete(self, id):
        query = 'DELETE FROM user WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def utilisateurName (self, id):
        query = 'SELECT name FROM user WHERE id=%s'
        params =(id,)
        return self.db.executeQuery(query, params)

    def utilisateurAllmail (self):
        query = 'SELECT mail FROM user'
        return self.db.executeQuery(query)

    def utilisateurAllName (self):
        query = 'SELECT name FROM user'
        return self.db.executeQuery(query)

    def allpassword (self):
        query = 'SELECT password FROM user'
        return self.db.executeQuery(query)
    
        

