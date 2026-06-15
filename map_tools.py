MOVEMENTS = {'w': (-1, 0),
             's': (1, 0),
             'a': (0, -1),
             'd': (0, 1)}

def in_bounds(level, row, col):
    return 0 <= row < len(level) and 0 <= col < len(level[row])


def collision_check(level, row, col, has_key):
    if not in_bounds(level, row, col):
        return False

    tile = level[row][col]

    if tile == '#':
        return False

    if tile == 'D' and not has_key:
        print("Key Required!")
        return False

    return True


def update_position(level, player, player_input):
    player_input = player_input.lower()
    if player_input not in MOVEMENTS:
        return

    row_change, col_change = MOVEMENTS[player_input]

    new_row = player.row + row_change
    new_col = player.col + col_change


    if collision_check(level, new_row, new_col, player.has_key):
        player.move_player(new_row, new_col)



def draw_map(level, player):
    for row_index, row in enumerate(level):
        display_row = ''

        for column_index, tile in enumerate(row):
            if (row_index == player.row) and (column_index == player.col):
                display_row += player.symbol
            else:
                display_row += tile
        print(display_row)



def handle_tile_effect(level, player):
    tile = level[player.row][player.col]
    level_complete = False

    if tile == 'K':
        print('Picked up the key')
        player.pick_up_key()
        level[player.row][player.col] = ' '

    elif tile == 'D' and player.has_key:
        print("Level complete!")
        level_complete = True

    elif tile == 'E':
        player.take_damage(1)
        level[player.row][player.col] = ' '

        if not player.is_alive():
            print('You died')

        else:
            print('Took damage from enemy')

    return level_complete

def display_info(player):
    print('W/A/S/D to move, Q to quit')
    print(f'Has Key: {player.has_key}')
    print(f'Health: {player.health}')
