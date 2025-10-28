"""Configuration settings for Orion Voice Assistant"""

import os

# API Keys
ZAI_API_KEY = os.getenv("ZAI_API_KEY", "b731340e2c344de6bebb959a08aa4b28.FogPhNvo65YP6Yq2")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "a470714feffa47eb849204509252710")

# Default settings
DEFAULT_CITY = "Москва"
VOICE_RATE = 150
VOICE_VOLUME = 0.9

# AI Model settings
AI_MODEL = "glm-5"
MAX_TOKENS = 300

# System prompts
SYSTEM_PROMPT = "Ты Орион - умный голосовой ассистент. Отвечай кратко и понятно на русском языке."

# Application commands
APPS = {
    'браузер': 'start chrome',
    'хром': 'start chrome',
    'калькулятор': 'start calc',
    'блокнот': 'start notepad',
    'проводник': 'start explorer',
    'файлы': 'start explorer',
    'код': 'start code',
    'стим': 'start steam',
    'дискорд': 'start discord',
    'телеграм': 'start telegram'
}