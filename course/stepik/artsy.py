import requests
import json

api_url_template = "https://api.artsy.net/api/artists/{}"
params = {
    'default': 'Boring',
    'json': 'true',
    'appid': '11c3d3c6093f7442898ee49d2430d20'

}

def get_artist(artist, headers2):
    # print('artist=', artist)
    # print('headers2', headers2)
    # инициируем запрос с заголовком
    r = requests.get(api_url_template.format(artist), headers=headers2)
    # разбираем ответ сервера
    j = json.loads(r.text)
    # print('full=',j)
    return j['sortable_name'],j['birthday']


client_id = '6a68dc7647f3ca8fc6bb'
client_secret = '3d870668f7a239c60fa93c4b2bf27025'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token": token}

a_lst = []  # Start with empty list
while True:
    a_str = input()
    if not a_str:  # Exit on empty string.
        break
    a_lst.append(a_str)
info = dict()
for i in a_lst:
    name, year = get_artist(i, headers)
    if name not in info.keys():
        info[name] = year
for j in info:
    print('key=', j, 'value=', info[j])

info_sort = sorted(info.items(), key=lambda x: (x[1],x[0]), reverse=False)
# print(info_sort)
# for i in range (0,len(info_sort)):
#     print(info_sort[i][0], info_sort[i][1])

for i in range(0, len(info_sort)):
    print(info_sort[i][0])
