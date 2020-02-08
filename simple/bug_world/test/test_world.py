import unittest

from geometry import Point
from matplotlib import pyplot as plt
from world import World

class TestWorld(unittest.TestCase):
  def test_create_bug(self):
    config = {
        'dim': [2, 3],
        'default_bug_size': 5,
    }
    world = World(config)
    world.create_bug()
    world.update()
    self.assertEqual(len(world._bugs), 1)
    self.assertEqual(world._bugs[0].size, config['default_bug_size'])

  def test_create_food(self):
    config = {
        'dim': [2, 3],
        'default_bug_size': 10,
    }
    world = World(config)
    world.create_food(options={'point': [1, 1]})
    world.update()
    self.assertEqual(len(world._foods), 1)
    self.assertEqual(world._foods[0].size, 10)
    self.assertEqual(world._foods[0].point, Point(1, 1, config['dim']))

  def test_defaults(self):
    world = World()
    world.create_food()
    world.create_bug()
    world.update()
    self.assertEqual(len(world._foods), 1)
    self.assertEqual(len(world._bugs), 1)
    world.show_field('smell', block=False)
    plt.close('all')

  def test_update(self):
    config = {
        'dim': [2, 3],
        'default_bug_size': 10,
    }
    world = World(config)
    world.create_food(options={'point': [1, 1]})
    world.create_bug(options={'point': [1, 1]})
    world.update()
    self.assertEqual( world._bugs[0].smells.size, 8)
    self.assertTrue( world._bugs[0].smells[0] > 0)
    self.assertTrue( world._bugs[0].is_on_food)
