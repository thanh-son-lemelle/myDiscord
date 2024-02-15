from .Db import DB

class Creation:
    def __init__(self) -> None:
        self.db = DB(
                        host = 'localhost',
                        user = 'root',
                        passwd = 'hR!9gT+pLq6s',
                        db = 'myDiscord'
                    )
        
    def create(self, username, name, lastname, email, password):
        query = "INSERT INTO creation (username) VALUES (%s), (name) VALUES (%s), (lastname) VALUES (%s), (email) VALUES (%s), (password) VALUES (%s)"
        params = (username, name, lastname, email, password)
        self.db.executeQuery(query, params)

    def read(self):
        query = 'SELECT * FROM creation'
        return self.db.executeQuery(query)
    
    def update(self, id, name):
        query = 'UPDATE creation SET name=%s WHERE id=%s'
        params = (name, id)
        self.db.executeQuery(query, params)

    def delete(self, id):
        query = 'DELETE FROM creation WHERE id=%s'
        params = (id,)
        self.db.executeQuery(query, params)

