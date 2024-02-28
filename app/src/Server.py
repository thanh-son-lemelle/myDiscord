from .Db import Db

class Server():
    def __init__(self) -> None:
        self.db = Db()
        
    def create(self, server_name, description, type, owner, server_image):
        query = "INSERT INTO server (server_name, description, type, owner, server_image) VALUES (%s, %s, %s, %s, %s)"
        params = (server_name, description, type, owner, server_image)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM server'
        return self.db.executeQuery(query)
    
    def update(self, server_name, description, type, owner, server_image, creation_date, serverID):
        query = 'UPDATE server SET server_name=%s, description=%s, type=%s, owner=%s, server_image=%s, creation_date=%s WHERE serverID=%s'
        params = (server_name, description, type, owner, server_image, creation_date, serverID)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM server WHERE serverID=%s'
        params = (id)
        self.db.executeQuery(query, params)