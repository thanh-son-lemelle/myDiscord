from .Model import Model
from .View import View
from .Service import Service

class Controller:
    '''
    classdocs
    '''

    '''
    class variables
    '''
    
    def __init__(self) -> None:
        self.model = Model()
        self.service = Service()
        self.view = View(self)
        self.automatic_login()

        
    #defining the main boucle of the application
    def main(self):
        self.view.main()
    
    #===============================================================================
    #         # login and logout process
    #===============================================================================

    # during the login, the controller will call the model to check if the user is allowed to access the main page

    def get_login_variables(self):
        username=self.view.login_screen.value_name.get()
        password=self.view.login_screen.value_password.get()
        return username, password


    #testing
    def automatic_login(self):
        result = self.service.automatic_login(self.get_remember_me_state())
        if result is not None:
            result, username = result
            if result == True:
                self.store_user_information(self.model.get_user_information_by_username(username))
                self.view.displayMainPage()
        else:
            pass

    def login(self):

        username, password = self.get_login_variables()
        result = self.service.login(username, password, self.view.login_screen.value_remember_me.get())
        if result == True:
            self.store_user_information(self.model.get_user_information_by_username(username))
            self.view.displayMainPage()
        else:
            self.view.error.set_error("Wrong username or password")
            self.view.error.creat_widgets(self.view.screen_width//2 ,self.view.screen_height//2)
    # store the user information in the controller

    def store_user_information(self, value):
        self.userID = value[0]
        self.username = value[1]
        self.firstname = value[2]
        self.mail = value[4]

    #logout
    def logout(self):
        self.service.auth = False
        self.service.reset_local_data()
        self.view.main_page.pack_forget()
        self.view.server_page.pack_forget()
        self.view.displayLoginScreen()

    # during the registration, the controller will call the model to create a new user
    def get_user_information(self):
        return self.userID, self.username, self.firstname, self.mail
    
    def get_sending_message(self, message, channelID):
        self.model.creatingMessage(message, self.userID, 1, channelID)

    def read_message(self):
        return self.model.read_message_user()
    
    def read_message_from_channel(self, channelID):
        return self.model.read_message_user_from_channel(channelID)
    
    def read_message_type2(self):
        return self.model.read_message_type2_from_message()
    
    def get_channel_by_serverID(self, serverID):
        return self.model.get_channel_by_serverID(serverID)
    
    #===============================================================================
    #         # methodes getters from the frontend to be used in the model
    #===============================================================================

    def getUserMail(self):
        return self.view.login_screen.value_name.get()
    
    def getUserPassword(self):
        return self.view.login_screen.value_password.get()
    
    def getRememberMe(self):
        return self.view.login_screen.value_remember_me.get()
    
    def getUserName(self):
        return self.model.returnAllName()
    

    #===============================================================================
    #         # methodes from service
    def get_remember_me_state(self):
        return self.service.load_checkbox_state()
    
    def get_auth(self):
        return self.service.auth
    
    def get_audio(self,filename):
        self.model.creatingMessage(filename, self.userID, 2, 2)
    
    
    #===============================================================================
    #         # methodes for the registration

    def get_register_variables(self):
        name=self.view.register_page.value_name.get()
        firstname=self.view.register_page.value_firstname.get()
        mail=self.view.register_page.value_mail.get()
        mdp=self.view.register_page.value_password.get()
        return name, firstname, mail, mdp
    
    def register_new_user(self):
        name, firstname, mail, mdp = self.get_register_variables()
        self.model.create_user(name, firstname, mdp, mail)
        self.view.displayloginScreen_from_register()

#===============================================================================
#         # methodes for buttons server
    def set_userID_for_button(self):
        return self.userID
    
    def get_user_server(self, userID, server_name=None): #no def
        return self.model.get_user_server(userID, server_name= None)
    
    def get_user_server_by_userID(self, userID, server_name= None):
        if server_name is None:
            return self.model.get_user_server_by_userID(userID)
        else:
            return self.model.get_user_server_by_userID(userID, server_name)     

#===============================================================================
        # methodes for the user buttons 

    def create_channel(self, name, channel_type):
        self.model.create_channel(name, channel_type)

    def create_membership(self, userID, serverID, role, channelID):
        self.model.create_membership(userID, serverID, role, channelID)

    def get_channelID_by_channel_name(self, channel_name):
        return self.model.get_channelID_by_channel_name(channel_name)
    
    def get_serverID_by_server_name_and_owner(self, server_name, owner):
        return self.model.get_serverID_by_server_name_and_owner(server_name, owner)
        
if __name__ == "__main__":

    application = Controller()
    application.main()
