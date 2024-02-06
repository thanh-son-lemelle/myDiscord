from Data.Db import DB
from Data.Message import Message
from Data.Message_salon import Message_salon
from Data.Role import Role
from Data.Salon import Salon
from Data.User import User


class Root:
    def __init__(self) -> None:
        
        self.message = Message()
        self.message_salon = Message_salon()
        self.role = Role()
        self.salon = Salon()
        self.user = User()

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
    def createMessage_salon(self, id_user, id_salon, message):
        self.message_salon.create(id_user, id_salon, message)
    
    def readMessage_salon(self):
        return self.message_salon.read()
    
    def updateMessage_salon(self, id, id_user, id_salon, message):
        self.message_salon.update(id, id_user, id_salon, message)

    def deleteMessage_salon(self, id):
        self.message_salon.delete(id)
#===============================================================================
        
#===============================================================================
        # role
#===============================================================================
    def createRole(self, admin, id_user, id_salon):
        self.role.create(admin, id_user, id_salon)
    
    def readRole(self):
        return self.role.read()
    
    def updateRole(self, id, admin, id_user, id_salon):
        self.role.update(id, admin, id_user, id_salon)

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
        # user
#===============================================================================
    def createUser(self, nom, prenom, email, password):
        self.user.create(nom, prenom, email, password)
    
    def readUser(self):
        return self.user.read()
    
    def updateUser(self, id, nom, prenom, email, password):
        self.user.update(id, nom, prenom, email, password)

    def deleteUser(self, id):
        self.user.delete(id)
#===============================================================================
        
