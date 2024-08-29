import requests

from core.settings import TG_KEY, MY_TG_KEY

bot_token = TG_KEY
my_bot_token = MY_TG_KEY

def send_mass_tg(text):

    message_text = (f'🟢 {text} 🟢')

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    chats = []
    chats.append(my_bot_token)

    for chat in chats:
        params = {
            'chat_id': chat,
            'text': message_text,
            'parse_mode': 'Markdown'
        }
        try:
           requests.post(url, json=params)
        except:
            pass