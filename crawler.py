import copy

from player import Player
from levels import LEVELS
from map_tools import display_info, draw_map, update_position, handle_tile_effect, find_start_tile, load_level

def main():
    level_index = 0
    level = copy.deepcopy(LEVELS[level_index])
    level, start_row, start_col = load_level(level)
    player = Player(row=start_row, col=start_col, health=10)

    while True:
        try:
            display_info(player)
            draw_map(level, player)
            next_input = input()

            if next_input.lower() == 'q':
                break

            update_position(level, player, next_input)
            level_complete = handle_tile_effect(level, player)

            if not player.is_alive():
                break

            if level_complete:
                level_index += 1

                if level_index >= len(LEVELS):
                    print("All levels complete!")
                    break

                level, start_row, start_col = load_level(level)
                player.move_player(row=start_row, col=start_col)
                player.has_key = False



        except KeyboardInterrupt:
            quit()


if __name__ == "__main__":
    main()

