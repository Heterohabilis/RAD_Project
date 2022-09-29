import speech_recognition as sr
r=sr.Recognizer()
condi=True
while condi:
    with sr.Microphone() as source:
        print("Talking...")
        audio_text=r.record(source,duration=5)
        print("Time over, thanks!")
        try:
            if r.recognize_google(audio_text).__contains__("stop"):
                condi=False
            print("Text:"+r.recognize_google(audio_text,language="en-us"))

        except:
            print("sorry, I did not get that")

print("Thanks for using!")
