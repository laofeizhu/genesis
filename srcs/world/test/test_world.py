import unittest

from utils.geometry import Point
from world.food import Food
from world.life import Bug
from world.world import Cell
from world.world import World


class TestWorld(unittest.TestCase):

  def test_cell(self):
    cell = Cell(0, 0)

  def test_create_world(self):
    world = World()

  def test_add_remove_life(self):
    world = World()
    point = Point(1, 2)
    bug = Bug(point=point)
    world.add_life(bug)
    self.assertEqual(len(world._life_cells), 1)
    bug_cell = world.get_cell(1, 2)
    self.assertTrue(bug_cell.id in world._life_cells)

    world.remove_life(life=bug)
    self.assertEqual(len(world._life_cells), 0)
    self.assertEqual(len(bug_cell.lives), 0)

  def test_add_remove_food(self):
    world = World()
    point = Point(1, 2)
    food = Food(point=point)
    world.add_food(food)
    self.assertEqual(len(world._food_cells), 1)
    food_cell = world.get_cell(1, 2)
    self.assertTrue(food_cell.id in world._food_cells)

    world.maybe_remove_food(food)
    self.assertEqual(len(world._food_cells), 1)

    food.size = 0
    world.maybe_remove_food(food)
    self.assertEqual(len(world._food_cells), 0)
    self.assertTrue(food_cell.food is None)

  def test_update(self):
    world = World()
    bug_point = Point(1, 2)
    food_point = Point(0, 0)
    bug = Bug(point=bug_point)
    food = Food(point=food_point)
    world.add_life(bug)
    world.add_food(food)
    world.update()

