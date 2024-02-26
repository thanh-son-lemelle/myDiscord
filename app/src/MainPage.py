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

class MainPage(CTkFrame):
    def __init__(self, master):
        
        super().__init__(master)
        self.running = True
        self.creat_widgets()
        self.master = master
        self.commande = "" 
        self.recording = False
        self.recordings = []
        self.messages = []
      
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

        chat_textuel = CTkButton(master=frame, text="Main chat", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        chat_textuel.pack(padx=30, pady=20)

        voice_button = CTkButton(master=frame, text="Voice channel", text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        voice_button.pack(padx=30, pady=20)

        quit_button = CTkButton(master=frame, text="Disconnect",command= self.disconnect ,text_color="#000000", fg_color="#FFFFFF", hover_color="#FFDE00")
        quit_button.pack(padx=30, pady=20,anchor = "s")

        button = CTkButton(self, text="Send", command=self.on_clik_buttonSend, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        button.pack(side=ctk.TOP,ipadx=40)

        self.record_button = CTkButton(self, text="Click to record", command=self.toggle_recording, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        self.record_button.pack(side=ctk.TOP,ipadx=10)

        emoji_button = CTkButton(self, text="Choose an Emoji", command=self.pick_emoji, text_color="#000000", fg_color="#FFFFFF", hover_color="#01b366")
        emoji_button.pack(side=ctk.TOP,ipadx=20)

        self.emoji_picker = None

        self.emojis = ["😊", "😂", "😍", "😎", "🤔", "😴", "🥳", "🎉", "❤️", "👍"] 

        # image = Image.open("app\image\cloche notif.png")  
        # image = image.resize((50, 50))
        # photo = ImageTk.PhotoImage(image)

        # label_notifications = tk.Label(window, image=photo, text="Notifications", compound=tk.LEFT)
        # label_notifications.pack(side=ctk.TOP,ipadx=30)
        # window = tk.Tk()
        # window.title("Instant Messaging")

        
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
            self.master.after(10, self.stop_recording)  

    def save_audio(self, filename):
        if not os.path.exists("audio_recordings"):
            os.makedirs("audio_recordings")
        os.rename(filename, os.path.join("audio_recordings", filename))
        print(f"Enregistrement audio sauvegardé sous : audio_recordings/{filename}")
     
        self.recordings.append(filename)

        with open('audio.json', 'w') as f:
            json.dump(self.recordings, f)

 
    # methods for emojis
    def send_message(self):
        message = self.entry.get()
        if message:
            self.messages_list.insert(tk.END, f"You: {message}")
            self.entry.delete(0, tk.END)

    def pick_emoji(self):
        if not self.emoji_picker:
            self.emoji_picker = tk.Toplevel(self)

            emoji_listbox = tk.Listbox(self.emoji_picker, width=20, height=10)
            for emoji in self.emojis:
                emoji_listbox.insert(tk.END, emoji)
            emoji_listbox.pack(padx=20, pady=20)

            select_button = ttk.Button(self.emoji_picker, text="Select", command=self.select_emoji)
            select_button.pack(pady=5)

            self.emoji_picker.protocol("WM_DELETE_WINDOW", self.close_emoji_picker)

    def select_emoji(self):
        selected_indices = self.emoji_picker.winfo_children()[0].curselection()
        if selected_indices:
            selected_emoji = self.emojis[selected_indices[0]]
            self.entry.insert(tk.END, selected_emoji)
            self.close_emoji_picker()

    def close_emoji_picker(self):
        if self.emoji_picker:
            self.emoji_picker.destroy()
            self.emoji_picker = None


    # # methods for notifications
    # def send_message(self, sender, content):
    #     self.messages.append((sender, content))

    # def display_notifications(self):
    #     if self.messages:
    #         for sender, content in self.messages:
    #             print(f"Notification: New message from {sender}: {content}")
    #     else:
    #         print("No new notifications")

    # def get_notification_count(self):
    #     return len(self.messages)

    # def update_notifications(event):
    #     count = instant_messaging.get_notification_count()
    #     label_notifications.configure(text=f"Notifications ({count})")
    #     label_notifications.bind("<Button-1>", update_notifications)

    #     instant_messaging = MainPage()
    #     instant_messaging.send_message()
    #     instant_messaging.display_notifications()
    #     instant_messaging.get_notification_count()
        

    def disconnect(self):
        self.master.main_page.pack_forget()
        self.master.displayLoginScreen()
        