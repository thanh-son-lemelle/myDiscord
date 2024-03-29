# myDiscord
# Hi Plateformers👋
# <p align="center">My Discord</p>
  
We are a group of 3 people and we need to create an instant messenger like Discord. We had 4 weeks to realize this project.
In this project there must be this :

- Communicate with others
- Using text and voice channels, public and private.
- Retrieve messages already posted with time and author.
- React to messages posted using emojis.
- Several channels available to users.
- Log in or create your account to have access to the main channel.
- Information for registration: name, first name, email and password.
- Logout button to return the user to the login page.
- Rights management so that certain users manage the different channels.
- Notification system.
- Use one class per file and one database with multiple tables.
    
## 🧐 Features    
- Feature 1 : Register - function to create an ID with name, lastname, email and password
- Feature 2 : Login - function to log your ID and to acces the tchat
- Feature 3 : Remember me - function to remerber the ID
- Feature 4 : Tchat rooms - function to chose the tchat room
- Feature 5 : Text message - function to write in the tchat room
- Feature 6 : Vocal message - function to speek in the tchat room
- Feature 7 : Emoji - function to react to messages
        
## 🛠️ Tech Stack
- [Python](https://www.python.org/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [MySQL](https://www.mysql.com/fr/)
- [Trello](https://trello.com/fr)
- [Dbdiagram](https://dbdiagram.io/home)
- [Miro](https://miro.com/fr/)
- [Figma](https://www.figma.com/)
- [Github](https://github.com/)
    
## 🛠️ Install Dependencies    
```bash
pip install customtkinter
pip install sounddevice
pip install soundfile
pip install mysql-collector
pip install keyring
pip install bcrypt
```

        
| User | Channel | Message | Server  | Server-members | Reaction
| -------- | -------- | -------- | -------- | -------- | -------- | 
| User-ID    | Channel-ID | Message ID | Server ID | Member ship ID | Reaction ID
| Name | Channel name    | Content  | Server name | User ID | Emoji
| Firstname   | Channel type  | Date time  | Description | Server ID | Message ID
| Password  | Server ID    | User ID   | Type | Rôle | User ID
| Mail   |   | Type    | Owner  | 
| Auth-Token  |    | Channel ID  | Server image
| Statut   |     |     | Creation name
| Creation name   |     |     |
        
## 🧑🏻‍💻 Usage
```js
from src import Controller

if __name__ == '__main__':
    controller = Controller.Controller()
    controller.main()
}
```
        
## 🙇 Acknowledgements      
- [Awesome README]()
- [GitHub Emoji Cheat Sheet]()
- [GitHub Markdown Emoji]()
        
## 🍰 Contributing    
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
        
## 🙇 Authors
#### Thanh Lemelle, Lyes Hamici, Kheira Lakhezoum