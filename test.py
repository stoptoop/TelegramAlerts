from pystyle import Colors, Colorate
from datetime import datetime
import requests
import time
import json


# # Load the JSON data from file
# with open('config.json', 'r') as file:
#     config = json.load(file)


# Page_Refresh_Rate = config['Page Refresh Rate']



def red(text):
    return Colorate.Horizontal(Colors.red_to_purple, f"{text}", 1)

def green(text):
    return Colorate.Horizontal(Colors.green_to_cyan, f"{text}", 1)


def now_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return (f"{current_time}")




import time
import requests

def now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")

def CheckAlert():
    AletKiev = False
    AletKievOblast = False

    while True:
        time.sleep(0.6)
        try:
            url = "https://ubilling.net.ua/aerialalerts/"
            response = requests.get(url)
            data = response.json()  # Парсинг JSON-ответа
            print(green(f"{now_time()} Успешно отправлен запрос!"))

            kiev_region = data["states"]["м. Київ"]["alertnow"]
            kievOblast_region = data["states"]["Київська область"]["alertnow"]
        except:
            print(red(f"{now_time()} Ошибка при отправке запроса на сайт!"))
            continue

        # Проверка состояния тревоги в Киеве
        if kiev_region == False:
            if AletKiev == True:  # Если до этого тревога была активна
                print(f"Отбой тревоги в Киеве в {now_time()}")
            AletKiev = False
        elif kiev_region == True:
            if AletKiev == False:  # Если до этого тревоги не было
                print(f"Тревога в Киеве началась в {now_time()}")
            AletKiev = True

        # Проверка состояния тревоги в Киевской области
        if kievOblast_region == False:
            if AletKievOblast == True:  # Если до этого тревога была активна
                print(f"Отбой тревоги в Киевской Области в {now_time()}")
            AletKievOblast = False
        elif kievOblast_region == True:
            if AletKievOblast == False:  # Если до этого тревоги не было
                print(f"Тревога в Киевской Области началась в {now_time()}")
            AletKievOblast = True

# Запуск функции
CheckAlert()
