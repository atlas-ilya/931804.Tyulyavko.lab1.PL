import requests
import json

url = 'http://127.0.0.1:8080'
print(requests.get(url).text)
print(requests.get(url + '/Asia/Kamchatka').text)
print('ОШИБКА в строке! ' + requests.get(url + '/Asia/Kamchatka' + ' ').text)

data = {'type': 'time'}
print('Время без учета параметров: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'type': 'date'}
print('Дата без учета пааметров: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_start': 'Asia/Kamchatka', 'tz_end': 'Asia/Jerusalem', 'type': 'datediff'}
print('Разница во времени: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_start': 'Etc/GMT-4', 'tz_end': 'Etc/GMT+4', 'type': 'datediff'}
print('Разница в дате: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_end': 'Canada/Pacific', 'type': 'datediff'}
print('Отсутсвует начальный аргумент: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_start': 'Canada/Pacific', 'type': 'datediff'}
print('Отсутствует конечный аргумент: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'type': 'datediff'}
print('Отсутвуют начальный и конечный аргумент: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_start': 'Canada/Pacific', 'tz_end': 'Canada/Pacific'}
print('Отсутствует тип: ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_start': 'Canada/Pacificcccc', 'tz_end': 'Canada/Pacific', 'type': 'datediff'}
print('Синтаксическая ошибка в первом аргументе : ' + requests.post(url=url, data=json.dumps(data)).text)

data = {'tz_start': 'Canada/Pacific', 'tz_end': 'Canada/Pacificcccc', 'type': 'datediff'}
print('Синтаксическая ошибка во втором аргументе : ' + requests.post(url=url, data=json.dumps(data)).text)