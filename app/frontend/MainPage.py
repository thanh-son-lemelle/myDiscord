import customtkinter as ctk
from customtkinter import *

class Mainpage():
    def __init__(self):
        
        self.app2 = ctk.CTk()
        
        self.app2.minsize(width=800, height=400)
    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.frame = CTkFrame(master=self.app2, fg_color="#01b366", border_color="#FFFFFF", border_width=2,width=700)
        self.frame.pack(expand=False,side = LEFT, fill = Y)

        self.frame2= CTkFrame(master=self.app2, fg_color="#383838", border_color="#FFFFFF", border_width=2,width=700)
        self.frame2.pack(expand=True,fill = 'both')  # Utilisation de pack pour étirer la frame dans toutes les directions

        self.entry = CTkEntry(self.frame2 ,text_color="#000000" ,fg_color="#FFFFFF",width=1200)
        self.entry.pack(side = BOTTOM,pady = 10)  # Utilisation de pack pour positionner l'entrée en bas

        self.resultat_label = CTkLabel(self.frame2, text="")
        self.resultat_label.pack(side = TOP , pady=10)


    def on_button_click(self):
        user_input = self.entry.get()
        self.resultat_label.configure(text=user_input)

    def display(self):
        print ("test")
        self.app2.after(0, lambda: self.app2.state('zoomed'))

        label = CTkLabel(master=self.frame, text="Canaux", text_color="#000000")
        label.pack(side="top", pady=(10, 0))  # Utilisation de pack pour positionner le label en haut

        button_textuel = CTkButton(master=self.frame, text="Salon textuel", text_color="#000000", fg_color="#FFFFFF",hover_color="#FFDE00").pack(padx=30, pady=20)

        button_vocal = CTkButton(master=self.frame, text="Salon vocal", text_color="#000000", fg_color="#FFFFFF",hover_color="#FFDE00").pack(padx=30, pady=20)


        button = CTkButton(self.frame2, text="Envoyer", command=self.on_button_click, text_color="#000000", fg_color="#FFFFFF",hover_color="#01b366")
        button.pack(side=BOTTOM, ipadx=40)  # Utilisation de pack pour positionner le bouton en bas

        print("test2")
       
        self.app2.mainloop()
        
