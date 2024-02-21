import tkinter as tk
import customtkinter as ctk
from PIL import Image


class LoginScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.user_entry = ''
        self.user_pass = ''
        self.create_widgets()
        
    def create_widgets(self):
            frame = ctk.CTkFrame(master=self, width=1482, height=834, corner_radius=45)
            frame.pack(pady=40, padx=300, fill='both', expand=False, side="top", anchor="center")
            
            label = ctk.CTkLabel(master=frame, text='HARMONY', font=('helvetica', 64))
            label.pack(pady=12, padx=10)

            self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Pseudo/mail")
            self.user_entry.pack(pady=12, padx=10)

            self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="mot de passe", show="*")
            self.user_pass.pack(pady=12, padx=10)

            login_button = ctk.CTkButton(master=frame, text='Login', command=self.go_to_MainPage)
            login_button.pack(pady=12, padx=10)

            remember_checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
            remember_checkbox.pack(pady=12, padx=10)

            register_button = ctk.CTkButton(master=frame, text='Register', command=self.set_register_true)
            register_button.pack(pady=12, padx=10)

    def get_permission(self):
        print ("test")

    def go_to_MainPage(self):
        self.get_permission()
        self.master.displayMainPage()
        # Handle further actions here

    def set_register_true(self):
        self.master.displayRegisterPage()
        # Handle further actions here

    def get_input_values(self):
        name = self.user_entry.get()
        psswd = self.user_pass.get()
        return name, psswd

    def get_login_status(self):
        return self.login

    def get_register_status(self):
        return self.register