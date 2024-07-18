import os
from selenium import webdriver
import pygame
import pyautogui
from gtts import gTTS


from math import floor
import speech_recognition

import datetime
from AppOpener import open
from AppOpener import close
import webbrowser




pygame.init()
recognitor = speech_recognition.Recognizer()



while True:

    def audio_rec2():
        with speech_recognition.Microphone() as source:
            print("Listening...")
            audio = recognitor.listen(source)
        print("Turning Your words to text...")
        try:
            text = recognitor.recognize_google(audio, language='en-EN')
            return text
        except speech_recognition.UnknownValueError:
            print("I don't understand")
            return None
    def audio_rec():
        with speech_recognition.Microphone() as source:
            print("Listening...")
            audio = recognitor.listen(source)
        print("Turning Your words to text...")
        try:
            text = recognitor.recognize_google(audio, language='en-EN')
            return text
        except speech_recognition.UnknownValueError:
            print("I don't understand")
            return None


    result = audio_rec()



    if result:
        print("You said:", result)


    if result.lower() == "hello":

        about = "HI! how are you?"

        tts = gTTS(about, lang="en")
        tts.save("voice/about.mp3")
        pygame.mixer.music.load("voice/about.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif "good" in result.lower():

        mood = "I'm good too"

        tts = gTTS(mood, lang="en")
        tts.save("voice/mood.mp3")
        pygame.mixer.music.load("voice/mood.mp3")
        pygame.mixer.music.lggitplay()

        while pygame.mixer.music.get_busy():
            continue

    elif "functions" in result.lower():

        AI_functions = ("I can control with your device. Open apps and close apps, control volume,"
                        "turn off your device and show date")

        tts = gTTS(AI_functions, lang="en")
        tts.save("voice/mood.mp3")
        pygame.mixer.music.load("voice/mood.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif result.lower() == "open telegram":

        opening3 = "I'm opening telegram"

        tts = gTTS(opening3, lang="en")
        tts.save("voice/openapp3.mp3")
        pygame.mixer.music.load("voice/openapp3.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        open("telegram", match_closest=True)




    elif result.lower() == "close telegram":

        closing3 = "I'm closing telegram"

        tts = gTTS(closing3, lang="en")
        tts.save("voice/closeapp3.mp3")
        pygame.mixer.music.load("voice/closeapp3.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        close("telegram", match_closest=True)

    elif result.lower() == "open google":

        opening2 = "I'm opening google"

        tts = gTTS(opening2, lang="en")
        tts.save("voice/openapp2.mp3")
        pygame.mixer.music.load("voice/openapp2.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        open("google chrome", match_closest=True)


    elif result.lower() == "close google":

        closing2 = "I'm closing google"

        tts = gTTS(closing2, lang="en")
        tts.save("voice/closeapp2.mp3")
        pygame.mixer.music.load("voice/closeapp2.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        close("google chrome", match_closest=True)


    elif result.lower() == "open firefox":
        opening1 = "I'm opening firefox"
        tts = gTTS(opening1, lang="en")
        tts.save("voice/openapp1.mp3")
        pygame.mixer.music.load("voice/openapp1.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue
        open("firefox", match_closest=True)


    elif result.lower() == "close firefox":

        closing1 = "I'm closing firefox"

        tts = gTTS(closing1, lang="en")
        tts.save("voice/closeapp1.mp3")
        pygame.mixer.music.load("voice/closeapp1.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        close("firefox", match_closest=True)


    elif result.lower() == "stop":

        print("Turning off")

        breakUp = "I'm turning off, bye dear user"

        tts = gTTS(breakUp, lang="en")
        tts.save("voice/get_out.mp3")
        pygame.mixer.music.load("voice/get_out.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

        break


    elif result.lower() == "what date":

        today = datetime.date.today()

        print(today)

        tts = gTTS("I wrote it in terminal", lang="en")
        tts.save("voice/outvoice3.mp3")
        pygame.mixer.music.load("voice/outvoice3.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue


    elif "volume up to" in result.lower():

        volumeUp = result.split("to")
        volume = int(volumeUp[1].split()[0])
        pyautogui.press("volumeup", floor(volume/2))

        output = "Volume turned up"

        print("Volume turned up")

        tts = gTTS(output, lang="en")
        tts.save("voice/outvoice2.mp3")
        pygame.mixer.music.load("voice/outvoice2.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue


    elif "volume down to" in result.lower():
        volumeUp = result.split("to")
        volume = int(volumeUp[1].split()[0])
        pyautogui.press("volumedown", floor(volume/2))
        output = "Volume turned down"

        print("Volume turned down")

        tts = gTTS(output, lang="en")
        tts.save("voice/outvoice.mp3")
        pygame.mixer.music.load("voice/outvoice.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue
    elif result.lower() == "open mars":

        school = "I'm opening Mars"

        webbrowser.open("https://space.marsit.uz/")

        tts = gTTS(school, lang="en")
        tts.save("voice/school.mp3")
        pygame.mixer.music.load("voice/school.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif result.lower() == "close mars":

        noSchool = "I'm closing Mars"

        site3 = webdriver.Chrome()
        site3.get("https://space.marsit.uz/")
        site3.close()

        tts = gTTS(noSchool, lang="en")
        tts.save("voice/noschool.mp3")
        pygame.mixer.music.load("voice/noschool.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue


    elif result.lower() == "open pylearning":

        python = "I'm opening pylearning"

        webbrowser.open("http://pylearning.uz/")

        tts = gTTS(python, lang="en")
        tts.save("voice/python.mp3")
        pygame.mixer.music.load("voice/python.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif result.lower() == "close pylearning":

        noPython = "I'm closing pylearning"

        site2 = webdriver.Chrome()
        site2.get("http://pylearning.uz/")
        site2.close()

        tts = gTTS(noPython, lang="en")
        tts.save("voice/nopython.mp3")
        pygame.mixer.music.load("voice/nopython.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif result.lower() == "open youtube":

        youtube = "I'm opening youtube"

        webbrowser.open("https://www.youtube.com/")

        tts = gTTS(youtube, lang="en")
        tts.save("voice/youtube.mp3")
        pygame.mixer.music.load("voice/youtube.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif result.lower() == "close youtube":

        noYoutube = "I'm closing youtube"
        site = webdriver.Chrome()


        site.get("https://www.youtube.com/")
        site.close()

        tts = gTTS(noYoutube, lang="en")
        tts.save("voice/noyoutube.mp3")
        pygame.mixer.music.load("voice/noyoutube.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue

    elif result.lower() == "shut down":

        end = "Shutting down in 5 seconds, bye (say 'stop' to stop process)"

        tts = gTTS(end, lang="en")
        tts.save("voice/end.mp3")
        pygame.mixer.music.load("voice/end.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue



        result2 = audio_rec2()


        if "stop" in result2.lower():
            print("Process is stopped")
            stopped2 = "Process is stopped"
            tts = gTTS(stopped2, lang="en")
            tts.save("voice/stopped2.mp3")
            pygame.mixer.music.load("voice/stopped2.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

            continue
        else:
            os.system("shutdown /s /t 5")



    elif result.lower() == "reboot":

        reboot = "Reboot down in 5 seconds, bye (say 'stop' to stop process)"

        tts = gTTS(reboot, lang="en")
        tts.save("voice/reboot.mp3")
        pygame.mixer.music.load("voice/reboot.mp3")
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            continue


        result2 = audio_rec2()


        if "stop" in result2.lower():
            print("Process is stopped")
            stopped = "Process is stopped"
            tts = gTTS(stopped, lang="en")
            tts.save("voice/stopped.mp3")
            pygame.mixer.music.load("voice/stopped.mp3")
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                continue

            continue
        else:
            os.system("shutdown /r /t 5")






