from .Channel import Channel
from .ServerMember import ServerMember
from .Message import Message
from .Reaction import Reaction
from .Server import Server
from .User import User
from .Join import Join

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
    def createMessage(self, content, userID, channelID, type):
        self.message.create(content, userID, channelID, type)
    
    def readMessage(self):
        return self.message.read()
    
    def updateMessage(self, messageID, content, userID, channelID, type):
        self.message.update(messageID, content, userID, channelID, type)

    def deleteMessage(self, messageID):
        self.message.delete(messageID)


    def read_message_type2_from_message(self):
        return self.message.read_audio()
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
    def createServer(self, server_name, description, type, owner, server_image):
        self.server.create(server_name, description, type, owner, server_image)
    
    def readServer(self):
        return self.server.read()
    
    def updateServer(self, serverID, server_name, description, type, owner, server_image):
        self.server.update(serverID, server_name, description, type, owner, server_image)

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
        return self.user.get_userName()
    
    def returnAllMail(self):
        return self.user.userAllmail()
    
    def returnAllPassword(self):
        return self.user.allpassword()
    

#===============================================================================
        # join
#===============================================================================


    def read_message_user(self):
        return self.join.get_message_and_user()
    
    def read_message_user_from_channel(self,channelID):
        return self.join.get_messages_for_user_in_channel(channelID)
    
    def get_channel_by_serverID(self, serverID):
        return self.join.get_channel_by_serverID(serverID)
    
#===============================================================================

#===============================================================================
        # methodes for the frontend
#===============================================================================
    
    #===========================================================================
    # methodes for the authentication service
    #===========================================================================
    
    def get_user_by_username(self, username):
        user_data = self.user.get_user_by_username(username)
        print ("test user data",user_data)
        if user_data:
            return user_data[1], user_data[3]
        else:
            return False
        
    def get_user_information_by_username(self, username):
        user_data = self.user.get_user_by_username(username)
        if user_data:
            return user_data
        else:
            return False
    
    def get_user_by_mail(self, mail):
        user_data = self.user.get_user_by_mail(mail)
        if user_data:
            return user_data['mail'], user_data['password']
        else:
            return False
        
    def save_auth_token(self,usermail, token):
        self.user.save_auth_token(usermail, token)

    def check_auth_token(self, token):
        return self.user.check_auth_token(token)

    #===========================================================================
    # methodes for the registration
    
    def edit_user(self, name, firstname, email, password):
        self.user.create(name, firstname, email, password)

    def creatingMessage(self, content, userID, type, channelID):
        self.message.create(content, userID, type, channelID)

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

    def check_input_register(self, name, firstname, mail, mdp):
        print("test dans check_input_register")
        print("name, firstname, mdp, mail", name, firstname, mail, mdp)
        if not all([name, firstname, mdp, mail]):
            print("Veuillez remplir tous les champs.")
            
            return False , "Veuillez remplir tous les champs."
        elif "@" not in mail:
            print("Veuillez entrer une adresse e-mail valide avec @.")
            return False , "Veuillez entrer une adresse e-mail valide avec @."
        result = self.check_user_mail(mail)
        if result == True:
            print("Mail valide test dans check_input_register")
            
            return True , ""
        
        else: 
            print("Mail existe déjà")
            # self.master.get_register_variables(name, firstname, mail, mdp)
            # self.master.register_page.pack_forget()

            return False, "Mail existe déjà"
        
    # when the user is created he need to have a private server
        
    def create_private_server(self, name, description, type, owner):
        with open("image\\icon_server_default.png", "rb") as image_file:
            server_image = image_file.read()

        self.server.create(name, description, type, owner, server_image)
    
    def create_membership(self, userID, serverID, role):
        self.server_member.create(userID, serverID, role)
        
    def create_user(self, name, firstname, mail, mdp):
        result = self.check_input_register(name, firstname, mdp, mail)
        if result[0] == True:
            self.edit_user(name, firstname, mail, mdp)
            userID=self.get_user_information_by_username(name)[0]
            self.create_private_server("Private Messages", "default server", 1, userID)
            print(self.join.get_user_server_by_userID(userID, "Private Messages"))
            serverID = self.join.get_user_server_by_userID(userID, "Private Messages")[0][3]
            self.create_membership(userID, serverID, "admin")
        print("User created")
        return True
        
#===============================================================================
        # methodes for the server_button
#===============================================================================
    def get_user_server(self, userID):
        return self.join.get_user_server(userID) #no def
    
    def get_user_server_by_userID(self, userID, server_name =None):
        if server_name:
            return self.join.get_user_server_by_userID(userID, server_name)
        else:
            return self.join.get_user_server_by_userID(userID)
#===============================================================================
        # methodes for the user buttons
#===============================================================================
        
    def create_channel(self, channel_name, channel_type):
        self.channel.create(channel_name, channel_type)

    def create_membership(self, userID, serverID, role, channelID):
        self.server_member.create(userID, serverID, role, channelID)

    def get_channelID_by_channel_name(self, channel_name):
        return self.channel.get_channelID_by_channel_name(channel_name)

    def get_serverID_by_server_name_and_owner(self, server_name, owner):
        return self.server.get_serverID_by_server_name_and_owner(server_name, owner)