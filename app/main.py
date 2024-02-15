from backend import app
from  backend import *

test = Root()

print(test.utilisateur.read())
print (test.returnAllMail())
print (test.returnAllName())
print (test.returnAllPassword())

test.displayApp()