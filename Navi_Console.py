#Gerardo Aguayo
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import sys


#Proceso para llamar al reconocimiento de voz
listener = sr.Recognizer()
#Llamar al proceso de Text to Speech
engine = pyttsx3.init()

#Funcion en la que Navi va a poder hablar
def talk(text):
    engine.say(text)
    engine.runAndWait()

#Funcion de reconocimiento de voz
def tomar_comando():
    try:
        with sr.Microphone() as source:
            print('Escuchando...')
            voz = listener.listen(source)
            comando = listener.recognize_google(voz)
            comando = comando.lower()
    except:
        pass
    return comando

def navi():
    comando = tomar_comando()
    print(comando)
#Reproducir musica o videos en YouTube
    if 'reproduce' in comando:
        cancion = comando.replace('reproduce','')
        talk('Reproduciendo ' + cancion)
        print('Reproduciendo' + cancion)
        pywhatkit.playonyt(cancion)
    elif 'pon' in comando:
        cancion = comando.replace('pon','')
        talk('Reproduciendo ' + cancion)
        print('Reproduciendo' + cancion)
        pywhatkit.playonyt(cancion)
#Que Navi te diga la hora
    elif 'hora' in comando:
        hora = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'La hora actual es {hora}')
        print(f'La hora actual es {hora}')
#Hacer que Navi investigue en Wikipedia
    elif 'busca' in comando:
        orden = comando.replace('busca', '')
        wikipedia.set_lang('es')
        info = wikipedia.summary(orden, 1)
        talk(info)
        talk('Aqui tienes la informacion escrita')
        print(info)
    elif 'que es' in comando:
        orden = comando.replace('que es', '')
        wikipedia.set_lang('es')
        info = wikipedia.summary(orden, 1)
        talk(info)
        talk('Aqui tienes la informacion escrita')
        print(info)
    elif 'que significa' in comando:
        orden = comando.replace('que significa', '')
        wikipedia.set_lang('es')
        info = wikipedia.summary(orden, 1)
        talk(info)
        talk('Aqui tienes la informacion escrita')
        print(info)
#Comandos de voz
    elif 'hola' in comando:
        talk(f'Hola!, soy Navi, tu asistente de voz')
        print(f'Hola!, soy Navi, tu asistente de voz')
    elif 'trabajar' in comando:
        talk(f'Claro que si , dime')
        print(f'Claro que si , dime')
        talk('Que quieres que haga por ti?')
        print('Que quieres que haga por ti?')
#Terminar el programa
    elif 'gracias' in comando:
        talk(f'Denada!')
        print(f'Denada!')
        exit()
    elif 'fue todo' in comando:
        talk('Denada, si tienes otro  problema avisame')
        print('Denada, si tienes otro problema avisame')
    else:
        talk('Vuelve a intentarlo')
        print('Vuelve a intentarlo')

navi()