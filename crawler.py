template_map = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', 'E', ' ', 'D'],
    ['#', ' ', 'K', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

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
        pass

    new_row = player.row + MOVEMENTS[player_input][0]
    new_col = player.col + MOVEMENTS[player_input][1]

    if collision_check(level, new_row, new_col, player.key):
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

    elif tile == 'D' and player.key:
        print("Level complete!")
        level_complete = True

    elif tile == 'E':
        player.take_damage(1)
        if not player.is_alive():
            print('You died')
            player.health = 0
            level[player.row][player.col] = ' '

        else:
            print('Took damage from enemy')
            level[player.row][player.col] = ' '

    return level_complete

def display_info(health, has_key):
    print('W/A/S/D to move, Q to quit')
    print(f'Has Key: {has_key}')
    print(f'Health: {health}')


class Player:
    def __init__(self, row, col, health=10):
        self.row = row
        self.col = col
        self.key = False
        self.health = health
        self.symbol = 'P'

    def take_damage(self, amount):
        self.health -= amount

        if self.health < 0:
            self.health = 0

    def pick_up_key(self):
        self.key = True

    def is_alive(self):
        return self.health > 0

    def move_player(self, row, col):
        self.row = row
        self.col = col


player = Player(row=2, col=4, health=10)

while True:
    try:
        display_info(player.health, player.key)
        draw_map(template_map, player)
        next_input = input()
        if next_input.lower() == 'q':
            break
        update_position(template_map, player, next_input)
        level_complete = handle_tile_effect(template_map, player)
        if not player.is_alive() or level_complete:
            break


    except KeyboardInterrupt:
        quit()







