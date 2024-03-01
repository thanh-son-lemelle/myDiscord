import customtkinter as ctk

from .LoginScreen import LoginScreen
from .MainPage import MainPage
from .Register import Register
"""from .ErrorMessage import ErrorMessage"""

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.geometry("1200x700")
        self.config(bg="light green")
        self.title("Harmony1.0")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.minsize(width=1200, height=700)
        self.maxsize(width=1200, height=700)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        """self.error = ErrorMessage()"""
        self.displayLoginScreen()
    
    def main(self):
        print("Main")
        self.mainloop()
        print("End of the mainlopp")

    
    def displayLoginScreen(self):
        self.login_screen = LoginScreen(self)
        self.login_screen.pack(expand=True, fill='both')

    def displayMainPage(self):
        self.login_screen.pack_forget()
        self.main_page = MainPage(self)
        self.main_page.pack(expand=True, fill='both')

    def displayRegisterPage(self):
        self.login_screen.pack_forget()
        self.register_page = Register(self)
        self.register_page.pack(expand=True, fill='both')

    def displayloginScreen_from_register(self):
        self.register_page.pack_forget()
        self.displayLoginScreen()

    def on_closing(self):
        print("Closing")
        if self.controller.get_auth() == True:
            self.main_page.running = False
            self.main_page.thread.join()
            print("Thread closed")
        self.destroy()
        print("Window closed")
#===============================================================================
        # variables from Controller
#===============================================================================
    #messages process
    def get_sending_message(self, message):
        self.controller.get_sending_message(message)

    def read_message(self):
        return self.controller.read_message()

    #login process    
    def login(self):
        self.controller.login()
    
    def get_remember_me_state(self):
        return self.controller.get_remember_me_state()
    
    def get_user_information(self):
        return self.controller.get_user_information()

    #register process
    def register_new_user(self):
        self.controller.register_new_user()

    #buttons server process
    def get_user_server_by_userID(self, userID, server_name=None):
        if server_name is None:
            return self.controller.get_user_server_by_userID(userID)
        else:
            return self.controller.get_user_server_by_userID(userID, server_name)
    
    def get_username(self):
        return self.controller.getUserName()
    
    def get_save_audio(self,filename):
        self.controller.get_audio(filename)

    def get_audio_message(self):
        return self.controller.read_message_type2()