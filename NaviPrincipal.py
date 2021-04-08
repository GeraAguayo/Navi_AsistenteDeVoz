#Gerardo Aguayo
#Librerias necesarias
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia

#Proceso para llamar al reconocimiento de voz
listener = sr.Recognizer()
#Llamar al proceso de Text to Speech
engine = pyttsx3.init()

#Funcion de reconocimiento de voz
def take_command():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
    except:
        pass
    return command
