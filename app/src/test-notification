import tkinter as tk
from PIL import Image, ImageTk

class InstantMessaging:
    def __init__(self):
        self.messages = []

    def send_message(self, sender, content):
        self.messages.append((sender, content))

    def display_notifications(self):
        if self.messages:
            for sender, content in self.messages:
                print(f"Notification: New message from {sender}: {content}")
        else:
            print("No new notifications")

    def get_notification_count(self):
        return len(self.messages)

def update_notifications(event):
    count = instant_messaging.get_notification_count()
    label_notifications.config(text=f"Notifications ({count})")

instant_messaging = InstantMessaging()
instant_messaging.send_message("Kheira", "Hi Lyes and Thanh, how are you?")
instant_messaging.send_message("Thanh", "I'm good, and you?")
instant_messaging.send_message("Lyes", "I'm alright, guy's!")
instant_messaging.send_message("Kheira", "I'm good too !")

window = tk.Tk()
window.title("Instant Messaging")

image = Image.open("app\image\cloche notif.png")  
image = image.resize((50, 50))
photo = ImageTk.PhotoImage(image)

label_notifications = tk.Label(window, image=photo, text="Notifications", compound=tk.LEFT)
label_notifications.pack()

label_notifications.bind("<Button-1>", update_notifications)

window.mainloop()
