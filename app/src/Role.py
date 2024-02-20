from Db import Db

class Role:
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
    
    def create(self, admin, id_user, id_channel):
        query = "INSERT INTO role (admin, id_user, id_channel) VALUES (%s, %s, %s)"
        params = (admin, id_user, id_channel)
        self.db.executeQuery(query, params)
    
    def read(self):
        query = 'SELECT * FROM role'
        return self.db.executeQuery(query)
    
    def update(self, id, admin, id_user, id_channel):
        query = 'UPDATE role SET admin=%s, id_user=%s, id_channel=%s WHERE id=%s'
        params = (admin, id_user, id_channel, id)
        self.db.executeQuery(query, params)
    
    def delete(self, id):
        query = 'DELETE FROM role WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)