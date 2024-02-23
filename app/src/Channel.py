from Db import Db

#À modifier car pas à jour avec la DB

class Channel:
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, channel_name, channel_type, server_id):
        query = "INSERT INTO channel (channel_name) VALUES (%s), (channel_type) VALUES (%s), (server_id) VALUES (%s)"
        params = (channel_name, channel_type, server_id)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM channel'
        return self.db.executeQuery(query)
    
    def update(self,id, channel_name, channel_type):
        query = 'UPDATE channel SET channel_name=%s channel_type=%s WHERE id=%s'
        params = (channel_name, channel_type, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM channel WHERE id=%s'
        params = (id)
        self.db.executeQuery(query, params)