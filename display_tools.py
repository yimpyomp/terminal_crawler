INFO_TEXT = "W/A/S/D to move, Q to quit || Level "
HEADER_HEIGHT = 4
MESSAGE_HEIGHT = 4
SIDEBAR_WIDTH = 28


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
    draw_layout(screen)
    draw_map(screen, level, player)
    display_info(screen, player, level, level_index, message)
    screen.refresh()


def build_horizontal_line(width):
    return '+' + '-' * (width - 2) + '+'


def draw_layout(screen):
    height, width = screen.getmaxyx()
    width -= 1

    # Draw box overlay
    box_screen(screen)

    # Define where additional borders will be
    header_divider = HEADER_HEIGHT - 1
    message_divider = height - MESSAGE_HEIGHT
    sidebar_divider = width - SIDEBAR_WIDTH

    # Draw horizontal dividers
    screen.addstr(header_divider, 0, build_horizontal_line(width))
    screen.addstr(message_divider, 0, build_horizontal_line(width))

    # Draw vertical divider
    for row in range(HEADER_HEIGHT, message_divider):
        screen.addstr(row, sidebar_divider, '|')

    # Add the corner pieces for the sidebar
    screen.addstr(header_divider, sidebar_divider, '+')
    screen.addstr(message_divider, sidebar_divider, '+')


def box_screen(screen):
    height, width = screen.getmaxyx()
    width -= 1

    horizontal_border = '+' + '-' * (width - 2) + '+'
    screen.addstr(0, 0, horizontal_border)

    side_border = '|' + ' ' * (width - 2) + '|'
    for row in range(1, height - 1):
        screen.addstr(row, 0, side_border)

    screen.addstr(height - 1, 0, horizontal_border)






