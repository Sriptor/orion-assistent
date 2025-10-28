"""Main Orion Assistant class"""

from .tts import TTS
from .stt import STT
from .commands import Commands


class OrionAssistant:
    """Main Orion Voice Assistant"""

    def __init__(self):
        self.tts = TTS()
        self.stt = STT()
        self.commands = Commands()

    def speak(self, text):
        """Speak text"""
        self.tts.speak(text)

    def listen(self):
        """Listen for command"""
        return self.stt.listen()

    def process_command(self, command):
        """Process user command"""
        return self.commands.process(command)

    def run(self):
        """Main assistant loop"""
        self.speak("Привет! Я Орион, ваш голосовой ассистент. Говорите 'Орион' для активации.")

        while True:
            try:
                command = self.listen()

                if not command:
                    continue

                if "орион" in command:
                    self.speak("Да, слушаю вас")
                    user_query = self.listen()

                    if user_query:
                        if any(word in user_query for word in ['стоп', 'выход', 'пока']):
                            self.speak("До свидания!")
                            break

                        response = self.process_command(user_query)
                        self.speak(response)

            except KeyboardInterrupt:
                self.speak("Орион завершает работу")
                break
            except Exception:
                continue