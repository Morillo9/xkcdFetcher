import json, urllib
import os
import sys

def main():

    x = 0

    if not os.path.exists('comics'):
        os.makedirs('comics')

    cur_comic = 'http://xkcd.com/info.0.json'
    cur_url = urllib.urlopen(cur_comic)
    cur_data = json.loads(cur_url.read())
    cur_comic_ID = cur_data['num']

    user_input = raw_input("which comic do you want to download (all comics = all)\n")

    if user_input == 'all':
        x = 1
        y = cur_comic_ID

    else:
        try:
            x = int(user_input)
            y = int(user_input) + 1
        except ValueError:
            print("invalid input")
            sys.exit()

    for i in range(x, y):
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

if __name__ == '__main__':
    main()
