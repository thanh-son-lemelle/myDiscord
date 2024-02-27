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

        

    def main(self):
        self.view.main()

    # during the login, the controller will call the model to check if the user is allowed to access the main page

    def get_login_variables(self):
        username=self.view.login_screen.value_name.get()
        password=self.view.login_screen.value_password.get()
        return username, password


    #testing
    def automatic_login(self):
        result = self.service.automatic_login(self.get_remember_me_state())
        if result == True:
            """self.store_user_information(self.model.get_user_information_by_username(username))"""
            self.view.displayMainPage()

    def login(self):

        username, password = self.get_login_variables()
        print(self.view.login_screen.value_remember_me.get())
        result = self.service.login(username, password, self.view.login_screen.value_remember_me.get())
        if result == True:
            self.store_user_information(self.model.get_user_information_by_username(username))
            self.view.displayMainPage()
        else:
            self.view.error.set_error("Wrong username or password")
            self.view.error.creat_widgets(self.view.screen_width//2 ,self.view.screen_height//2)

        #testing
        #print(self.userID, self.username, self.firstname, self.mail)
        '''    
        print(result)
        print(f'Button is sending: {username}, {password}')
        return username, password
        '''
    # store the user information in the controller
    
      
    def store_user_information(self, value):
        self.userID = value[0]
        self.username = value[1]
        self.firstname = value[2]
        self.mail = value[4]
    # during the registration, the controller will call the model to create a new user
    
    def get_sending_message(self, message):
        self.model.creatingMessage(message, self.userID, 2)

        #testing
        '''
        print(f'Button is sending: {message}')
        return message
        '''

    def read_message(self):
        return self.model.read_message_user()
    
    #===============================================================================
    #         # methodes getters from the frontend to be used in the model
    #===============================================================================

    def getUserMail(self):
        return self.view.login_screen.value_name.get()
    
    def getUserPassword(self):
        return self.view.login_screen.value_password.get()
    
    def getRememberMe(self):
        return self.view.login_screen.value_remember_me.get()
    

    #===============================================================================
    def get_remember_me_state(self):
        return self.service.load_checkbox_state()

        
if __name__ == "__main__":

    application = Controller()
    application.main()
