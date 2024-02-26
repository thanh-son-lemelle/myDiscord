import customtkinter as ctk
from customtkinter import *  
from customtkinter.assets import *

class ErrorMessage(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.window = ctk.CTk()
        self.window.title("ERROR")
        self.protocol("WM_DELETE_WINDOW", self.close_pop_up)
        # self.window.minsize(width=300, height=300)
        # self.window.maxsize(width=400, height=300)

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.text = ""

    def creat_widgets(self,pos_window_x,pos_window_y):
        
        self.window.geometry(f"200x100+{pos_window_x}+{pos_window_y}")

        text_label = CTkLabel(self.window, text=self.text,font=("Arial", 10),fg_color="#242424",text_color="#FFFFFF")

        # Pack the Label widget to make it visible in the window
        text_label.pack()  


        quit_button = CTkButton(master = self.window ,text="Ok",command=self.close_pop_up ,text_color="#000000", fg_color="#FFFFFF",bg_color="#242424")
        quit_button.pack(padx=30, pady=20,anchor = "s" , side = ctk.BOTTOM)


        self.window.mainloop() 



    def set_error(self,error_message):
        self.text = error_message



    def close_pop_up(self):
        self.window.destroy()