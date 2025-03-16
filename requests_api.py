import requests


class RequestsCollector:
    def __init__(self):
        self.url = r'https://olimp.miet.ru/ppo_it/api'

    def get_maps(self):
        maps = []
        while len(maps) != 16:
            data = requests.get(self.url).json()['message']['data']
            if data not in maps:
                maps.append(data)
        return maps

    def get_coords(self):
        return requests.get(self.url + '/coords').json()['message']


if __name__ == '__main__':
    rc = RequestsCollector()

    print(rc.get_maps())
