from backend import Application
from  backend import *

test = Application()

print (test.user.read())
print (test.returnAllMail())
print (test.returnAllName())
print (test.returnAllPassword())

test.displayApp()