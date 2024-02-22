import customtkinter as ctk

from LoginScreen import LoginScreen
from MainPage import MainPage
from Register import Register

class View(ctk.CTk):
    def __init__(self, controller):
        super().__init__()

        self.controller = controller

        self.geometry("1200x800")
        self.config(bg="light green")
        self.title("Harmony1.0")
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.minsize(width=1200, height=800)
        self.maxsize(width=1200, height=800)
        self.resizable(False, False)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.displayLoginScreen()
    
    def main(self):
        self.mainloop()

    
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

    def on_closing(self):
        self.destroy()
#===============================================================================
        # variables from Controller
#===============================================================================

    def get_login_variables(self, username, password):
        self.controller.get_login_variables(username, password)

    def get_register_variables(self, name, firstname, mail, mdp):
        self.controller.get_register_variables(name, firstname, mail, mdp)

    def get_sending_message(self, message):
        self.controller.get_sending_message(message)

        
