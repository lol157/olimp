from colorama import Fore
from requests_api import RequestsCollector


def test(func, res_type, *args):
    try:
        if isinstance(func(*args), res_type):
            print(f'{Fore.GREEN}TEST SUCCESSFULLY COMPLETED')
        else:
            print(f'{Fore.RED}TEST FAILED')
    except:
        print(f'{Fore.RED}TEST FAILED')


rc = RequestsCollector()

test(rc.get_coords, list)
test(rc.get_maps, list)