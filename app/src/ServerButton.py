import customtkinter as ctk

class ServerButton(ctk.CTkButton):
    def __init__(self, master, server_name, server_icon, server_description, is_last=False):
        super().__init__(master)
        self.server_name = server_name
        """self.server_id = server_id"""
        self.server_icon = server_icon
        self.server_description = server_description
        self.is_last = is_last
        """self.userID = userId"""
        self.create_widgets()
        """self.userID = self.master.get_user_information()[0]"""

    def create_widgets(self):
        self.configure(text=self.server_name, command=self.on_click, fg_color="#000000", bg_color="#01b366", hover_color="#FFDE00", width=20, height=2, font=("Arial", 16))

    def on_click(self):
        if self.is_last==False:
            self.master.display_server_page(self.server_name, self.server_icon, self.server_description)
        else:
            self.add_server()

    def add_server(self):
        self.master.display_add_server_page()

    def get_user_servers(self):
        return self.master.get_user_servers(self.userID)[3]
    

