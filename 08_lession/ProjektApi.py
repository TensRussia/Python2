import requests
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env файла
load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")
id = os.getenv("COMPANY_ID")
TOKEN = os.getenv("API_KEY")
HEADERS = {"Authorization": f"Bearer {TOKEN}"}


class ProjektApi:
    # Инициализация
    def __init__(self, url):
        self.url = url

# создать проект
    def post_projekt(self, payload=None):
        r = requests.post(self.url + '/projects',
                          json=payload, headers=HEADERS)
        return r.json()

# получить список проектов
    def get_projekt_list(self, id_neg=""):
        lis = requests.get(self.url + '/projects/' + id_neg, headers=HEADERS)
        return lis.status_code

# изменить проект
    def change_projekt(self, id=None, payload=None):
        c = requests.put(self.url + '/projects/' + id,
                         json=payload, headers=HEADERS)
        return c.status_code
