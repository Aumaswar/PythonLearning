print('''Back from his trip, he's at the door
When he gets back, he's on the phone
Innocent eye, innocent heart
No, it's not wrong, but it's not right
Innocent time, out on his own
Not gonna do that, fuck, I'm out of control
I was just bored, playin' the guitar
Learned all your tricks, wasn't too hard''')

import pyttsx3
engine = pyttsx3.init()

engine.say("My name is ommm")
engine.runAndWait()


# this imports the built in os module
import os
# this is for the specific directory 
files = os.listdir()  
# this is for printing the directory files
for f in files:
    print(f)