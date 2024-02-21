from Db import Db
from Message import Message
from MessageChannel import MessageChannel
from Channel import Channel
from User import User
from Role import Role

from LoginScreen import LoginScreen
from MainPage import MainPage
from Register import Register
from Screen import Screen

class Application:
    def __init__(self) -> None:

        self.screen = Screen()
        self.message = Message()
        self.message_channel = MessageChannel()
        self.role = Role()
        self.channel = Channel()
        self.user = User()

#===============================================================================
        # message 
#===============================================================================
    def createMessage(self, id_receiver, id_sender, message):
        self.message.create(id_receiver, id_sender, message)
    
    def readMessage(self):
        return self.message.read()
    
    def updateMessage(self, id, id_receiver, id_sender, message):
        self.message.update(id, id_receiver, id_sender, message)

    def deleteMessage(self, id):
        self.message.delete(id)
#===============================================================================

#===============================================================================
        # message_channel
#===============================================================================
    def createMessage_channel(self, id_user, id_channel, message):
        self.message_channel.create(id_user, id_channel, message)
    
    def readMessage_channel(self):
        return self.message_channel.read()
    
    def updateMessage_channel(self, id, id_user, id_channel, message):
        self.message_channel.update(id, id_user, id_channel, message)

    def deleteMessage_channel(self, id):
        self.message_channel.delete(id)
#===============================================================================
        
#===============================================================================
        # role
#===============================================================================
    def createRole(self, admin, id_user, id_channel):
        self.role.create(admin, id_user, id_channel)
    
    def readRole(self):
        return self.role.read()
    
    def updateRole(self, id, admin, id_user, id_channel):
        self.role.update(id, admin, id_user, id_channel)

    def deleteRole(self, id):
        self.role.delete(id)
#===============================================================================

#===============================================================================
        # channel
#===============================================================================
    def createChannel(self, name):
        self.channel.create(name)
    
    def readChannel(self):
        return self.channel.read()
    
    def updateChannel(self, id, name):
        self.channel.update(id, name)

    def deleteChannel(self, id):
        self.channel.delete(id)
#===============================================================================
    
#===============================================================================
        # user
#===============================================================================
    def createUser(self, name, firstname, email, password):
        self.user.create(name, firstname, email, password)
    
    def readUser(self):
        return self.user.read()
    
    def updateUser(self, id, name, firstname, email, password):
        self.user.update(id, name, firstname, email, password)

    def deleteUser(self, id):
        self.user.delete(id)

    def returnNameUser(self,id):
        return self.user.userName(id)
    
    def returnAllName(self):
        return self.user.userAllName()
    
    def returnAllMail(self):
        return self.user.userAllmail()
    
    def returnAllPassword(self):
        return self.user.allpassword()
    
#===============================================================================

#===============================================================================
        # Variables for the frontend
#===============================================================================
    
    def stockMdpetMail(self):
        listeMail =[]
        listePassword =[]
        listeMail = self.returnAllName()
        listePassword = self.returnAllPassword()
        return listeMail, listePassword
    

#===============================================================================
        # treating input
#===============================================================================
    def givingPermission(self):
        allUser = self.readUser()
        for user in allUser:
            if user[3] == self.login_screen.get_user() and user[4] == self.login_screen.get_password():
                return user[0]
            

    def show_mess(self):
        self.screen.main_page.get_message(self.returnAllMail())
            
    
        

#===============================================================================
        # display methodes
#===============================================================================


"""    def displayApp(self):

        while True:
            root =  Application()
            name , paswd = root.login_screen.displayLoginScreen()
            print (name, paswd)

            if root.login_screen.get_login() == True:
                root.main_Page.display()
                print("test3")
            elif root.login_screen.register:
                name, firstname, email, password = root.register_Page.launch()

            print("Nom:", name)
            print("Prénom:", firstname)
            print("Email:", email)
            print("Mot de passe:", password)
            break"""



