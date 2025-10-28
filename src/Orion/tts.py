"""Text-to-Speech module for Orion"""

import win32com.client
from .config import VOICE_RATE, VOICE_VOLUME


class TTS:
    """Text-to-Speech engine using Windows SAPI"""

    def __init__(self):
        try:
            self.engine = win32com.client.Dispatch("SAPI.SpVoice")
            self._setup_voice()
        except Exception:
            self.engine = None

    def _setup_voice(self):
        """Setup male voice (David)"""
        if self.engine:
            voices = self.engine.GetVoices()
            for voice in voices:
                if 'david' in voice.GetDescription().lower():
                    self.engine.Voice = voice
                    break

    def speak(self, text):
        """Convert text to speech"""
        print(f"Орион: {text}")
        if self.engine:
            try:
                self.engine.Speak(text)
            except Exception:
                pass