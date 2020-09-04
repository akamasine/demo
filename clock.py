#This is a world clock which shows current time of particular place
import pyfiglet
import time
print("ok,let's begain")
    
def welcome_layout():
    output = pyfiglet.figlet_format("World Clock") 
    print (output)

welcome_layout()