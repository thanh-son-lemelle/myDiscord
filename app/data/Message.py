from Db import DB

class Message():
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, id_destinataire, id_expediteur, message):
        query = "INSERT INTO message (id_destinataire, id_expediteur, message) VALUES (%s, %s, %s)"
        params = (id_destinataire, id_expediteur, message)
        self.db.executeQuery(query, params)
    
    def read(self):
        query = 'SELECT * FROM message'
        return self.db.executeQuery(query)
    
    def update(self, id, id_destinataire, id_expediteur, message):
        query = 'UPDATE message SET id_destinataire=%s, id_expediteur=%s, message=%s WHERE id=%s'
        params = (id_destinataire, id_expediteur, message, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM message WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)


    def read_message(self):
        query = 'SELECT message FROM message'
        return self.db.executeQuery(query)



    def read_time(self):
        query = 'SELECT created_at FROM message'
        return self.db.executeQuery(query)
    

    




    