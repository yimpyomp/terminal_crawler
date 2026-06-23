from map_tools import (
    in_bounds,
    collision_check,
    update_position,
    handle_tile_effect,
    find_start_tile,
    load_level
)

from player import Player
import pytest

test_level = [
    list("#####"),
    list("#S K#"),
    list("# D #"),
    list("# X #"),
    list("#####"),
]

# in_bounds tests
def test_in_bound_result():
    assert in_bounds(test_level, 2, 2) is True

def test_out_of_bounds_result():
    assert in_bounds(test_level, 5, 5) is False

# collision_check tests
def test_collision_check():
    assert collision_check(test_level, 0, 1, False) is False

def test_door_behavior_with_key():
    assert collision_check(test_level, 2, 2, True) is True

def test_door_behavior_without_key():
    assert collision_check(test_level, 2, 2, False) is False

def test_allows_empty_space():
    assert collision_check(test_level, 1, 2, False) is True

# update_position tests
def test_move_to_open_space():
    player = Player(2, 3)
    assert update_position(test_level, player, 's') == ''
    assert player.row == 3
    assert player.col == 3

def test_move_to_locked_door():
    player = Player(1, 2)
    assert update_position(test_level, player, 's') == 'Key required!'
    assert player.row == 1
    assert player.col == 2







