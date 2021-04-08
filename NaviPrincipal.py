#Gerardo Aguayo
#Librerias necesarias
import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia

#HACER QUE NAVI TE LLAME POR TU NOMBRE
'''
    Para hacer que Navi te llame por tu nombre necesitas ponerlo en la variable 'nombre',
    no olvides que tiene que ir entre comillas. En este caso tendrias que sustituir Itzel
    por la manera en la que quieras que te llame Navi.
'''
Nombre = 'Itzel'

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

#Funcion donde basicamente esta el funcionaminento del programa
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
    else:
        talk('Vuelve a intentarlo')
        print('Vuelve a intentarlo')
#Este while ayuda a que la aplicacion se siga reproduciendo en bucle
#en caso de que no reconozca el comando de voz.
while True:
    navi()