import pyttsx3
import time

synthesizer = pyttsx3.init()
voices = synthesizer.getProperty('voices')

synthesizer.setProperty('voice', voices[0].id)
   
print("Powered By 'pyttsx3'")
synthesizer.say("Powered By pyttsx3")
synthesizer.runAndWait() 
synthesizer.stop()

print("Created By Amethyst")
synthesizer.say("Created By Amethyst")
synthesizer.runAndWait() 
synthesizer.stop()

time.sleep(3)
   
my_text = input("Enter the text: ")
synthesizer.say(my_text) 
synthesizer.runAndWait() 
synthesizer.stop()
    
