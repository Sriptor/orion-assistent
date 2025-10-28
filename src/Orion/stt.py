"""Speech-to-Text module for Orion"""

import speech_recognition as sr


class STT:
    """Speech-to-Text engine using Google Speech Recognition"""

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """Listen for speech and convert to text"""
        with self.microphone as source:
            print("Слушаю...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                text = self.recognizer.recognize_google(audio, language="ru-RU")
                print(f"Вы: {text}")
                return text.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                print("Не расслышал, повторите")
                return ""
            except sr.RequestError:
                print("Проблема с подключением")
                return ""