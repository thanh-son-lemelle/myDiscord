from Db import Db

class MessageChannel():
    def __init__(self) -> None:
        self.db = Db(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, id_user, id_channel, message):
        query = "INSERT INTO message_channel (id_user, id_channel, message) VALUES (%s, %s, %s)"
        params = (id_user, id_channel, message)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM message_channel'
        return self.db.executeQuery(query)

    def update(self, id, id_user, id_channel, message):
        query = 'UPDATE message_channel SET id_user=%s, id_channel=%s, message=%s WHERE id=%s'
        params = (id_user, id_channel, message, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM message_channel WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)
        