def draw_map(screen, level, player):
    for row_number, row in enumerate(level):
        display_line = ''
        for col_number, tile in enumerate(row):
            if row_number == player.col and col_number == player.col:
                display_line += '@'
            else:
                display_line += tile
        screen.addstr(display_line)


def draw_screen(screen, level, player, info_line, message):
    screen.clear()
    info_display_row = len(level) + 1
    screen.addstr(info_display_row, 0, info_line)
    screen.addstr(info_display_row + 1, 0, message)
    draw_map(screen, level, player)
    screen.refresh()



