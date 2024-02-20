from Db import Db

class Message():
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self,content):
        query = "INSERT INTO message (content) VALUES (%s)"
        params = (content,)
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
    
    
    




    