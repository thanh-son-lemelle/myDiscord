import tkinter as tk
import customtkinter as ctk
from PIL import Image

def bg_resizer(e):
    if e.widget is app:
        i = ctk.CTkImage(image, size=(e.width, e.height))
        bg_lbl.configure(text="", image=i)

def get_input_values():
    name = user_entry.get()
    psswd = user_pass.get()
    print("Valeur de l'entrée 1:", name)
    print("Valeur de l'entrée 2:", psswd)


ctk.set_appearance_mode("dark") 
  
# Selecting color theme-blue, green, dark-blue 
ctk.set_default_color_theme("green") 

app = ctk.CTk()

image = Image.open("image\\background.gif")
backgroundImage = ctk.CTkImage(image, size = (1482,834))
app.geometry("1482x834")

"""app.after(0, lambda:app.state('zoomed'))"""

# Create a bg label

bg_lbl = ctk.CTkLabel(app, text="", image=backgroundImage)
bg_lbl.place(x=0, y=0)

# Create a frame 
frame = ctk.CTkFrame(master=app, width=1482, height=834, corner_radius=45,)

frame.pack(pady=40,padx=300, fill='both',expand= False, side="top", anchor="center")
"""frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)"""
  
# Set the label inside the frame 
label = ctk.CTkLabel(master=frame, 
                     text='HARMONY',
                     font=('helvetica',64)) 
label.pack(pady=12,padx=10) 
  
# Create the text box for taking 
# username input from user 
user_entry= ctk.CTkEntry(master=frame, 
                         placeholder_text="Pseudo/mail") 
user_entry.pack(pady=12,padx=10) 
  
# Create a text box for taking  
# password input from user 
user_pass= ctk.CTkEntry(master=frame, 
                        placeholder_text="mot de passe", 
                        show="*") 
user_pass.pack(pady=12,padx=10) 
  
# Create a login button to login 
button = ctk.CTkButton(master=frame, 
                       text='Login',command= get_input_values) 
button.pack(pady=12,padx=10, side='right')
  
# Create a remember me checkbox 
checkbox = ctk.CTkCheckBox(master=frame, 
                           text='Remember Me') 
checkbox.pack(pady=12,padx=10) 

# Create a register button link
button = ctk.CTkButton(master=frame,
                       text='register',command='')
button.pack(pady=12,padx=10)


app.bind("<Configure>", bg_resizer)
app.mainloop()
#okokok
