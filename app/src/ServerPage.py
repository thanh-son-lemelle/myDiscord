import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *
import tkinter as tk
import sounddevice as sd
import soundfile as sf
import threading
import os
import json
from datetime import datetime
from PIL import Image, ImageTk
from tkinter import ttk
import time

import winsound


class ServerPage(CTkFrame):
    def __init__(self, master, userID=None, serverID=None, list_channelID=[]):
        super().__init__(master)
        self.running = True
        self.userID=userID
        self.serverID = serverID
        self.list_channelID = list_channelID
        self.channel_selected = 2
        self.create_widgets()
        self.recording = False
        self.recordings = []
        for elem in self.master.get_audio_message():
            if elem not in self.recordings:
                self.recordings.append(elem)
        self.messages = []

    def create_widgets(self):

        frame = CTkFrame(master=self, fg_color="#2B2D31", border_width=0, width=700)
        frame.pack(expand=False, side=ctk.LEFT, fill=ctk.Y)
   
        frame3 = CTkScrollableFrame(master=self, fg_color="#1E1F22", border_color="#FFFFFF", border_width=0, orientation="vertical", scrollbar_button_color="#383838", width=80)
        frame3.pack(expand=False, side=ctk.RIGHT, fill=ctk.Y)

        frame2 = CTkScrollableFrame(master=self, fg_color="#383838", border_color="#FFFFFF", border_width=0, orientation="vertical", scrollbar_button_color="#383838")
        frame2.pack(expand=True, fill="both")

        self.entry = CTkEntry(self, text_color="#000000", fg_color="#FFFFFF", width=800)
        self.entry.pack(side=ctk.TOP, pady=10)  

        self.result_label = CTkLabel(master=frame2, text="",justify="left",font=("Arial", 16))
        self.result_label.pack(anchor="w", expand=True,pady=0, padx=0)

        title_online_user = CTkLabel(master=frame3, text="Users",justify="center",font=("Arial", 16))
        title_online_user.pack(anchor="n",pady=5, padx=0)

        self.list_user = self.master.get_username()
        def threading1():
             while self.running == True:

                self.test()
                self.list_user = self.master.get_username()
                time.sleep(1)

        self.thread = threading.Thread(target=threading1)
        self.thread.start()

        label = CTkLabel(master=frame, text="Canaux",font=("Arial", 16))
        label.pack(side="top", pady=(10, 0))
        
        if self.list_channelID is not None:
            for channel in self.list_channelID:
                channel_button = CTkButton(master=frame, text=channel, text_color="#000000", fg_color="#FFFFFF", hover_color="#FFAB00", command=lambda channel=channel: self.channel_select(channel))
                channel_button.pack(padx=30, pady=20)

        for user in self.list_user:
            if user[1]!=self.userID:
                self.user_button = CTkButton(master=frame3, text=user[0], fg_color="transparent", hover_color="#FFAB00", bg_color="transparent", command=lambda user=user[0]: self.on_button_user_click(user))
                self.user_button.pack(padx=0, pady=0)

        quit_button = CTkButton(master=frame, text="Disconnect",command= self.disconnect ,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFAB00")
        quit_button.pack(padx=30, pady=20,anchor = "s", side=BOTTOM)

        button = CTkButton(self, text="Send", command=self.on_clik_buttonSend, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        button.pack(side=ctk.TOP,ipadx=10)
        
        emoji_button = CTkButton(self, text="Choose an Emoji", command=self.pick_emoji, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        emoji_button.pack(side=ctk.TOP,ipadx=10)

        self.record_button = CTkButton(self, text="Click to record", command=self.toggle_recording, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        self.record_button.pack(side=ctk.TOP,ipadx=10)

        self.emoji_picker = None

        self.emojis = ["😊", "😂", "😍", "😎", "🤔", "😴", "🥳", "🎉", "👍", "❤️"]

        emoji_frame = CTkFrame(master=self, fg_color="#01b366", border_color="#FFFFFF", border_width=2)
        emoji_frame.pack(side=tk.BOTTOM, pady=10)

        for emoji in self.emojis:
            emoji_button = CTkButton(master=emoji_frame, text=emoji, command=lambda e=emoji: self.select_emoji(e), text_color="#000000", fg_color="#FFFFFF", hover_color="#FFAB00")
            emoji_button.configure(width=10, height=10)
            emoji_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.listbox = tk.Listbox(self,width=50)
        self.listbox.bind("<Double-Button-1>",self.play_selected)
        self.listbox.pack()

    # def add_message(self, message):
    #     message_label = tk.Label(self.frame2, text=message)
    #     message_label.pack(anchor="w")
    #     self.frame2.update_idletasks()  # Assurez-vous que les tâches sont à jour
    #     self.frame2.canvas.yview_scroll(1, "units")  # Déplacer la vue vers le bas d'une unité


    def on_button_click(self):
        user_input = self.entry.get()
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
        self.master.get_sending_message(message,self.channel_selected)
        self.entry.delete(0, 'end')


    def test(self):
        texte = ""
        for tup in self.master.read_message_from_channel(self.channel_selected):
            # Convert the elements of the tuple to strings
            str_tup = [str(item) if not isinstance(item, bytes) else item.decode('utf-8') for item in tup]
            str_tup[0] += " : "
            texte += " \n".join(str_tup) + "\n\n"
        self.result_label.configure(text=texte)


    # methods for emojis
    def send_message(self):
        message = self.entry.get()
        if message:
            self.messages_list.insert(tk.END, f"You: {message}")
            self.entry.delete(0, tk.END)


    def pick_emoji(self):
        if not self.emoji_picker:
            self.emoji_picker = tk.Toplevel(self)
            
            for emoji in self.emojis:
                emoji_button = CTkButton(master=self.emoji_picker, text=emoji, command=lambda e=emoji: self.select_emoji(e), text_color="#000000", fg_color="#FFFFFF", hover_color="#FFAB00")
                # emoji_button.configure(width=30, height=30)
                # emoji_button.pack(padx=30, pady=30)

            self.emoji_picker.protocol("WM_DELETE_WINDOW", self.close_emoji_picker)


    def select_emoji(self, emoji):
        self.entry.insert(tk.END, emoji)
        self.close_emoji_picker()


    def close_emoji_picker(self):
        if self.emoji_picker:
            self.emoji_picker.destroy()
            self.emoji_picker = None


 # methods for recording audio
    def start_recording(self):
        self.recording = True
        self.record_button.configure(text="Stop recording")
        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()


    def stop_recording(self):
        self.recording = False
        self.record_button.configure(text="Recording")


    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()


    def record_audio(self):
        duration = 10  
        fs = 44100  
        try:
            filename = f"enregistrement_{datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
            with sf.SoundFile(filename, mode='x', samplerate=fs, channels=2) as file:
                with sd.InputStream(callback=lambda data, frames, time, status: file.write(data)):
                    sd.sleep(int(duration * 1000))
            self.save_audio(filename)
        except Exception as e:
            print("Une erreur est survenue lors de l'enregistrement :", e)
        finally:
            self.stop_recording()
            

    def save_audio(self, filename):
        if not os.path.exists("audio_recordings"):
            os.makedirs("audio_recordings")
        os.rename(filename, os.path.join("audio_recordings", filename))
        if filename not in self.recordings:
            self.recordings.append(filename)
            self.master.get_save_audio(filename)
            self.update_listbox()


    def update_listbox(self):
        for recording in self.master.get_audio_message():
            
            self.listbox.insert(tk.END, recording)


    def play_selected(self,event):
        selected_index = self.listbox.curselection()[0]
        filename = self.recordings[selected_index]
        filename_str = str(filename[0]) if not isinstance(filename[0], bytes) else filename[0].decode("utf-8")
        winsound.PlaySound(f"audio_recordings/{filename_str}", winsound.SND_FILENAME)
    
    def get_userID(self, user):
        for item in self.list_user:
            if item[0] == user:
                userID = item[1]
                user_name = item[0]
                return userID, user_name
    
    def create_channel(self, channel_name, channel_type):
        self.master.create_channel(channel_name, channel_type)

    def create_membership(self, userID, serverID, role, channelID):
        self.master.create_membership(userID, serverID, role, channelID)

    def get_serverID_by_server_name_and_owner(self, server_name, owner):
        return self.master.get_serverID_by_server_name_and_owner(server_name, owner)

    def on_button_user_click(self, user):
        userID, user_Name = self.get_userID(user)
        channel_name = f"{self.userID}+{userID}"
        result = self.master.get_channelID_by_channel_name(channel_name)
        if result == []:
            
            self.create_channel(str(channel_name), "private channel")
            channelID = self.master.get_channelID_by_channel_name(channel_name)[0][0]
            self.create_membership(self.userID, self.serverID, "member", channelID)
            #get serverid from the user
            serverID = self.get_serverID_by_server_name_and_owner("Private Messages",userID)[0][0]
            self.create_membership(userID, serverID, "member", channelID)
    
    def channel_select(self, channel):
        self.channel_selected = channel[0]


    def disconnect(self):
        self.master.stop_thread()
        self.master.logout()
        