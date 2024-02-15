from .Db import DB

class Salon:
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, nom):
        query = "INSERT INTO salon (nom) VALUES (%s)"
        params = (nom,)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM salon'
        return self.db.executeQuery(query)
    
    def update(self, id, nom):
        query = 'UPDATE salon SET nom=%s WHERE id=%s'
        params = (nom, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM salon WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

        