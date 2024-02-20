import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkCanvas


class Register(ctk.CTkFrame):
    """
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

        self.validation_button = CTkButton(self.frame, text="Valider", bg_color="green", fg_color="black", font=("Arial", 12), command=self.afficher_info and self.root.quit)
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
    """
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()
    
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

        label3 = CTkLabel(master=frame, text="Mail:", font=("Arial", 12))
        label3.pack(pady=12, padx=10)
        self.entry3 = CTkEntry(master=frame)
        self.entry3.pack(pady=12, padx=10)

        label4 = CTkLabel(master=frame, text="Mot de Passe:", font=("Arial", 12))
        label4.pack(pady=12, padx=10)
        self.entry4 = CTkEntry(master=frame)
        self.entry4.pack(pady=12, padx=10)

        validation_button = CTkButton(master=frame, text="Valider", command=self.get_input)
        validation_button.pack(pady=12, padx=10)
        
    def get_input(self):
        name = self.entry1.get()
        firstname = self.entry2.get()
        mail = self.entry3.get()
        mdp = self.entry4.get()
        return name, firstname, mail, mdp

if __name__ =="__main__":
    test = Register()
    test.launch()

