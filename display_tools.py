INFO_TEXT = "W/A/S/D to move, Q to quit || Level "

def draw_map(screen, level, player):
    for row_number, row in enumerate(level):
        display_line = ''
        for col_number, tile in enumerate(row):
            if row_number == player.row and col_number == player.col:
                display_line += '@'
            else:
                display_line += tile
        screen.addstr(row_number, 0, display_line)


def display_info(screen, player, level, level_index, message):
    info_display_row = len(level) + 1
    player_display_row = info_display_row + 1
    screen.addstr(info_display_row, 0 ,INFO_TEXT + str(level_index + 1))
    screen.addstr(player_display_row, 0, f"Has Key: {player.has_key} | Health: {player.health}")
    screen.addstr(player_display_row + 1, 0, message)


def draw_screen(screen, level, level_index, player, message):
    screen.clear()
    draw_map(screen, level, player)
    display_info(screen, player, level, level_index, message)
    screen.refresh()




