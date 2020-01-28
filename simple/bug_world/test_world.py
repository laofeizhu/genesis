import pytest

from geometry import Point
from matplotlib import pyplot as plt
from world import World

def test_create_bug():
  config = {
      'dim': [2, 3],
      'default_bug_size': 5,
  }
  world = World(config)
  world.create_bug()
  assert len(world._bugs) == 1
  assert world._bugs[0].size == config['default_bug_size']

def test_create_food():
  config = {
      'dim': [2, 3],
      'default_bug_size': 10,
  }
  world = World(config)
  world.create_food(options={'point': [1, 1]})
  assert len(world._foods) == 1
  assert world._foods[0].size == 10
  assert world._foods[0].point == Point(1, 1, config['dim'])

def test_defaults():
  world = World()
  world.create_food()
  world.create_bug()
  assert len(world._foods) == 1
  assert len(world._bugs) == 1
  world.show_field('smell', block=False)
  plt.close('all')