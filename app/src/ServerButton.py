import customtkinter as ctk

class ServerButton(ctk.CTkButton):
    def __init__(self, master, server_name, server_id, server_icon, server_description, position):
        super().__init__(master)
        self.server_name = server_name
        self.server_id = server_id
        self.server_icon = server_icon
        self.server_description = server_description
        self.position = position
        self.create_widgets()

    def create_widgets(self):
        self.config(text=self.server_name, command=self.on_click, fg_color="#000000", bg_color="#01b366", hover_color="#FFDE00", width=20, height=2, font=("Arial", 16))

    def on_click(self):
        self.master.display_server_page(self.server_id, self.server_name, self.server_icon, self.server_description)