from Db import Db

class Join:
    def __init__(self) -> None:
        self.db = Db(
                        host = '10.10.92.164',
                        user = 'adminmydiscord',
                        passwd = 'Np/yy7>FD35@',
                        db = 'myDiscord'
                    )
        

    def get_message_and_user(self):
        query = 'SELECT user.name AS username , message.content , message.date_time FROM message INNER JOIN user ON message.userID = user.userID'
        return self.db.executeQuery(query)
        