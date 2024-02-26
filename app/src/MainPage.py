import customtkinter as ctk
from customtkinter import *
from customtkinter.assets import *
import tkinter as tk
import sounddevice as sd
import soundfile as sf
import threading

class MainPage(CTkFrame):
    def __init__(self, master):
        
        super().__init__(master)
        self.running = True
        self.creat_widgets()
        self.master = master
        self.commande = "" 
        self.recording = False

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
        
        self.label = tk.Label(self.master, text="Cliquez sur Enregistrer pour commencer l'enregistrement.")
        self.label.pack()

        self.record_button = tk.Button(self.master, text="Enregistrer", command=self.toggle_recording)
        self.record_button.pack()


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
        self.record_button.config(text="Arrêter l'enregistrement")
        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()


    def stop_recording(self):
        self.recording = False
        self.record_button.config(text="Enregistrer")


    def toggle_recording(self):
        if self.recording:
            self.stop_recording()
        else:
            self.start_recording()


    def record_audio(self):
        duration = 10  # Durée de l'enregistrement en secondes
        fs = 44100  # Fréquence d'échantillonnage
        try:
            with sf.SoundFile('enregistrement.wav', mode='x', samplerate=fs, channels=2) as file:
                with sd.InputStream(callback=lambda data, frames, time, status: file.write(data)):
                    sd.sleep(int(duration * 1000))
        except Exception as e:
            print("Une erreur est survenue lors de l'enregistrement :", e)
        finally:
            self.master.after(10, self.stop_recording)  # Arrête l'enregistrement après la durée spécifiée

            
    def disconnect(self):
        self.master.main_page.pack_forget()
        self.master.displayLoginScreen()