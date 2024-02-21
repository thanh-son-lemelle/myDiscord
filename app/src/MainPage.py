import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *

class MainPage(CTkFrame):
    def __init__(self, master):
        
        """super().__init__(master)
        
        self.application2 = ctk.CTk()
        
        self.application2.minsize(width=800, height=400)
    
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.frame = CTkFrame(master=self.application2, fg_color="#01b366", border_color="#FFFFFF", border_width=2,width=700)
        self.frame.pack(expand=False,side = LEFT, fill = Y)

        self.frame2= CTkFrame(master=self.application2, fg_color="#383838", border_color="#FFFFFF", border_width=2,width=700)
        self.frame2.pack(expand=True,fill = 'both')  # Utilisation de pack pour étirer la frame dans toutes les directions

        self.entry = CTkEntry(self.frame2 ,text_color="#000000" ,fg_color="#FFFFFF",width=1200)
        self.entry.pack(side = BOTTOM,pady = 10)  # Utilisation de pack pour positionner l'entrée en bas

        self.result_label = CTkLabel(self.frame2, text="")
        self.result_label.pack(side = TOP , pady=10)


    def on_button_click(self):
        user_input = self.entry.get()
        self.result_label.configure(text=user_input)

    def display(self):
        print ("test")
        self.application2.after(0, lambda: self.application2.state('zoomed'))

        label = CTkLabel(master=self.frame, text="Canaux", text_color="#000000")
        label.pack(side="top", pady=(10, 0))  # Utilisation de pack pour positionner le label en haut

        button_textuel = CTkButton(master=self.frame, text="Salon textuel", text_color="#000000", fg_color="#FFFFFF",hover_color="#FFDE00").pack(padx=30, pady=20)

        button_vocal = CTkButton(master=self.frame, text="Salon vocal", text_color="#000000", fg_color="#FFFFFF",hover_color="#FFDE00").pack(padx=30, pady=20)


        button = CTkButton(self.frame2, text="Envoyer", command=self.on_button_click, text_color="#000000", fg_color="#FFFFFF",hover_color="#01b366")
        button.pack(side=BOTTOM, ipadx=40)  # Utilisation de pack pour positionner le bouton en bas

       
        self.application2.mainloop()


    def get_message(self,message):
        commande = message
        return commande"""

        super().__init__(master)
        self.creat_widgets()

    def creat_widgets(self):
        
        frame = CTkFrame(master=self, fg_color="#01b366", border_color="#FFFFFF", border_width=2, width=700)
        frame.pack(expand=False, side=ctk.LEFT, fill=ctk.Y)

        frame2 = CTkFrame(master=self, fg_color="#383838", border_color="#FFFFFF", border_width=2, width=700)
        frame2.pack(expand=True, fill='both')  

        self.entry = CTkEntry(frame2, text_color="#000000", fg_color="#FFFFFF", width=1200)
        self.entry.pack(side=ctk.BOTTOM, pady=10)  

        self.result_label = CTkLabel(frame2, text="")
        self.result_label.pack(side=ctk.TOP, pady=10)

        label = CTkLabel(master=frame, text="Canaux", text_color="#000000")
        label.pack(side="top", pady=(10, 0))

        button_textuel = CTkButton(master=frame, text="Salon textuel", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        button_textuel.pack(padx=30, pady=20)

        button_vocal = CTkButton(master=frame, text="Salon vocal", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        button_vocal.pack(padx=30, pady=20)

        button = CTkButton(frame2, text="Envoyer", command=self.show_content, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        button.pack(side=ctk.BOTTOM, ipadx=40)
        




    def on_button_click(self):
        user_input = self.entry.get()
        print(user_input)
        return user_input
       


    def get_message(self, message):
        self.commande = ""
        self.commande = message
        return self.commande 
    


    def show_message(self):
        self.result_label.configure(text = self.commande)



    def show_content(self):
        self.show_message()
        self.on_button_click()


    