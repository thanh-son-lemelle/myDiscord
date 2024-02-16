import mysql.connector
from mysql.connector import errorcode

class Db:
    def __init__(self, host, user, passwd, db,port = 3306):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.port = port
    
    def connect(self):
        if self.db is not None:
            try:
                self.conn = mysql.connector.connect(
                                                        host=self.host, 
                                                        user=self.user, 
                                                        passwd=self.passwd, 
                                                        db=self.db,
                                                        port = self.port
                    
                                                    )
                self.cursor = self.conn.cursor()
            except mysql.connector.Error as e:
                print(e)
                if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
                elif e.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                    createDb = input("Do you want to create the database? (y/n): ")
                    if createDb == 'y':
                        self.db = None
                        self.createDb()
                    else:
                        exit()
        elif self.db == None:
            try:
                self.conn = mysql.connector.connect(
                                                        host=self.host, 
                                                        user=self.user, 
                                                        passwd=self.passwd,
                                                        db = 'mysql'
                                                    )
                self.cursor = self.conn.cursor()
            except mysql.connector.Error as e:
                print(e)
                if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with your user name or password")
        

    def disconnect(self):
        self.conn.close()

    def executeQuery(self, query, params=None):
        self.connect()
        self.cursor.execute(query, params or ())
        result = self.cursor.fetchall()
        self.conn.commit()
        self.disconnect()
        return result
    
    def createDb(self):
        self.connect()
        self.cursor.execute("CREATE DATABASE myDiscord")
        self.disconnect()
        print("Database created successfully")
        self.db = 'myDiscord'
        self.createTables()
    
    def createTables(self):
        self.connect()
        query = """CREATE TABLE user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            name VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            email VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""" 
        self.executeQuery(query)
        query = """CREATE TABLE message_salon (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_user INT NOT NULL,
            id_salon INT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.executeQuery(query)
        query = """CREATE TABLE salon (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.executeQuery(query)
        query = """ CREATE TABLE message (
            id INT AUTO_INCREMENT PRIMARY KEY,
            id_destinataire INT NOT NULL,
            id_expediteur INT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
        self.executeQuery(query)
        query = """CREATE TABLE role (
            id INT AUTO_INCREMENT PRIMARY KEY,
            admin BOOLEAN NOT NULL,
            id_user INT NOT NULL,
            id_salon INT NOT NULL
        )"""
        self.executeQuery(query)
        print("Tables created successfully")

db = Db('localhost', 'root', 'hR!9gT+pLq6s', 'myDiscord')
db.connect()