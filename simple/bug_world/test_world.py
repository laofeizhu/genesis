from world import World

import pytest

def test_create_bug():
  config = {
      'dim': [2, 3],
      'default_size': 5,
  }
  world = World(config)
  world.create_bug()
  assert len(world._bugs) == 1
  assert world._bugs[0].size == config['default_size']

def test_create_food():
  config = {
      'dim': [2, 3],
      'default_size': 10,
  }
  world = World(config)
  world.create_food(options={'point': [1, 1]})
  assert len(world._foods) == 1
  assert world._foods[0].size == 10
  assert world._foods[0].point == [1, 1]
