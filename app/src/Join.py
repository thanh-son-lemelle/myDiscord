from .Db import Db

class Join:
    def __init__(self) -> None:
        self.db = Db()
        

    def get_message_and_user(self):
        query = 'SELECT user.name AS username , message.content , message.date_time FROM message INNER JOIN user ON message.userID = user.userID ORDER BY message.date_time ASC;'
        return self.db.executeQuery(query)
    
    def get_user_server_server_member_by_userID(self, userID, server_name=None):
        if server_name:
            query = '''
                SELECT u.userID, u.name, u.firstname, s.serverID, s.server_name, s.description, sm.role
                FROM user u
                JOIN server_member sm ON u.userID = sm.userID
                JOIN server s ON sm.serverID = s.serverID
                WHERE u.userID = %s
                AND s.server_name = %s;
            '''
            params = (userID, server_name)
        else:
            query = '''
                SELECT u.userID, u.name, u.firstname, s.serverID, s.server_name, s.description, sm.role
                FROM user u
                JOIN server_member sm ON u.userID = sm.userID
                JOIN server s ON sm.serverID = s.serverID
                WHERE u.userID = %s;
            '''
            params = (userID,)
        
        return self.db.executeQuery(query, params)
    
    def get_user_server_by_userID(self, userID, server_name=None):
        if server_name:
            query = '''
                SELECT u.userID, u.name, u.firstname, s.serverID, s.server_name, s.description
                FROM user u
                JOIN server s ON u.userID = s.owner
                WHERE u.userID = %s
                AND s.server_name = %s;
            '''
            params = (userID, server_name)
        else:
            query = '''
                SELECT u.userID, u.name, u.firstname, s.serverID, s.server_name, s.description
                FROM user u
                JOIN server s ON u.userID = s.owner
                WHERE u.userID = %s;
            '''
            params = (userID,)
        return self.db.executeQuery(query, params)
        