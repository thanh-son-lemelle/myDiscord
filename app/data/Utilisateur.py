from Db import DB

class Utilisateur:
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, username, name, lastname, email, password):
        query = "INSERT INTO user (username, name, lastname, email, password) VALUES (%s, %s, %s, %s, %s)"
        params = (username, name, lastname, email, password)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM user'
        return self.db.executeQuery(query)
    
    def update(self, id, username, name, lastname, email, password):
        query = 'UPDATE user SET username=%s, name=%s, lastname=%s, email=%s, password=%s WHERE id=%s'
        params = (username, name, lastname, email, password, id)
        self.db.executeQuery(query, params)
    
    def delete(self, id):
        query = 'DELETE FROM user WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
    
    def utilisateurName (self, id):
        query = 'SELECT FROM name WHERE id=%s'
        params =(id,)
        self.db.executeQuery(query, params)

    
        

