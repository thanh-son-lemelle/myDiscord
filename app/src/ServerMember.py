from Db import Db

class ServerMember:
    def __init__(self) -> None:
        self.db = Db(
                        host = '10.10.82.210',
                        user = 'adminmydiscord',
                        passwd = 'Np/yy7>FD35@',
                        db = 'myDiscord'
                    )
        
    def create(self, userID, serverID, role):
        query = "INSERT INTO server_member (userID, serverID, role) VALUES (%s, %s, %s)"
        params = (userID, serverID, role)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM server_member'
        return self.db.executeQuery(query)
    
    def update(self, userID, serverID, role, membershipID):
        query = 'UPDATE server_member SET userID=%s, serverID=%s, role=%s WHERE membershipID=%s'
        params = (userID, serverID, role, membershipID)
        self.db.executeQuery(query, params)

    def delete(self, membershipID):
        query = 'DELETE FROM server_member WHERE membershipID=%s'
        params = (membershipID)
        self.db.executeQuery(query, params)