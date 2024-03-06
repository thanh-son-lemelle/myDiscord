from .Db import Db

class Channel:
    def __init__(self) -> None:
        self.db = Db()
        
    def create(self, channel_name, channel_type):
        query = "INSERT INTO channel (channel_name, channel_type) VALUES (%s, %s)"
        params = (channel_name, channel_type)
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

    def get_channelID_by_channel_name(self, channel_name):
        query = 'SELECT channelID FROM channel WHERE channel_name=%s'
        params = (channel_name,)
        return self.db.executeQuery(query, params)