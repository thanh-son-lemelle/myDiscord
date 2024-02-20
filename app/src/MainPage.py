import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *

class MainPage(CTkFrame):
    def __init__(self, master):

        super().__init__(master)

        self.creat_widgets()

    def creat_widgets(self):

        frame = CTkFrame(master=self, fg_color="#01b366", border_color="#FFFFFF", border_width=2, width=700)
        frame.pack(expand=False, side=ctk.LEFT, fill=ctk.Y)

        frame2 = CTkFrame(master=self, fg_color="#383838", border_color="#FFFFFF", border_width=2, width=700)
        frame2.pack(expand=True, fill='both')  

        entry = CTkEntry(frame2, text_color="#000000", fg_color="#FFFFFF", width=1200)
        entry.pack(side=ctk.BOTTOM, pady=10)  

        result_label = CTkLabel(frame2, text="")
        result_label.pack(side=ctk.TOP, pady=10)

        label = CTkLabel(master=frame, text="Canaux", text_color="#000000")
        label.pack(side="top", pady=(10, 0))

        button_textuel = CTkButton(master=frame, text="Salon textuel", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        button_textuel.pack(padx=30, pady=20)

        button_vocal = CTkButton(master=frame, text="Salon vocal", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        button_vocal.pack(padx=30, pady=20)

        button = CTkButton(frame2, text="Envoyer", command=self.on_button_click, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        button.pack(side=ctk.BOTTOM, ipadx=40)

    def on_button_click(self):
        user_input = self.entry.get()
        self.result_label.configure(text=user_input)

    def get_message(self, message):
        commande = message
        return commande