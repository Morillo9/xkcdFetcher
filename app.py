import json, urllib
import os


for i in range(1, 1710):
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
