import customtkinter as ctk
from LoginScreen import LoginScreen

class Screen(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1482x834")
        self.config(bg="light green")
        self.title("Harmony")
        self.minsize(width=1482, height=834)
        self.maxsize(width=1482, height=834)
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.displayLoginScreen()

    def displayLoginScreen(self):
        self.login_screen = LoginScreen(self)
        self.login_screen.pack(expand=True, fill='both')

    def on_closing(self):
        self.destroy()

if __name__ == "__main__":
    app = Screen()
    app.mainloop()