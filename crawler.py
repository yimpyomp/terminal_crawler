template_map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', 'D'],
    ['#', ' ', 'K', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

movements = {'w': (-1, 0),
             's': (1, 0),
             'a': (0, -1),
             'd': (0, 1)}

# Bounds are 1-8 horizontally (columns), 1-3 vertically (rows)

#change this
# Function to check if new position is within bounds
def collision_check(level, row, col, has_key):
    tile = level[row][col]

    if tile == '#':
        return False

    if tile == 'D' and not has_key:
        print("Key Required!")
        return False

    return True


def update_position(level, row, col, player_input, has_key):
    player_input = player_input.lower()

    new_row = row + movements[player_input][0]
    new_column = col + movements[player_input][1]

    try:
        if collision_check(level, new_row, new_column, has_key):
            return new_row, new_column
        else:
            return row, col
    except IndexError:
        return row, col


def draw_map(level, player_row, player_col):
    for row_index, row in enumerate(level):
        display_row = ''

        for column_index, tile in enumerate(row):
            if (row_index == player_row) and (column_index == player_col):
                display_row += 'P'
            else:
                display_row += tile
        print(display_row)



def handle_tile_effect(level, row, col, has_key, health):
    tile = level[row][col]
    level_complete = False

    if tile == 'K':
        print('Picked up the key')
        has_key = True
        level[row][col] = ' '

    elif tile == 'D' and has_key:
        print("Level complete!")
        level_complete = True

    elif tile == 'E':
        health -= 1
        if health <= 0:
            print('You died')
            health = 0
            level[row][col] = ' '
            return has_key, health, level_complete
        else:
            print('Took damage from enemy')
            level[row][col] = ' '

    return has_key, health, level_complete

def display_info(health, has_key):
    print('W/A/S/D to move, Q to quit')
    print(f'Has Key: {has_key}')
    print(f'Health: {health}')
    return None


# Basic debug initializations
player_row = 2
player_column = 4
player_key = False
player_health = 10



while True:
    try:
        display_info(player_health, player_key)
        draw_map(template_map, player_row, player_column)
        next_input = input()
        if next_input.lower() == 'q':
            break
        player_row, player_column= update_position(template_map, player_row, player_column, next_input, player_key)
        player_key, player_health, level_complete = handle_tile_effect(template_map, player_row, player_column, player_key, player_health)
        if player_health <= 0 or level_complete:
            break


    except KeyboardInterrupt:
        quit()







