import requests
import json
import threading
import os

letters = [chr(i) for i in range(65, 65 + 26)]
combinations = set()

for i in letters:
    for j in letters:
        for k in letters:
            combinations.add(f'{i}{j}{k}')

combinations = sorted(combinations)

curl = 'https://matrix.itasoftware.com/geosearch'

h = {
    'authority': 'matrix.itasoftware.com',
    'x-gwt-module-base': 'https://matrix.itasoftware.com/gwt/',
    'x-gwt-permutation': '40C0A8F41CAEE2C1259EA9CBCE6840B0',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'content-type': 'application/javascript; charset=UTF-8',
    'accept': '*/*',
    'origin': 'https://matrix.itasoftware.com',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://matrix.itasoftware.com/',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
}

failed = []


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


def download(c):
    data = {
        "method": "suggest",
        "params": {
            "1": c,
            "2": 4
        }
    }
    try:
        response = requests.post(url=curl, headers=h, json=data)
        out = response.json()
        with open(f'output/{c}.json', 'w') as f:
            f.write(json.dumps(out, indent=2))
        print(c)
    except Exception as err:
        failed.append(c)
        print(f'{c}: {type(err)}')


for chunk in divide_chunks(combinations, 16):
    ths = list()
    for c in chunk:
        if not os.path.exists(f'output/{c}.json'):
            th = threading.Thread(target=download, args=(c,))
            ths.append(th)
            th.start()

    for th in ths:
        th.join()
