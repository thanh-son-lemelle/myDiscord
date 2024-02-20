import tkinter as tk
import customtkinter as ctk
from PIL import Image


class LoginScreen(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.user_entry = ''
        self.user_pass = ''
        self.create_widgets()
    #testing
        """self.status = True
        
        ctk.set_appearance_mode("dark") 
  
        # Selecting color theme-blue, green, dark-blue 
        ctk.set_default_color_theme("green") 

        self.application = ctk.CTk()"""#testing

        """self.image = Image.open("image\\background.gif")
        self.backgroundImage = ctk.CTkImage(self.image, size = (1482,834))"""
        """self.application.geometry("1482x834")
        """

        """app.after(0, lambda:app.state('zoomed'))"""


    """    def bg_resizer(self,e):
        if e.widget is self.app:
            i = ctk.CTkImage(self.image, size=(e.width, e.height))
            self.bg_lbl.configure(text="", image=i)"""
    #testing
    """
    def get_input_values(self):
        name = self.user_entry.get()
        psswd = self.user_pass.get()
        return name, psswd


    def get_login(self):
        return self.login

    def set_loginAtTrue(self):
        self.get_input_values()
        self.login = True
        self.application.quit()
        self.application.destroy()
    
    def set_register_userAtTrue(self):
        self.register_user = True
        self.application.quit()
        self.application.destroy()
    

    # Create a bg label
    def displayLoginScreen(self):""" 
    #testing

    """     bg_lbl = ctk.CTkLabel(self.app, text="", image=self.backgroundImage)
        bg_lbl.place(x=0, y=0)"""
    """
        # Create a frame 
        frame = ctk.CTkFrame(master=self.application, width=1482, height=834, corner_radius=45,)

        frame.pack(pady=40,padx=300, fill='both',expand= False, side="top", anchor="center")
        """#testing
    """     frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)"""
    """
        # Set the label inside the frame 
        label = ctk.CTkLabel(master=frame, 
                            text='HARMONY',
                            font=('helvetica',64)) 
        label.pack(pady=12,padx=10) 
        
        # Create the text box for taking 
        # username input from user 
        self.user_entry= ctk.CTkEntry(master=frame, 
                                placeholder_text="Pseudo/mail") 
        self.user_entry.pack(pady=12,padx=10) 
        
        # Create a text box for taking  
        # password input from user 
        self.user_pass= ctk.CTkEntry(master=frame, 
                                placeholder_text="mot de passe", 
                                show="*") 
        self.user_pass.pack(pady=12,padx=10) 
        
        # Create a login button to login 
        button = ctk.CTkButton(master=frame, 
                            text='Login',command= self.set_loginAtTrue)
        button.pack(pady=12,padx=10)
        
        # Create a remember me checkbox 
        checkbox = ctk.CTkCheckBox(master=frame, 
                                text='Remember Me') 
        checkbox.pack(pady=12,padx=10) 

        # Create a register_user button link
        button = ctk.CTkButton(master=frame,
                            text='register_user',command= self.set_register_userAtTrue)
        button.pack(pady=12,padx=10)
        """#testing


    """     self.app.bind("<Configure>", self.bg_resizer)"""
    """     self.application.mainloop()
        return self.get_input_values()"""
    def create_widgets(self):
            frame = ctk.CTkFrame(master=self, width=1482, height=834, corner_radius=45)
            frame.pack(pady=40, padx=300, fill='both', expand=False, side="top", anchor="center")
            
            label = ctk.CTkLabel(master=frame, text='HARMONY', font=('helvetica', 64))
            label.pack(pady=12, padx=10)

            self.user_entry = ctk.CTkEntry(master=frame, placeholder_text="Pseudo/mail")
            self.user_entry.pack(pady=12, padx=10)

            self.user_pass = ctk.CTkEntry(master=frame, placeholder_text="mot de passe", show="*")
            self.user_pass.pack(pady=12, padx=10)

            login_button = ctk.CTkButton(master=frame, text='Login', command=self.go_to_MainPage)
            login_button.pack(pady=12, padx=10)

            remember_checkbox = ctk.CTkCheckBox(master=frame, text='Remember Me')
            remember_checkbox.pack(pady=12, padx=10)

            register_button = ctk.CTkButton(master=frame, text='Register', command=self.set_register_true)
            register_button.pack(pady=12, padx=10)

    def get_permission(self):
        print ("test")

    def go_to_MainPage(self):
        self.get_permission()
        self.master.displayMainPage()
        # Handle further actions here

    def set_register_true(self):
        self.master.displayRegisterPage()
        # Handle further actions here

    def get_input_values(self):
        name = self.user_entry.get()
        psswd = self.user_pass.get()
        return name, psswd

    def get_login_status(self):
        return self.login

    def get_register_status(self):
        return self.register