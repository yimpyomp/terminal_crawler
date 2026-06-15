import copy

from player import Player
from levels import LEVELS
from map_tools import display_info, draw_map, update_position, handle_tile_effect

def main():
    player = Player(row=2, col=4, health=10)
    level_index = 0
    level = copy.deepcopy(LEVELS[level_index])

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

                level = copy.deepcopy(LEVELS[level_index])
                player.move_player(row=2, col=2)
                player.has_key = False



        except KeyboardInterrupt:
            quit()


if __name__ == "__main__":
    main()

