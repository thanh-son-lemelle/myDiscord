import time
from plyer import notification

from .Model import Model


if __name__=="__main__":

		notification.notify(
			title = "HEADING HERE",
			message=" DESCRIPTION HERE" ,
		
			# displaying time
			timeout=2
)
		# waiting time
		time.sleep(7)

class Notif_service:
    def __init__(self):
        self.model = Model()
        self.userID = ""

    def send_notif(self, title, message, app_icon, timeout, ticker, toast):
        notification.notify(title=title, message=message, app_name='Harmony', app_icon=app_icon, timeout=timeout, ticker=ticker, toast=toast)
        time.sleep(7)

    def get_current_userID(self, username):
        return self.model.get_user_information_by_username(username)[0]
    
    