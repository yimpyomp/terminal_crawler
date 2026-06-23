import curses

from levels import LEVELS
from map_tools import update_position, handle_tile_effect, load_level, MOVEMENTS
from display_tools import draw_screen


def main(screen):
    curses.curs_set(0)
    level_index = 0
    level = LEVELS[level_index]
    level, player = load_level(level)
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

        if player_input == 'r':
            level, player = load_level(LEVELS[level_index])
            message = f"Restarted Level {level_index + 1}!"
            continue

        if player_input not in MOVEMENTS:
            message = "Invalid input!"
            continue

        message = update_position(level, player, player_input)
        level_complete, tile_message = handle_tile_effect(level, player)

        if tile_message != '':
            message = tile_message

        if not player.is_alive():
            message = "You Died! Press Q to Quit or R to Restart"
            continue

        if level_complete:
            level_index += 1

            if level_index >= len(LEVELS):
                message = "All levels complete!"
                draw_screen(screen, level, level_index - 1, player, message)
                screen.getch()
                break

            level, player = load_level(LEVELS[level_index])


if __name__ == "__main__":
    curses.wrapper(main)





