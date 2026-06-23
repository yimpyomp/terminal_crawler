CONTROL_TEXT = "W/A/S/D to move"
GAMEPLAY_TEXT = "Q to quit, R to restart"
HEADER_HEIGHT = 4
MESSAGE_HEIGHT = 4
SIDEBAR_WIDTH = 28
CONTENT_START_COL = 2
HEADER_INFO_START_ROW = 1


def build_header_text(player, level_index):
    return f"Level {level_index + 1} | Has Key: {player.has_key} | Health: {player.health}"

def draw_map(screen, level, player, map_start_row, map_start_col):
    for row_number, row in enumerate(level):
        display_line = ''
        for col_number, tile in enumerate(row):
            if row_number == player.row and col_number == player.col:
                display_line += '@'
            else:
                display_line += tile
        screen.addstr(map_start_row + row_number, map_start_col, display_line)


def calculate_layout_positions(screen):
    height, width = screen.getmaxyx()
    usable_width = width - 1
    header_divider = HEADER_HEIGHT - 1
    message_divider = height - MESSAGE_HEIGHT
    sidebar_divider = usable_width - SIDEBAR_WIDTH
    map_start_row = header_divider + 1
    message_row = message_divider + 1
    sidebar_start_col = sidebar_divider + 2
    layout = {"height": height,
              "width": width,
              "usable_width": usable_width,
              "header_divider": header_divider,
              "message_divider": message_divider,
              "sidebar_divider": sidebar_divider,
              "map_start_row": map_start_row,
              "map_start_col": CONTENT_START_COL,
              "message_start_row": message_row,
              "message_start_col": CONTENT_START_COL,
              "sidebar_start_row": map_start_row,
              "sidebar_start_col": sidebar_start_col,
              "header_info_start_row": HEADER_INFO_START_ROW,
              "header_info_start_col": CONTENT_START_COL}
    return layout


def draw_header_info(screen, player, level_index, layout_positions):
    info_text = build_header_text(player, level_index)
    screen.addstr(layout_positions["header_info_start_row"], layout_positions["header_info_start_col"], info_text)


def draw_message(screen, message, layout_positions):
    screen.addstr(layout_positions["message_start_row"], layout_positions["message_start_col"], message)

def draw_screen(screen, level, level_index, player, message):
    screen.clear()
    layout_positions = calculate_layout_positions(screen)
    draw_layout(screen, layout_positions)
    draw_map(screen, level, player, layout_positions["map_start_row"], layout_positions["map_start_col"])
    draw_header_info(screen, player, level_index, layout_positions)
    draw_message(screen, message, layout_positions)
    draw_sidebar(screen, layout_positions)
    screen.refresh()


def draw_sidebar(screen, layout_positions):
    screen.addstr(layout_positions['sidebar_start_row'], layout_positions['sidebar_start_col'], CONTROL_TEXT)
    screen.addstr(layout_positions['sidebar_start_row'] + 1, layout_positions['sidebar_start_col'], GAMEPLAY_TEXT)


def build_horizontal_line(width):
    return '+' + '-' * (width - 2) + '+'


def draw_layout(screen, layout_positions):
    # Draw box overlay
    box_screen(screen, layout_positions)

    # Draw horizontal dividers
    screen.addstr(layout_positions["header_divider"], 0, build_horizontal_line(layout_positions["usable_width"]))
    screen.addstr(layout_positions["message_divider"], 0, build_horizontal_line(layout_positions["usable_width"]))

    # Draw vertical divider
    for row in range(HEADER_HEIGHT, layout_positions["message_divider"]):
        screen.addstr(row, layout_positions["sidebar_divider"], '|')

    # Add the corner pieces for the sidebar
    screen.addstr(layout_positions["header_divider"], layout_positions["sidebar_divider"], '+')
    screen.addstr(layout_positions["message_divider"], layout_positions["sidebar_divider"], '+')


def box_screen(screen, layout_positions):
    horizontal_border = '+' + '-' * (layout_positions["usable_width"] - 2) + '+'
    screen.addstr(0, 0, horizontal_border)

    side_border = '|' + ' ' * (layout_positions["usable_width"] - 2) + '|'
    for row in range(1, layout_positions["height"] - 1):
        screen.addstr(row, 0, side_border)

    screen.addstr(layout_positions["height"] - 1, 0, horizontal_border)
