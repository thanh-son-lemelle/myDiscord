import time
from plyer import notification


if __name__=="__main__":

		notification.notify(
			title = "HEADING HERE",
			message=" DESCRIPTION HERE" ,
		
			# displaying time
			timeout=2
)
		# waiting time
		time.sleep(7)


notification.notify(title='test', message='test', app_name='test', app_icon=None, timeout=10, ticker='test', toast=False)