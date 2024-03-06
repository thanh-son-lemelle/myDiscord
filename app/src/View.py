import customtkinter as ctk
from tkinter import Frame

from .LoginScreen import LoginScreen
from .MainPage import MainPage
from .Register import Register
from .ServerPage import ServerPage

from .ErrorMessage import ErrorMessage

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller
        self.error = ErrorMessage()

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
        print("view Main")
        self.mainloop()
        print("End of the mainlopp")

    
    def displayLoginScreen(self):
        self.login_screen = LoginScreen(self)
        self.login_screen.pack(expand=True, fill='both')

    def displayMainPage(self):
        self.login_screen.pack_forget()
        self.main_page = MainPage(self)
        self.display_ServerPage()
        # Pack the main page on the left side of the container
        self.main_page.pack(side='left', expand=True, fill='both')

        # Pack the server page on the right side of the container
        self.server_page.pack(side='right', expand=True, fill='both')
        

    def displayRegisterPage(self):
        self.login_screen.pack_forget()
        self.register_page = Register(self)
        self.register_page.pack(expand=True, fill='both')

    def displayloginScreen_from_register(self):
        self.register_page.pack_forget()
        self.displayLoginScreen()
    
    def display_ServerPage(self):
        self.server_page = ServerPage(self, userID=self.controller.get_user_information()[0])
        print("display_ServerPage", self.controller.get_user_information()[0])
    
    def swap_server_page(self,userID, serverID, list_channels):
        self.stop_thread()
        self.server_page.pack_forget()
        self.server_page = ServerPage(self, userID, serverID, list_channels)
        self.server_page.pack(side='right', expand=True, fill='both')


    def stop_thread(self):
        self.server_page.running = False
        self.server_page.thread.join()
        print("Thread closed")

    def on_closing(self):
        print("Closing")
        if self.controller.get_auth() == True:
            self.stop_thread()
        self.destroy()
        print("Window closed")
#===============================================================================
        # variables from Controller
#===============================================================================
    #messages process
    def get_sending_message(self, message, channelID):
        self.controller.get_sending_message(message, channelID)

    def read_message(self):
        return self.controller.read_message()
    

    def read_message_from_channel(self, channelID):
        return self.controller.read_message_from_channel(channelID)
    
    def get_channel_by_serverID(self, serverID):
        return self.controller.get_channel_by_serverID(serverID)

    #login process    
    def login(self):
        self.controller.login()
    
    def get_remember_me_state(self):
        return self.controller.get_remember_me_state()
    
    def get_user_information(self):
        return self.controller.get_user_information()
    
    #logout process
    def logout(self):
        return self.controller.logout()

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
    
    #buttons user process

    def create_channel(self, channel_name, channel_type):
        self.controller.create_channel(channel_name, channel_type)

    def create_membership(self, userID, serverID, role, channelID):
        self.controller.create_membership(userID, serverID, role, channelID)
    
    def get_channelID_by_channel_name(self, channel_name):
        return self.controller.get_channelID_by_channel_name(channel_name)
    
    def get_serverID_by_server_name_and_owner(self, server_name, owner):
        return self.controller.get_serverID_by_server_name_and_owner(server_name, owner)