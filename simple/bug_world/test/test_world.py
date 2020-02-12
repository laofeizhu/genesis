import unittest

from geometry import Point
from matplotlib import pyplot as plt
from world import World

class TestWorld(unittest.TestCase):
  def test_create_bug(self):
    config = {
        'dim': [2, 3],
        'default_bug_size': 5,
        "default_food_size": 5,
    }
    world = World(config)
    bug = world.create_bug()
    self.assertEqual(len(world._bugs), 1)
    self.assertEqual(world._bugs[bug.id]._size, config['default_bug_size'])
    bug_cell = world.get_cell(bug.point.x, bug.point.y)
    self.assertEqual(len(bug_cell.bugs), 1)
    self.assertTrue(bug.id in bug_cell.bugs)
    self.assertEqual(len(world._bug_cells), 1)

  def test_create_food(self):
    config = {
        'dim': [2, 3],
        'default_bug_size': 10,
        "default_food_size": 5,
    }
    world = World(config)
    food = world.create_food(options={'point': [1, 1]})
    self.assertEqual(len(world._foods), 1)
    self.assertEqual(world._foods[food.id].size, 5)
    self.assertEqual(world._foods[food.id].point, Point(1, 1, config['dim']))
    self.assertEqual(food, world._foods[food.id])
    food_cell = world.get_cell(food.point.x, food.point.y)
    self.assertIsNotNone(food_cell.food)
    self.assertEqual(len(world._food_cells), 1)

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
        "default_food_size": 5,
    }
    world = World(config)
    world.create_food(options={'point': [1, 1]})
    bug = world.create_bug(options={'point': [1, 1]})
    self.assertEqual(len(world._bugs[bug.id]._vision), 8)
    self.assertTrue(world._bugs[bug.id]._vision[0] > 0)
    self.assertTrue(world._bugs[bug.id].is_on_food)

  def test_bug_move(self):
    config = {
        'dim': [20, 1],
        'default_bug_size': 10,
        "default_food_size": 5,
    }
    world = World(config)
    world.create_food(options={'point': [0, 0]})
    bug_not_on_food_1 = world.create_bug(options={'point': [5, 0]})
    bug_not_on_food_2 = world.create_bug(options={'point': [15, 0]})
    bug_on_food = world.create_bug(options={'point': [0, 0]})
    world.step()
    self.assertEqual(world._step_count, 1)
    self.assertEqual(bug_not_on_food_1.point.x, 4)
    self.assertEqual(bug_not_on_food_2.point.x, 16)
    self.assertEqual(bug_on_food.point.x, 0)

  def test_bug_grow_bigger(self):
    config = {
        'dim': [20, 1],
        'default_bug_size': 1,
        "default_food_size": 5,
    }
    world = World(config)
    world.create_food(options={'point': [0, 0]})
    bug = world.create_bug(options={'point': [0, 0]})
    size_before = bug._size
    world.step()
    size_after = bug._size
    self.assertTrue(size_after > size_before)

  def test_bug_grow_smaller(self):
    config = {
        'dim': [20, 1],
        'default_bug_size': 5,
        "default_food_size": 1,
    }
    world = World(config)
    world.create_food(options={'point': [0, 0]})
    bug = world.create_bug(options={'point': [0, 0]})
    size_before = bug._size
    world.step()
    size_after = bug._size
    self.assertTrue(size_after < size_before)

  def test_bug_starve_to_death(self):
    config = {
        'dim': [20, 1],
        'default_bug_size': 5,
        "default_food_size": 1,
    }
    world = World(config)
    bug = world.create_bug(options={'point': [0, 0]})
    for _ in range(10):
      world.step()
    self.assertEqual(len(world._bugs), 0)
    self.assertEqual(len(world._bug_cells), 0)

  def test_bug_eat_up_food(self):
    config = {
        'dim': [20, 1],
        'default_bug_size': 5,
        "default_food_size": 1,
    }
    world = World(config)
    world.create_food(options={'point': [0, 0]})
    bug = world.create_bug(options={'point': [0, 0]})
    self.assertEqual(len(world._foods), 1)
    self.assertEqual(len(world._food_cells), 1)
    for _ in range(10):
      world.step()
    self.assertEqual(len(world._foods), 0)
    self.assertEqual(len(world._food_cells), 0)

