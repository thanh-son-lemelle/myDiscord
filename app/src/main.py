from Application import Application
import threading
import sys

if __name__ == "__main__":
    app = Application()
    
    app.show_mess()
    app.receive_input()
    app.screen.mainloop()
    app.quit()
