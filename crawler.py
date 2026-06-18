import copy
import curses

from player import Player
from levels import LEVELS
from map_tools import update_position, handle_tile_effect, load_level, MOVEMENTS
from display_tools import draw_screen


def main(screen):
    curses.curs_set(0)
    level_index = 0
    level = copy.deepcopy(LEVELS[level_index])
    level, start_row, start_col = load_level(level)
    player = Player(row=start_row, col=start_col, health=10)
    message = ''

    while True:
        draw_screen(screen, level, level_index, player, message)

        key = screen.getch()

        try:
            player_input = chr(key).lower()

        except ValueError:
            message = "Invalid input"
            continue

        if player_input == 'q':
            break

        if player_input not in MOVEMENTS:
            message = "Invalid input"
            continue

        update_position(level, player, player_input)
        level_complete, message = handle_tile_effect(level, player)

        if not player.is_alive():
            break

        if level_complete:
            level_index += 1

            if level_index >= len(LEVELS):
                message = "All levels complete!"
                draw_screen(screen, level, level_index, player, message)
                screen.getch()
                break

            level, start_row, start_col = load_level(LEVELS[level_index])
            player.move_player(row=start_row, col=start_col)
            player.has_key = False


if __name__ == "__main__":
    curses.wrapper(main)





