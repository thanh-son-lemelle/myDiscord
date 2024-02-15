from data.Db import DB
from data.Message import Message
from data.Message_salon import Message_salon
from data.Role import Role
from data.Salon import Salon
from data.Utilisateur import Utilisateur

from frontend.LoginScreen import LoginScreen
from frontend.MainPage import Mainpage
from frontend.register import Register

class Root:
    def __init__(self) -> None:

        self.login_screen = LoginScreen()
        self.mainPage = Mainpage()
        self.registerPage = Register()
        
        self.message = Message()
        self.message_salon = Message_salon()
        self.role = Role()
        self.salon = Salon()
        self.utilisateur = Utilisateur()

#===============================================================================
        # message 
#===============================================================================
    def createMessage(self, id_destinataire, id_expediteur, message):
        self.message.create(id_destinataire, id_expediteur, message)
    
    def readMessage(self):
        return self.message.read()
    
    def updateMessage(self, id, id_destinataire, id_expediteur, message):
        self.message.update(id, id_destinataire, id_expediteur, message)

    def deleteMessage(self, id):
        self.message.delete(id)
#===============================================================================

#===============================================================================
        # message_salon
#===============================================================================
    def createMessage_salon(self, id_utilisateur, id_salon, message):
        self.message_salon.create(id_utilisateur, id_salon, message)
    
    def readMessage_salon(self):
        return self.message_salon.read()
    
    def updateMessage_salon(self, id, id_utilisateur, id_salon, message):
        self.message_salon.update(id, id_utilisateur, id_salon, message)

    def deleteMessage_salon(self, id):
        self.message_salon.delete(id)
#===============================================================================
        
#===============================================================================
        # role
#===============================================================================
    def createRole(self, admin, id_utilisateur, id_salon):
        self.role.create(admin, id_utilisateur, id_salon)
    
    def readRole(self):
        return self.role.read()
    
    def updateRole(self, id, admin, id_utilisateur, id_salon):
        self.role.update(id, admin, id_utilisateur, id_salon)

    def deleteRole(self, id):
        self.role.delete(id)
#===============================================================================

#===============================================================================
        # salon
#===============================================================================
    def createSalon(self, nom):
        self.salon.create(nom)
    
    def readSalon(self):
        return self.salon.read()
    
    def updateSalon(self, id, nom):
        self.salon.update(id, nom)

    def deleteSalon(self, id):
        self.salon.delete(id)
#===============================================================================
    
#===============================================================================
        # utilisateur
#===============================================================================
    def createutilisateur(self, nom, prenom, email, password):
        self.utilisateur.create(nom, prenom, email, password)
    
    def readutilisateur(self):
        return self.utilisateur.read()
    
    def updateutilisateur(self, id, nom, prenom, email, password):
        self.utilisateur.update(id, nom, prenom, email, password)

    def deleteutilisateur(self, id):
        self.utilisateur.delete(id)

    def returnNameUtlissateur(self,id):
        return self.utilisateur.utilisateurName(id)
    
    def returnAllName(self):
        return self.utilisateur.utilisateurAllName()
    
    def returnAllMail(self):
        return self.utilisateur.utilisateurAllmail()
    
    def returnAllPassword(self):
        return self.utilisateur.allpassword()
    
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
            root = Root()
            root.login_screen.displayLoginScreen()
            print("Login test dans root:", root.login_screen.get_login())
            if root.login_screen.get_login() == True:
                root.mainPage.display()
                print("test3")
            elif root.login_screen.register:
                root.registerPage.launch()
            break