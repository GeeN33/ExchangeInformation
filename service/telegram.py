import requests

from core.settings import TG_KEY, MY_TG_ID

bot_token = TG_KEY
my_chat_id = MY_TG_ID

def send_mass_tg(text):

    message_text = (f'🟢 {text} 🟢')

    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

    chats = []
    chats.append(my_chat_id)

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