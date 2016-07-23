import json, urllib
import os

cur_comic = 'http://xkcd.com/info.0.json'
cur_url = urllib.urlopen(cur_comic)
cur_data = json.loads(cur_url.read())
cur_comic_ID = cur_data['num']

if not os.path.exists('comics'):
    os.makedirs('comics')

for i in range(1, cur_comic_ID):
    try:
        url = "http://xkcd.com/" + str(i) +"/info.0.json"
        response = urllib.urlopen(url)
        data = json.loads(response.read())
        comic = data['img']

        comic_name = "./comics/Comic" + str(i)+".jpg"

        urllib.urlretrieve(comic, comic_name)

        print("Comic " + str(i) + " fetched")

    except Exception:
        print("Faulty Link")
