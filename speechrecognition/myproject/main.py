import pyttsx3
import speech_recognition
import dbconnection
import datetime
import winsound
import pyaudio
import wave
import keyboard
from flask import Flask
from flask_restful import Resource , Api , request
import flet as ft
"""here flask app starts here"""
"""app = Flask("virtual assistant")
@app.route('/listen', methods=['POST'])
def listen_endpoint():
    text = listen()
    return text, 200


if __name__ == '__main__':
    app.run()
"""




"""initialization and configuration """
engine = pyttsx3.init()
male_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
engine.setProperty('voice', 'en')
engine.setProperty('voice', male_voice_id)
stop= False
"""do this when the response is found """
def speak(text):
    print("saying ......")
    engine.say(text)
    engine.runAndWait()

"""this function is to specify the request type """
def specify(text):
    if "joke" in text:
        current_joke = dbconnection.selectRandomJoke()
        speak(current_joke)
        speak("do you need anything else ? ")
        listen()

    elif "time" in text:
        now = datetime.datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
        speak(formatted_datetime)
        speak("do you need anything else ? ")
        listen()
    elif "music" in text:
        music()
        """winsound.PlaySound('song1.wav', 0)
        winsound.PlaySound(None, 0)"""
        speak("do you need anything else ? ")
        listen()
    elif "lesson" in text:
        speak(dbconnection.get_next_lesson())
        speak("do you need anything else ? ")
        listen()
    elif "finish" in text:
        speak("glad to serve you , press the mic button again if you need me")

    else:
        speak("I'm not sure what you're asking for.")
        listen()

"""function to be called when the mic button is on hold"""
def listen():
    recognizer = speech_recognition.Recognizer()
    while True :
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print(f'You said: {text}')
                specify(text)
            return text
        except speech_recognition.UnknownValueError:
            speak("sorry I didn't understand your audio ")
            recognizer = speech_recognition.Recognizer()
            continue
        finally:
            return text
def music():
    filename = "song1.wav"  # Replace with your actual file path  ssss
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()
    channels = wf.getnchannels()
    sample_width = wf.getsampwidth()
    framerate = wf.getframerate()
    chunk = 1024  # Read audio data in chunks of 1024 bytes

    stream = p.open(format=p.get_format_from_width(sample_width),
                    channels=channels,
                    rate=framerate,
                    output=True)
    data = wf.readframes(chunk)
    print("preparing to play")
    while data :
        print("playing")
        stream.write(data)
        data = wf.readframes(chunk)
        if keyboard.is_pressed('s'):
            break

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()

"""flet try"""
"""def main(page: ft.Page):
    page.title = ' Virtual Assisstant Prototype'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    welcome_textbox = ft.TextField(value="Hello , I'm your virtual assistant", text_align=ft.TextAlign.CENTER, width=360)

    def listen_to(e):
        listen()

    page.add(ft.Row([
        ft.IconButton(ft.icons.MIC,on_click=listen_to),
        welcome_textbox


    ],alignment=ft.MainAxisAlignment.CENTER))
ft.app(main)"""

speak("Hello i am your virtual assistant , how can i help you today ?? ")
listen()