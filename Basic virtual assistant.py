"""
Need to have the conda environment
with the following modules:
pyttsx3
SpeechRecognition
PyAudio
conda install PyAudio
pip install pyttsx3
pip install SpeechRecognition
"""

# Importing modules

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')  # sapi5 is the speech engine
voices = engine.getProperty('voices')
print(f'Using: {voices[0].id}')
engine.setProperty('voices', voices[0].id) # here voice id is the inbuilt voice in the computer


# Making a function to output the audio form text input
def speak(audio):
    """
    This function will make the text into speech
    """
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f'user said: {query}')
    except Exception as e:
        speak("Say that again please")
        return "none"
    return query






if __name__ == "__main__":
    # speak('Hello sir')
    takeCommand()
