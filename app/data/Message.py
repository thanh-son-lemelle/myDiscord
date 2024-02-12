from Db import DB

class Message():
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self,contenu):
        query = "INSERT INTO message (contenu) VALUES (%s)"
        params = (contenu,)
        self.db.executeQuery(query, params)
    
    def read(self):
        query = 'SELECT * FROM message'
        return self.db.executeQuery(query)
    
    def update(self, id, contenu):
        query = 'UPDATE message SET contenu=%s WHERE id=%s'
        params = (contenu, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM message WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)


    def read_message(self):
        query = 'SELECT contenu FROM message'
        return self.db.executeQuery(query)



    def read_time(self):
        query = 'SELECT date_heure FROM message'
        return self.db.executeQuery(query)
    

    def read_user_id(self):
        query = 'SELECT utilisateurID FROM message'
        return self.db.executeQuery(query)
    
    
    




    