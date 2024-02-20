from Db import Db

class Server():
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, server_name, description, owner, server_image, creation_date):
        query = "INSERT INTO server (server_name, description, owner, server_image, creation_date) VALUES (%s, %s, %s, %s, %s)"
        params = (server_name, description, owner, server_image, creation_date)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM server'
        return self.db.executeQuery(query)
    
    def update(self, id, server_name, description, owner, server_image, creation_date):
        query = 'UPDATE server SET server_name=%s, description=%s, owner=%s, server_image=%s, creation_date=%s WHERE id=%s'
        params = (server_name, description, owner, server_image, creation_date, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM server WHERE id=%s'
        params = (id)
        self.db.executeQuery(query, params)