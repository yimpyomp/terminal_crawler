template_map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', 'P', ' ', ' ', ' ', ' ', 'D'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]
# Bounds are 1-8 horizontally (columns), 1-3 vertically (rows)

player_row = 2
player_column = 4

game_running = True

# Function to check if new position is within bounds
def collision_check(level, col, row):
    return level[row][col] != '#'

def update_position(level, col, row, player_input):
    player_input = player_input.lower()
    if player_input == 'a':
        new_column = col - 1
        new_row = row
    elif player_input == 'd':
        new_column = col + 1
        new_row = row
    elif player_input == 'w':
        new_column = col
        new_row = row - 1
    elif player_input == 's':
        new_column = col
        new_row = row + 1
    else:
        new_column = col
        new_row = row

    if collision_check(level, new_column, new_row):
        return new_column, new_row
    else:
        return col, row

def update_map(level, col, row):
    try:
        for current_row in level:
            if 'P' in current_row:
                old_col = current_row.index('P')
                current_row[old_col] = ' '
    except ValueError:
        pass
    level[row][col] = 'P'
    return level

def draw_map(level):
    for row in level:
        print(''.join(row))
    return None

def check_level_completion(level, row, col):
    if level[row][col] == 'D':
        print('Level complete!')
    game_running = False



while game_running:
    try:
        draw_map(template_map)
        next_input = input()
        player_column, player_row = update_position(template_map, player_column, player_row, next_input)
        check_level_completion(template_map, player_row, player_column)
        template_map = update_map(template_map, player_column, player_row)

    except KeyboardInterrupt:
        quit()







