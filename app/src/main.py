from Application import Application
import threading
import sys

if __name__ == "__main__":
    app = Application()
   
    app.start()
    app.screen.mainloop()
    app.stop()

