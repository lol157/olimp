from colorama import Fore


def test(func, res_type, *args):
    try:
        if isinstance(func(*args), res_type):
            print(f'{Fore.GREEN}TEST SUCCESSFULLY COMPLETED')
        else:
            print(f'{Fore.RED}TEST FAILED')
    except:
        print(f'{Fore.RED}TEST FAILED')