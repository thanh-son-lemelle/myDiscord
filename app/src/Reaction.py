from Db import Db

class Reaction():
    def __init__(self) -> None:
        self.db = Db(
                        host = '10.10.82.210',
                        user = 'adminmydiscord',
                        passwd = 'Np/yy7>FD35@',
                        db = 'myDiscord'
                    )
        
    def create(self, emoji, messageID, userID):
        query = "INSERT INTO message_channel (reactionID, emoji, messageID, userID) VALUES (%s, %s, %s, %s)"
        params = (emoji, messageID, userID)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM message_channel'
        return self.db.executeQuery(query)

    def update(self, reactionID, emoji, messageID, userID):
        query = 'UPDATE message_channel SET emoji=%s, messageID=%s, userID=%s WHERE reactionID=%s'
        params = (emoji, messageID, userID, reactionID)
        self.db.executeQuery(query, params)

    def delete(self, reactionID):
        query = 'DELETE FROM message_channel WHERE reactionID=%s'
        params = (reactionID)
        self.db.executeQuery(query, params)