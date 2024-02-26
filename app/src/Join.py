from .Db import Db

class Join:
    def __init__(self) -> None:
        self.db = Db()
        

    def get_message_and_user(self):
        query = 'SELECT user.name AS username , message.content , message.date_time FROM message INNER JOIN user ON message.userID = user.userID'
        return self.db.executeQuery(query)
        