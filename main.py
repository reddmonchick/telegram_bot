import requests
import time
from dotenv import load_dotenv
import os


load_dotenv()

API_URL = 'https://api.telegram.org/bot'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
BOT_TOKEN = os.getenv('MY_TOKEN')
ERROR_TEXT = 'Нету котиков'
MAX_COUNTER = 10000

offset = -2
counter = 0
timeout = 60
chat_id: int

def do_something(res: dict) -> None:
    user = res.get('message').get('from').get('username')
    chat_id = res.get('message').get('from').get('id')
    message = res.get('message').get('text')
    if 'бля' in message:
        textik = f'Хеллоу, {user} твое последнее сообщение подозрительное! {message}'
    else:
        textik = f'Хеллоу, {user} твое последнее сообщение! {message}'
    requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={textik}')


while True:
    start_time = time.time()
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}&timeout={timeout}').json()

    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            do_something(result)

    end_time = time.time()
    print(f'Время между запросами к Telegram Bot API: {end_time - start_time}')