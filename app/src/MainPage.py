import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *
from tkinter import ttk

from .ServerButton import ServerButton


class MainPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.running = True
        self.creat_widgets()
        self.commande = "" 
        self.recording = False
        self.recordings = []
        for elem in self.master.get_audio_message():
            if elem not in self.recordings:
                self.recordings.append(elem)
        self.messages = []
        
    def creat_widgets(self):

        server_frame = CTkFrame(master=self, fg_color="#01b366", border_color="#FFFFFF", border_width=2, width=80)
        server_frame.pack(expand=False, side=ctk.LEFT, fill=ctk.Y)
        
        
        print("test id",self.master.get_user_information()[0])
        list_servers = self.master.get_user_server_by_userID(self.master.get_user_information()[0])
        print("test list",list_servers)
        for server in list_servers:
            self.server_button = ServerButton(server_frame, server_name=server[4], server_icon=None, server_description=server[5], is_last=False)
            self.server_button.pack()


        

        