import customtkinter as tk
from customtkinter import *


class Register:
    def __init__(self):
        self.root = tk.CTk()
        self.root.title("Création de compte")
        self.root.geometry("1482x834")  
        self.root.config(bg="light green")  
        
        self.canvas_title = CTkCanvas(self.root, width=500, height=100, bg="white", highlightthickness=0)
        self.canvas_title.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        self.title_label = CTkLabel(self.canvas_title, text="Inscription à Harmony", font=("Lucid", 30), bg_color="white", fg_color="white")
        self.title_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.frame = CTkFrame(self.root, bg_color="white", width=500, height=300)
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.label = CTkLabel(self.frame, text="Veuillez remplir les informations", font=("Arial", 14), bg_color="white")
        self.label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)
        
        self.label1 = CTkLabel(self.frame, text="Nom:", font=("Arial", 12), bg_color="white")
        self.label1.place(relx=0.2, rely=0.3, anchor=tk.W)
        self.entry1 = CTkEntry(self.frame)
        self.entry1.place(relx=0.5, rely=0.3, anchor=tk.CENTER) 

        self.label2 = CTkLabel(self.frame, text="Prénom:", font=("Arial", 12), bg_color="white")
        self.label2.place(relx=0.2, rely=0.4, anchor=tk.W)
        self.entry2 = CTkEntry(self.frame)
        self.entry2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        self.label3 = CTkLabel(self.frame, text="Mail:", font=("Arial", 12), bg_color="white")
        self.label3.place(relx=0.2, rely=0.5, anchor=tk.W)
        self.entry3 = CTkEntry(self.frame)
        self.entry3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.label4 = CTkLabel(self.frame, text="Mot de Passe:", font=("Arial", 12), bg_color="white")
        self.label4.place(relx=0.2, rely=0.6, anchor=tk.W)
        self.entry4 = CTkEntry(self.frame)
        self.entry4.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

        self.validation_button = CTkButton(self.frame, text="Valider", bg_color="green", fg_color="black", font=("Arial", 12), command=self.afficher_info)
        self.validation_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

        

    def afficher_info(self):
        name = self.entry1.get()
        firstname = self.entry2.get()
        mail = self.entry3.get()
        mdp = self.entry4.get()
        
        print("Nom:", name)
        print("Prénom:", firstname)
        print("Email:", mail)
        print("Mot de Passe:", mdp)


    def launch(self):
        self.root.mainloop()



