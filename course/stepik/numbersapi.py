import requests


api_url_template = "http://numbersapi.com/{}/math"
params = {
    'default' : 'Boring',
    'json' : 'true',
    'appid' : '11c3d3c6093f7442898ee49d2430d20'

}

def interesting(n):
    res = requests.get(api_url_template.format(n),params=params)
    data = res.json()
    if data["text"] != 'Boring':
        print('Interesting')
    else:
        print('Boring')

a_lst = []          # Start with empty list
while True:
    a_str = input()
    if not a_str:   # Exit on empty string.
        break
    a_lst.append(a_str)
# print(a_lst)
for i in a_lst:
    interesting(i)