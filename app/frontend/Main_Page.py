import customtkinter as ctk
from customtkinter import *

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.after(0, lambda: app.state('zoomed'))
app.minsize(width=800, height=400)

frame = CTkFrame(master=app, fg_color="#01b366", border_color="#FFFFFF", border_width=2,width=700)
frame.pack(expand=False,side = LEFT, fill = Y)


frame2 = CTkFrame(master=app, fg_color="#383838", border_color="#FFFFFF", border_width=2,width=700)
frame2.pack(expand=True,fill = 'both')  # Utilisation de pack pour étirer la frame dans toutes les directions

label = CTkLabel(master=frame, text="Canaux", text_color="#000000")
label.pack(side="top", pady=(10, 0))  # Utilisation de pack pour positionner le label en haut

button_textuel = CTkButton(master=frame, text="Salon textuel", text_color="#000000", fg_color="#FFFFFF",hover_color="#FFDE00").pack(padx=30, pady=20)


button_vocal = CTkButton(master=frame, text="Salon vocal", text_color="#000000", fg_color="#FFFFFF",hover_color="#FFDE00").pack(padx=30, pady=20)


def on_button_click():
    user_input = entry.get()
    resultat_label.configure(text=user_input)

entry = CTkEntry(frame2 ,text_color="#000000" ,fg_color="#FFFFFF",width=1200)
entry.pack(side = BOTTOM,pady = 10)  # Utilisation de pack pour positionner l'entrée en bas

button = CTkButton(frame2, text="Envoyer", command=on_button_click, text_color="#000000", fg_color="#FFFFFF",hover_color="#01b366")
button.pack(side=BOTTOM, ipadx=40)  # Utilisation de pack pour positionner le bouton en bas

resultat_label = CTkLabel(frame2, text="")
resultat_label.pack(side = TOP , pady=10)

app.mainloop()
