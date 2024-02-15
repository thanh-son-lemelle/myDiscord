from data.Db import Db
from data.Message import Message
from data.MessageChannel import MessageChannel
from data.Channel import Channel
from data.User import User
from data.Role import Role

from frontend.LoginScreen import LoginScreen
from frontend.MainPage import MainPage
from frontend.Register import Register

class Application:
    def __init__(self) -> None:

        self.login_screen = LoginScreen()
        self.main_Page = MainPage()
        self.register_Page = Register()
        
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
        # display methodes
#===============================================================================


    def displayApp(self):

        while True:
            root =  Application()
            root.login_screen.displayLoginScreen()
            print("Login test dans application:", root.login_screen.get_login())
            if root.login_screen.get_login() == True:
                root.main_Page.display()
                print("test3")
            elif root.login_screen.register:
                root.register_Page.launch()
            break