from Channel import Channel
from ServerMember import ServerMember
from Message import Message
from Reaction import Reaction
from Server import Server
from User import User
from Join import Join

class Model:
    def __init__(self) -> None:

        self.channel = Channel()
        self.server_member = ServerMember()
        self.message = Message()
        self.reaction = Reaction()
        self.server = Server()
        self.user = User()
        self.join = Join()


#===============================================================================
        # channel
#===============================================================================
    def createchannel(self, channel_name, channel_type, serverID):
        self.channel.create(channel_name, channel_type, serverID)
    
    def readchannel(self):
        return self.channel.read()
    
    def updatechannel(self, channelID, channel_name, channel_type, serverID):
        self.channel.update(channelID, channel_name, channel_type, serverID)

    def deletechannel(self, channelID):
        self.channel.delete(channelID)
#===============================================================================
        
#===============================================================================
        # server_member
#===============================================================================
    def createserver_member(self, admin, userID, serverID, role):
        self.server_member.create(admin, userID, serverID, role)
    
    def readserver_member(self):
        return self.server_member.read()
    
    def updateserver_member(self, membershipID, admin, userID, serverID, role):
        self.server_member.update(membershipID, admin, userID, serverID, role)

    def deleteserver_member(self, membershipID):
        self.server_member.delete(membershipID)
#===============================================================================
#===============================================================================
        # message 
#===============================================================================
    def createMessage(self, content, userID, channelID):
        self.message.create(content, userID, channelID)
    
    def readMessage(self):
        return self.message.read()
    
    def updateMessage(self, messageID, content, userID, channelID):
        self.message.update(messageID, content, userID, channelID)

    def deleteMessage(self, messageID):
        self.message.delete(messageID)
#===============================================================================
#===============================================================================
        # reaction
#===============================================================================
    def createReaction(self, emoji, messageID, userID):
        self.reaction.create(emoji, messageID, userID)
    
    def readReaction(self):
        return self.reaction.read()
    
    def updateReaction(self, reactionID, emoji, messageID, userID):
        self.reaction.update(reactionID, emoji, messageID, userID)

    def deleteReaction(self, reactionID):
        self.reaction.delete(reactionID)
#===============================================================================
#===============================================================================
        # server
#===============================================================================
    def createServer(self, server_name, description, owner, server_image):
        self.server.create(server_name, description, owner, server_image)
    
    def readServern(self):
        return self.server.read()
    
    def updateServer(self, serverID, server_name, description, owner, server_image):
        self.server.update(serverID, server_name, description, owner, server_image)

    def deleteServer(self, serverID):
        self.server.delete(serverID)
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
        # join
#===============================================================================


    def read_message_user(self):
        return self.join.get_message_and_user()
    
#===============================================================================

#===============================================================================
        # methodes for the frontend
#===============================================================================
    def allowingAccess(self, email, password):
        return self.user.allowAccess(email, password)
    
    def creatingUser(self, name, firstname, email, password):
        self.user.create(name, firstname, email, password)

    def creatingMessage(self, content, userID, channelID):
        self.message.create(content, userID, channelID)

    def getUserMail(self, mail):
        return self.user.getUserMail(mail)
    
    def check_user_mail(self, mail):
        result = self.getUserMail(mail)
        print(result)
        if result:
            print('Mail already exists')
            return False
        else:
            print('Mail does not exist')
            return True



#===============================================================================
        # methodes from the controller
#===============================================================================
    