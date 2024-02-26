import tkinter as tk
import sounddevice as sd
import soundfile as sf
import threading
import os
import json
from datetime import datetime

class AudioRecorderApp:
    def __init__(self, master):
        self.master = master
        master.title("Enregistreur audio")

        self.record_button = tk.Button(master, text="Enregistrer", command=self.toggle_recording)
        self.record_button.pack()

        self.recording = False
        self.recordings = []

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

root = tk.Tk()
app = AudioRecorderApp(root)
root.mainloop()
