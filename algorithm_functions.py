from vars import maps


def solve_algorithm(maps, coords):
    return {'maps': maps, 'coords': coords}


if __name__ == '__main__':
    solve_algorithm(
        maps,
        {'listener': [53, 202], 'price': [0.4, 0.6], 'sender': [199, 5]}
    )