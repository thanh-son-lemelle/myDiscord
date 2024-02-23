import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *

class MainPage(CTkFrame):
    def __init__(self, master):
        
        super().__init__(master)
        self.running = True
        self.creat_widgets()

    def creat_widgets(self):
        
        frame = CTkFrame(master=self, fg_color="#01b366", border_color="#FFFFFF", border_width=2, width=700)
        frame.pack(expand=False, side=ctk.LEFT, fill=ctk.Y)

        frame2 = CTkScrollableFrame(master=self, fg_color="#383838", border_color="#FFFFFF", border_width=2,orientation="vertical", scrollbar_button_color="#383838")
        frame2.pack(expand=True, fill="both")

        

        self.entry = CTkEntry(self, text_color="#000000", fg_color="#FFFFFF", width=800)
        self.entry.pack(side=ctk.TOP, pady=10)  

        self.result_label = CTkLabel(master=frame2, text="",justify="left",font=("Arial", 16))
        self.result_label.pack(anchor="w", expand=True,pady=10, padx=30)

        self.test()

        label = CTkLabel(master=frame, text="Canaux", text_color="#000000")
        label.pack(side="top", pady=(10, 0))

        button_textuel = CTkButton(master=frame, text="Salon textuel", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        button_textuel.pack(padx=30, pady=20)

        button_vocal = CTkButton(master=frame, text="Salon vocal", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        button_vocal.pack(padx=30, pady=20)


        quit_button = CTkButton(master=frame, text="Disconnect",command= self.disconnect ,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        quit_button.pack(padx=30, pady=20,anchor = "s")

        button = CTkButton(self, text="Envoyer", command=self.on_clik_buttonSend, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        button.pack(side=ctk.TOP,ipadx=40)
        




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


    def set_runnig(self):
        self.running = False


    def get_mainPage_status(self):
        return self.running
    
    #new methods from this point
    def on_clik_buttonSend(self):
        message = self.entry.get()
        self.master.get_sending_message(message)
        self.entry.delete(0, 'end')


    def test(self):
        texte = ""
        for tup in  self.master.read_message():
            texte += str(tup) + "\n" + "\n"

        self.result_label.configure(text=texte)



    def disconnect(self):
        self.master.main_page.pack_forget()
        self.master.displayLoginScreen()


    