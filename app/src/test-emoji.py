import tkinter as tk
from tkinter import ttk

class ChatApp:
    def __init__(self, master):
        self.master = master
        master.title("Messagerie Instantanée")

        self.messages_frame = tk.Frame(master)
        self.messages_frame.pack()

        scrollbar = tk.Scrollbar(self.messages_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.messages_list = tk.Listbox(self.messages_frame, height=15, width=50, yscrollcommand=scrollbar.set, font=('Segoe UI Emoji', 20))
        self.messages_list.pack(side=tk.LEFT, fill=tk.BOTH)
        scrollbar.config(command=self.messages_list.yview)

        self.entry = tk.Entry(master, width=50)
        self.entry.pack()

        send_button = tk.Button(master, text="Envoyer", command=self.send_message)
        send_button.pack()

        emoji_button = tk.Button(master, text="Choisir Emoji", command=self.pick_emoji)
        emoji_button.pack()

        self.emoji_picker = None

        self.emojis = ["😊", "😂", "😍", "😎", "🤔", "😴", "🥳", "🎉", "❤️", "👍"] 

    def send_message(self):
        message = self.entry.get()
        if message:
            self.messages_list.insert(tk.END, f"You: {message}")
            self.entry.delete(0, tk.END)

    def pick_emoji(self):
        if not self.emoji_picker:
            self.emoji_picker = tk.Toplevel(self.master)
            self.emoji_picker.title("Sélectionner un emoji")

            emoji_listbox = tk.Listbox(self.emoji_picker, width=10, height=5)
            for emoji in self.emojis:
                emoji_listbox.insert(tk.END, emoji)
            emoji_listbox.pack(padx=10, pady=10)

            select_button = ttk.Button(self.emoji_picker, text="Sélectionner", command=self.select_emoji)
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

root = tk.Tk()
app = ChatApp(root)
root.mainloop()
