# import speech_recognition as sr
# import webbrowser
# import pyttsx3

# # obtain audio from the microphone
# r = sr.Recognizer()
# engine = pyttsx3.init()

# engine.say("Hi Noble, Thanks for developing this speech recognition app. Noble you are the greatest developer ever ,")
# engine.runAndWait()
# with sr.Microphone() as source:
#     print("Say something!")
#     audio = r.listen(source)

# # recognize speech using Google Speech Recognition
# try:
#     command = r.recognize_google(audio)
#     print("You said: " + command)
# except sr.UnknownValueError:
#     print("Google Speech Recognition could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Google Speech Recognition service; {0}".format(e))

# # check if the command is to open YouTube and play a video
# if "play" in command and "YouTube" in command:
#     video = command.split("play")[-1].strip()
#     engine.say("Hi Mr Noble Mutuwa , i heard  you say " + command)
#     engine.runAndWait()
#     url = f"https://www.youtube.com/results?search_query={video}"
#     webbrowser.open_new_tab(url)
import speech_recognition as sr
import os
import pyttsx3

# Initialize the recognizer
engine = pyttsx3.init()
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Speech recognition using Google Speech Recognition
try:
    command = r.recognize_google(audio)
    # print("You said: " + command)
    # if "open whatsapp" in command.lower():
    #     # os.system("open -a /Applications/WhatsApp.app") # for MacOS
    #     os.system("start whatsapp") # for Windows
    if "open whatsapp" in command.lower():
       
        # 060os.system(f"open -a /Applications/WhatsApp.app 'https://wa.me/{number}'") # for MacOS
        engine.say("Hi Mr Noble Mutuwa , please enter the number to send message to " )
        engine.runAndWait()
        number = input("Enter the number to text: ")
        engine.say("Mr Noble are you sure you want to text this person")
        engine.runAndWait()
        os.system(f"start https://wa.me/{number}") # for Windows
    else:
        print("Command not recognized")
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
