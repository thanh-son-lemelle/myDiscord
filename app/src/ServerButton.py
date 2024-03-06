from customtkinter import CTkButton

class ServerButton(CTkButton):
    def __init__(self, master, main_page, server_name, serverID, userID):
        super().__init__(master)
        self.main_page = main_page
        self.server_name = server_name
        self.userID = userID
        self.serverID = serverID
        self.list_channels = self.get_channel_by_serverID(serverID)
        print("list_channels into serverbutton", self.list_channels)
        self.create_widgets()

    def create_widgets(self):
        self.configure(text=self.server_name, command=self.on_click, fg_color="transparent", hover_color="#FFAB00", width=20, height=2, font=("Arial", 16))

    def on_click(self):
        print(f"Server {self.server_name, self.serverID} clicked")
        self.main_page.swap_server_page(self.userID, self.serverID, self.list_channels)
        print(f"Server {self.server_name} clicked")
    
    def get_channel_by_serverID(self, serverID):
        result = self.main_page.get_channel_by_serverID(serverID)
        result.pop(0)
        return result
    