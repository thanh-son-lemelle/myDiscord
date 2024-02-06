from Db import DB

class Message_salon():
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, id_user, id_salon, message):
        query = "INSERT INTO message_salon (id_user, id_salon, message) VALUES (%s, %s, %s)"
        params = (id_user, id_salon, message)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM message_salon'
        return self.db.executeQuery(query)

    def update(self, id, id_user, id_salon, message):
        query = 'UPDATE message_salon SET id_user=%s, id_salon=%s, message=%s WHERE id=%s'
        params = (id_user, id_salon, message, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM message_salon WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
        