from .Db import Db

#À modifier car pas à jour avec la DB

class Channel:
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, name):
        query = "INSERT INTO channel (name) VALUES (%s)"
        params = (name)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM channel'
        return self.db.executeQuery(query)
    
    def update(self, id, name):
        query = 'UPDATE channel SET name=%s WHERE id=%s'
        params = (name, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM channel WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

        