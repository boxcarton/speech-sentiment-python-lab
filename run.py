import os
import json
from os.path import join, dirname
from dotenv import load_dotenv
from watson_developer_cloud import SpeechToTextV1 as SpeechToText
from watson_developer_cloud import AlchemyLanguageV1 as AlchemyLanguage

from speech_sentiment_python.recorder import Recorder

def transcribe_audio(path_to_audio_file):
    pass

def get_text_sentiment(text):
    pass
    
def main():
    recorder = Recorder("speech.wav")

    print("Please say something nice into the microphone\n")
    recorder.record_to_file()

    print("Transcribing audio....\n")
    result = transcribe_audio('speech.wav')
    
    text = result['results'][0]['alternatives'][0]['transcript']
    print("Text: " + text + "\n")
    
    sentiment, score = get_text_sentiment(text)
    print(sentiment, score)  

if __name__ == '__main__':
    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)
    try:
        main()
    except:
        print("IOError detected, restarting...")
        main()
