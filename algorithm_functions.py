from vars import maps

def right(tile):
    return [x[-1] for x in tile]

def down(tile):
    return tile[-1]

def left(tile):
    return [x[0] for x in tile]

def up(tile):
    return tile[0]

def solve_algorithm(maps, coords):
    field = [[[[0 for _ in range(64)] * 64] for _ in range(4)] for _ in range(4)]
    for x in range(len(maps)):
        if maps[x][0][3] == 255 and maps[x][3][0] == 255:
            first = maps[x]
            first_index = x
        # if maps[0][60] == 255 and maps[3][63] == 255:
        #     field[3] = x
        #     field.remove(x)
        # if maps[63][3] == 255 and maps[60][0] == 255:
        #     field[12] = x
        #     field.remove(x)
        # if maps[60][63] == 255 and maps[63][60] == 255:
        #     field[15] = x
        #     field.remove(x)
    first_ends = (right(first), down(first), (0, 0), first_index)
    nodes = []
    for i in range(len(maps)):
        tile = maps[i]
        nodes.append((right(tile), down(tile), left(tile), up(tile), i))
    queue = [first_ends]
    while queue:
        last_right, last_down, last_coords, last_index = queue.pop(0)
        field[last_coords[1]][last_coords[0]] = maps[last_index]

        if not all(x == 255 for x in last_right):
            for n in nodes:
                node_right = n[0]
                node_down = n[1]
                node_left = n[2]
                node_up = n[3]
                node_index = n[4]
                if (all(abs(last_right[i] - node_left[i]) <= 20 for i in range(64))):
                    queue.append((node_right, node_down, (last_coords[0] + 1, last_coords[1]), node_index))
                    nodes.remove(n)
                    break
        if not all(x == 255 for x in last_down):
            for n in nodes:
                node_right = n[0]
                node_down = n[1]
                node_left = n[2]
                node_up = n[3]
                node_index = n[4]
                if all(abs(last_down[i] - node_up[i]) <= 20 for i in range(64)):
                    queue.append((n[0], n[1], (last_coords[0], last_coords[1] + 1), node_index))
                    nodes.remove(n)
                    break
    
    true_field = []

    for a in range(4):
        for line in range(0, 63, 16):
            for i in range(4):
                true_field += field[a][i][line:line+15]
    
    true_field = [x for xs in true_field for x in xs]

    
    return true_field
        
    
    
    


if __name__ == '__main__':
    solve_algorithm(
        maps,
        {'listener': [53, 202], 'price': [0.4, 0.6], 'sender': [199, 5]}
    )