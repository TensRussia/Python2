from ProjektApi import ProjektApi
from dotenv import load_dotenv


# Загрузка переменных окружения из .env файла
load_dotenv()

Api = ProjektApi("https://ru.yougile.com/api-v2")
ID_POZ = None


# создать проект автотест
def test_create_project_post():
    body = Api.post_projekt(payload={"title": "autotest"})
    global ID_POZ
    ID_POZ = body.get('id')
    assert body["id"]


# создать проект - негатив
def test_create_project_post_negativ():
    body = Api.post_projekt(payload={"title": ""})
    assert body["error"] == 'Bad Request'


# получить список проектов автотест
def test_get_list_projekts():
    stat_code = Api.get_projekt_list()
    assert stat_code == 200


# получить проект по ID негативный автотест
def test_get_by_ID_negativ():
    stat_code = Api.get_projekt_list(id_neg="2343")
    assert stat_code == 404


# изменить проект по ID автотест
def test_change_project():
    stat_code = Api.change_projekt(id=ID_POZ, payload={"title": "mototest"})
    assert stat_code == 200


# изменить проект по ID негативный автотест
def test_change_projekt_negativ():
    stat_code = Api.change_projekt(id="", payload={"title": "mototest"})
    assert stat_code == 404
