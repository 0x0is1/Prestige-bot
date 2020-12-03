import requests
import random
from bs4 import BeautifulSoup as scrapper
import time
import os

choice_container = {'very-short-quotes/': 35, 'life-is-short-be-happy-quotes/': 31, 'funny-inspirational-quotes-about-life/': 71, 'gratitude-quotes/': 73, 'short-happy-quotes/': 71, 'short-quotes-about-love/': 24}
def random_quotes_generator(random_choice):
    cur_choice = list(choice_container.keys())[random_choice]
    quote_count_choice = random.randint(0, choice_container[cur_choice])
    print(cur_choice, quote_count_choice)
    url = 'https://thegoalchaser.com/' + cur_choice
    response = requests.get(url)
    soup = scrapper(response.content, 'html.parser')
    try:
        data = soup.find_all('em')[quote_count_choice]
    except Exception:
        data = soup.find_all(
            'p', {'style': 'text-align: center;'})[quote_count_choice]
    return data.text.split('”')[0] + '”'


url = 'https://discord.com/api/v8/users/@me/settings'
status = 'test 5'
headers = {
    'Host': 'discord.com',
    'User-Agent': 'Mozilla/5.0 (X11 Linux x86_64 rv: 75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json',
    'Authorization': os.environ.get('USER_TOKEN'),
    'Origin': 'https://discord.com',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'TE': 'Trailers'
}
cookies = {
    '_ga': 'GA1.2.735792174.1600309507',
    '__cfduid': 'dbeed583f239f1c25f3526680d7a200f71605977430',
    'locale': 'en-US'
}

while True:
    try:
        status = random_quotes_generator(random.randint(0, 5))
        if len(status) < 10:
            continue
        else:
            data = '{"custom_status":{"text":"' + status + '"}}'
            response = requests.patch(
                url, headers=headers, cookies=cookies, data=data.encode('utf-8'))
            #print(response.status_code)
    except Exception:
        pass
    time.sleep(120)
