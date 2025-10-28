"""AI module for Orion using Zhipu AI"""

from zai import ZaiClient
from .config import ZAI_API_KEY, AI_MODEL, MAX_TOKENS, SYSTEM_PROMPT


class AI:
    """AI assistant using Zhipu AI"""

    def __init__(self):
        self.client = ZaiClient(api_key=ZAI_API_KEY)

    def ask(self, question):
        """Get response from AI"""
        try:
            response = self.client.chat.completions.create(
                model=AI_MODEL,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": question}
                ],
                max_tokens=MAX_TOKENS
            )
            return response.choices[0].message.content
        except Exception:
            return "Ошибка подключения к AI"