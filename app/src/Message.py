from .Db import Db

class Message():
    def __init__(self) -> None:
        self.db = Db()
        
    def create(self,content, userID, channelID, type):
        query = "INSERT INTO message (content, userID, channelID, type) VALUES (%s, %s, %s, %s)"
        params = (content, userID, channelID, type)
        self.db.executeQuery(query, params)
    
    def read(self):
        query = 'SELECT * FROM message'
        return self.db.executeQuery(query)
    
    def update(self, id, content):
        query = 'UPDATE message SET content=%s WHERE id=%s'
        params = (content, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM message WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)


    def read_message(self):
        query = 'SELECT content FROM message'
        return self.db.executeQuery(query)


    def read_time(self):
        query = 'SELECT date_time FROM message'
        return self.db.executeQuery(query)
    

    def read_user_id(self):
        query = 'SELECT userID FROM message'
        return self.db.executeQuery(query)
    
    
    




    