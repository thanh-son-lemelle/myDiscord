from .Db import Db

class ServerMember:
    def __init__(self) -> None:
        self.db = Db()
        
    def create(self, userID, serverID, role, channelID):
        query = "INSERT INTO server_member (userID, serverID, role, channelID) VALUES (%s, %s, %s, %s)"
        params = (userID, serverID, role, channelID)
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