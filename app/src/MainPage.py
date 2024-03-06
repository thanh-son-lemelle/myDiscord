import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *
from tkinter import ttk

from .ServerButton import ServerButton

import pygame


class MainPage(CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.running = True
        self.create_widgets()
        self.commande = "" 
        self.recording = False
        self.recordings = []
        for elem in self.master.get_audio_message():
            if elem not in self.recordings:
                self.recordings.append(elem)
        self.messages = []
        
    def create_widgets(self):
        server_frame = CTkFrame(master=self, fg_color="#1E1F22", border_width=0, width=80)
        server_frame.pack(expand=False, side=ctk.LEFT, fill=ctk.Y)
        
        print("test id", self.master.get_user_information()[0])
        list_servers = self.master.get_user_server_by_userID(self.master.get_user_information()[0])
        print("test list", list_servers)

        chat_textuel = CTkButton(master=server_frame, text="Main chat", fg_color="transparent", hover_color="#FFAB00", font=("Arial", 16), command=self.on_click_main_chat)
        chat_textuel.pack(padx=0, pady=20)
        
        for server in list_servers:
            server_button = ServerButton(server_frame, self, server_name=server[4], serverID=server[3], userID=self.master.get_user_information()[0])
            server_button.pack()

    def swap_server_page(self, server_name, serverID, list_channels):
        self.master.swap_server_page(server_name, serverID, list_channels)

    def get_channel_by_serverID(self, serverID):
        return self.master.get_channel_by_serverID(serverID)
    
    def on_click_main_chat(self):
        self.master.swap_server_page(self.master.get_user_information()[0], None, None)