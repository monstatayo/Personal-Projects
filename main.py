import speech_recognition as sr
import pyaudio
from pynput.keyboard import Key, Controller
import keyboard 
import time
from playsound import playsound
#play on

playsound('voiceinit.wav')

while(True):

    k = Controller()
    r = sr.Recognizer()

    if keyboard.is_pressed('i'):
            
        playsound('voicepush.wav')

        with sr.Microphone() as source:

            print("Enter your input")
            audio = r.listen(source)

            try:
                text = r.recognize_google(audio)
                print("AUDIO CAPTURE SUCCESSFUL\n")
                print("Phrase captured : {}".format(text))
                
                time.sleep(2)

                for char in text:    
                    k.press(char)
                    k.release(char)
                    time.sleep(0.12)

            


            except:
                print("Voice recognition failed")

            
            playsound('voicerelease.wav')

    elif keyboard.is_pressed('p'):
        playsound('goodbye.wav')
        exit()
