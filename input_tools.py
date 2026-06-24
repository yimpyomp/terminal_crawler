import curses


def get_player_input(screen):
    key = screen.getch()
    message = ''

    try:
        player_input = chr(key).lower()

    except ValueError:
        message = "Invalid input!"

    return
