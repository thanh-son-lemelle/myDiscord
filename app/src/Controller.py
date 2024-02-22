from Model import Model
from View import View

class Controller:
    '''
    classdocs
    '''

    '''
    class variables
    '''
    
    def __init__(self) -> None:
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.view.main()

    # during the login, the controller will call the model to check if the user is allowed to access the main page

    def get_login_variables(self, username, password):
        result = self.model.allowingAccess(username, password)
        if result:
            self.store_user_information(result)
            self.view.displayMainPage()
        else:
            print('Wrong username or password')

        #testing
        print(self.userID, self.username, self.firstname, self.mail)
        '''    
        print(result)
        print(f'Button is sending: {username}, {password}')
        return username, password
        '''
    # store the user information in the controller
        
    def store_user_information(self, value):
        self.userID = value[0][0]
        self.username = value[0][1]
        self.firstname = value[0][2]
        self.mail = value[0][4]

    # during the registration, the controller will call the model to create a new user
        
    def get_register_variables(self, name, firstname, mail, mdp):
        result = self.model.check_user_mail(mail)
        if result:
            self.model.creatingUser(name, firstname, mail, mdp)
        else:
            print('Mail already exists')
            #pop un message d'erreur
        
        #testing
        '''
        print(f'Button is sending: {name}, {firstname}, {mail}, {mdp}')
        return name, firstname, mail, mdp
        '''
    
    def get_sending_message(self, message):
        self.model.creatingMessage(message, self.userID, 2)

        #testing
        '''
        print(f'Button is sending: {message}')
        return message
        '''

    def read_message(self):
        return self.model.read_message_user()

        
if __name__ == "__main__":

    application = Controller()
    application.main()
