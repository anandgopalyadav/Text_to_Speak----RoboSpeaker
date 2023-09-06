import pyttsx3
print("Welcome to RoboSpeaker Programm....")
engine = pyttsx3.init()
engine.say("Ram Ram ji Saareyaa Nu")
engine.runAndWait()
engine.say("Let's start")
engine.runAndWait()
while True:
    a = input("What you want me to Speak: ")
    if a == "q" or "Q":
        engine.say('Bye bye')
        engine.runAndWait()
        break
    engine.say(a)
    engine.runAndWait()