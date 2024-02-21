import customtkinter as ctk
from LoginScreen import LoginScreen
from MainPage import MainPage
from Register import Register

class Screen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x600")
        self.config(bg="light green")
        self.title("Harmony")
        self.minsize(width=0, height=0)
        self.maxsize(width=1482, height=834)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.main_page = MainPage(self)
        self.register_page = Register(self)
        self.login_screen = LoginScreen(self)
        self.displayLoginScreen()

    def displayLoginScreen(self):
        self.login_screen.pack(expand=True, fill='both')

    def displayMainPage(self):
        self.login_screen.pack_forget()
        self.main_page.pack(expand=True, fill='both')

    def displayRegisterPage(self):
        self.login_screen.pack_forget()
        self.register_page.pack(expand=True, fill='both')

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = Screen()
    app.mainloop()