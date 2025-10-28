"""Command processing module for Orion"""

import requests
import os
import webbrowser
import subprocess
import platform
import threading
import time
from datetime import datetime
from .config import WEATHER_API_KEY, DEFAULT_CITY, APPS
from .ai import AI


class Commands:
    """Command processor for Orion"""

    def __init__(self):
        self.ai = AI()
        self.current_city = DEFAULT_CITY
        self.reminders = []

    def get_weather(self, city=None):
        """Get weather information"""
        if city is None:
            city = self.current_city

        try:
            params = {
                'key': WEATHER_API_KEY,
                'q': city,
                'lang': 'ru'
            }
            response = requests.get('https://api.weatherapi.com/v1/current.json', params=params, timeout=5)

            if response.status_code == 200:
                data = response.json()
                location = data['location']
                current = data['current']

                return (f"В {location['name']} сейчас {current['condition']['text'].lower()}. "
                       f"Температура: {current['temp_c']}°C. "
                       f"Влажность: {current['humidity']}%.")
            else:
                return "Не удалось получить данные о погоде"
        except:
            return "Ошибка подключения к сервису погоды"

    def open_app(self, app_name):
        """Open application"""
        app_name_lower = app_name.lower()

        for app_key, app_command in APPS.items():
            if app_name_lower in app_key:
                try:
                    if platform.system() == "Windows":
                        subprocess.Popen(app_command, shell=True)
                    else:
                        subprocess.Popen([app_command])
                    return f"Запускаю {app_key}"
                except:
                    return f"Не удалось запустить {app_key}"

        return "Приложение не найдено"

    def set_reminder(self, text, minutes):
        """Set reminder"""
        def reminder():
            time.sleep(minutes * 60)
            print(f"Напоминание: {text}")

        thread = threading.Thread(target=reminder)
        thread.daemon = True
        thread.start()
        self.reminders.append(thread)
        return f"Напоминание установлено: {text} через {minutes} минут"

    def play_music(self):
        """Open music service"""
        try:
            webbrowser.open("https://music.yandex.ru")
            return "Включаю музыку"
        except:
            return "Не удалось открыть музыку"

    def get_time(self):
        """Get current time"""
        now = datetime.now()
        return f"Сейчас {now.strftime('%H:%M')}"

    def get_date(self):
        """Get current date"""
        now = datetime.now()
        return f"Сегодня {now.strftime('%d.%m.%Y')}"

    def search_web(self, query):
        """Search web"""
        try:
            webbrowser.open(f"https://google.com/search?q={query}")
            return f"Ищу {query}"
        except:
            return "Не удалось выполнить поиск"

    def shutdown_pc(self):
        """Shutdown computer"""
        if platform.system() == "Windows":
            os.system("shutdown /s /t 60")
            return "Компьютер выключится через 1 минуту"
        return "Функция не поддерживается на этой ОС"

    def process(self, command):
        """Process user command"""
        command = command.lower()

        # Weather
        if any(word in command for word in ['погод', 'погоду', 'температур']):
            city = self.current_city
            if 'москв' in command:
                city = "Москва"
            elif 'питер' in command:
                city = "Санкт-Петербург"
            return self.get_weather(city)

        # Applications
        if any(word in command for word in ['открой', 'запусти']):
            for trigger in ['открой', 'запусти']:
                if trigger in command:
                    app_name = command.split(trigger, 1)[1].strip()
                    if app_name:
                        return self.open_app(app_name)

        # Time and date
        if any(word in command for word in ['время', 'час']):
            return self.get_time()
        if any(word in command for word in ['дата', 'число']):
            return self.get_date()

        # Music
        if any(word in command for word in ['музык', 'музыку']):
            return self.play_music()

        # Search
        if 'найди' in command:
            query = command.replace('найди', '').strip()
            if query:
                return self.search_web(query)

        # Reminders
        if 'напомни' in command and 'через' in command:
            try:
                parts = command.split('через')
                time_part = parts[1].split()[0]
                if time_part.isdigit():
                    text = command.split('напомни')[1].split('через')[0].strip()
                    return self.set_reminder(text, int(time_part))
            except:
                pass

        # System commands
        if 'выключи' in command and 'компьютер' in command:
            return self.shutdown_pc()

        # Greetings and thanks
        if any(word in command for word in ['привет', 'здравствуй']):
            return "Привет! Чем могу помочь?"
        if any(word in command for word in ['спасибо', 'благодар']):
            return "Всегда рад помочь!"

        # AI for unrecognized commands
        return self.ai.ask(command)