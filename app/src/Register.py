import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkCanvas


class Register(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
        self.click_validation = False

    def create_widgets(self):
        frame = CTkFrame(master=self, width=1482, height=834, corner_radius=45)
        frame.pack(pady=40, padx=300, fill='both', expand=False, side="top", anchor="center")
        
        label = CTkLabel(master=frame, text='Inscription à Harmony', font=('helvetica', 30))
        label.pack(pady=12, padx=10)

        label1 = CTkLabel(master=frame, text="Nom:", font=("Arial", 12))
        label1.pack(pady=12, padx=10)
        self.entry1 = CTkEntry(master=frame)
        self.entry1.pack(pady=12, padx=10)

        label2 = CTkLabel(master=frame, text="Prénom:", font=("Arial", 12))
        label2.pack(pady=12, padx=10)
        self.entry2 = CTkEntry(master=frame)
        self.entry2.pack(pady=12, padx=10)

        label3 = CTkLabel(master=frame, text="Mot de Passe:", font=("Arial", 12))
        label3.pack(pady=12, padx=10)
        self.entry3 = CTkEntry(master=frame)
        self.entry3.pack(pady=12, padx=10)

        label4 = CTkLabel(master=frame, text="Mail:", font=("Arial", 12))
        label4.pack(pady=12, padx=10)
        self.entry4 = CTkEntry(master=frame)
        self.entry4.pack(pady=12, padx=10)

        validation_button = CTkButton(master=frame, text="Valider", command=self.on_click_validation)
        validation_button.pack(pady=12, padx=10)
        
    # to this point new methods

    def on_click_validation(self):
        name = self.entry1.get()
        firstname = self.entry2.get()
        mdp = self.entry3.get()
        mail = self.entry4.get()
        return self.master.get_register_variables(name, firstname, mdp, mail)   

    # Handle further actions here
