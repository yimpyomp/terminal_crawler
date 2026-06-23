from player import Player

MOVEMENTS = {'w': (-1, 0),
             's': (1, 0),
             'a': (0, -1),
             'd': (0, 1)}

def in_bounds(level, row, col):
    return 0 <= row < len(level) and 0 <= col < len(level[row])


def is_door_tile(level, row, col):
    return level[row][col] == 'D'

def collision_check(level, row, col, has_key):
    if not in_bounds(level, row, col):
        return False

    tile = level[row][col]

    if tile == '#':
        return False

    if tile == 'D' and not has_key:
        return False

    return True


def update_position(level, player, player_input):
    row_change, col_change = MOVEMENTS[player_input]

    new_row = player.row + row_change
    new_col = player.col + col_change
    message = ''

    if collision_check(level, new_row, new_col, player.has_key):
        player.move_player(new_row, new_col)

    else:
        if is_door_tile(level, new_row, new_col) and in_bounds(level, new_row, new_col):
            message = "Key required!"

    return message




def handle_tile_effect(level, player):
    tile = level[player.row][player.col]
    level_complete = False
    message = ''

    if tile == 'K':
        message = "Picked up the key!"
        player.pick_up_key()
        level[player.row][player.col] = ' '

    elif tile == 'D' and player.has_key:
        level[player.row][player.col] = ' '
        message = "Unlocked the door!"

    elif tile == 'X':
        message = "Level Complete!"
        level_complete = True

    elif tile == '^':
        player.take_damage(1)
        message = "Took damage from trap!"

    elif tile == 'E':
        player.take_damage(1)
        level[player.row][player.col] = ' '
        message = "Took damage from enemy!"

    elif tile == "+":
        player.heal()
        level[player.row][player.col] = ' '
        message = "Picked up the health pack!"

    return level_complete, message


def find_start_tile(level):
    for row_number, row in enumerate(level):
        for col_number, col in enumerate(row):
            if col == 'S':
                start_row, start_col = row_number, col_number
                level[row_number][col_number] = ' '
                return start_row, start_col

    raise ValueError("No starting position found!")


def load_level(level_template):
    level = [list(row) for row in level_template]
    start_row, start_col = find_start_tile(level)
    player = Player(row=start_row, col=start_col, health=10)
    return level, player
