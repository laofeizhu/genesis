"""The world class. The world is a 2d plane in a donut shape. The world has food points in it. The food coordinates are always integers. Food has smells, which is inverse proportional to the distance, the distance at the food will be 1 to avoid dividing by 0. The smell is also proportional to the food quantity.

Distance is defined as the shortest path to the food.
"""

import numpy as np
import uuid

from bug import Bug
from config import CONFIG
from food import Food
from geometry import Point, Vector
from law import calculate_food_for_bugs
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d

class Cell(Point):
  def __init__(self, x, y):
    super(Cell, self).__init__(x, y)
    self.bugs = {}
    self.food = None
    self.id = uuid.uuid4()


class World(object):
  def __init__(self, config=CONFIG):
    self._foods = []
    self._bugs = {}
    self._fields = {}
    self._config = config
    self._cells = [[Cell(i, j) for i in range(self._config['dim'][1])] for j in range(self._config['dim'][0])]
    self._bug_cells = {}  # a dict from cell id to cell
    self._food_cells = {} # a dict from cell id to cell
    self._step_count = 0

  def step(self):
    """
    World evolves one step, will update bug and food.
    For all the bugs, update their size and check if new bug's created.
    For all the foods, update their size based on consumption.
    After food update, update fields.
    """
    self._step_count += 1
    # Bugs can eat or move in one step.
    # we need to know how many bugs are in one food grid. There's
    # a certain rule that how food are distributed among bugs.
    for _, bug in self._bugs.items():
      move = bug.maybe_move()
      self._handle_bug_move(move)
    # This will update food supplies field for bugs
    law.calculate_food_for_bugs(self)
    for _, bug in self._bugs.items():
      growth = bug.grow()
      self._handle_bug_growth(growth)

  def create_bug(self, options={}):
    bug = Bug(point=self._point_or_random(options),
              size=self._size_or_default(options))
    cell = self.get_cell(bug.point.x, bug.point.y)
    cell.bugs[bug.id] = bug
    self._bug_cells[cell.id] = cell
    self._bugs[bug.id] = bug
    self.update()
    return bug

  def create_food(self, options={}):
    food = Food(size=self._size_or_default(options),
                point=self._point_or_random(options))
    food.update_smell_field(self._config['dim'])
    cell = self.get_cell(food.point.x, food.point.y)
    cell.food = food
    self._food_cells[cell.id] = cell
    self._foods.append(food)
    self._update_fields(food)

  def update(self):
    """updates status"""
    self._clear_fields()
    for food in self._foods:
      self._update_fields(food)
    for _, bug in self._bugs.items():
      self._update_bug(bug)

  def show_field(self, field_name, block=True):
    self.update()
    fig = plt.figure()
    ax = plt.axes()
    X = np.arange(0,self._config['dim'][0],1)
    Y = np.arange(0,self._config['dim'][1],1)
    X, Y = np.meshgrid(X, Y)
    surf = ax.pcolormesh(X, Y, np.log(self._fields[field_name].T))
    fig.colorbar(surf)
    for _, bug in self._bugs.items():
      ax.plot(bug.point.x, bug.point.y, 'o', ms=10, color='r')
    plt.show(block=block)

  def _handle_bug_growth(self, growth):
    # check if bug is dead and remove it if so.

  def _handle_bug_move(self, move):
    """
    update world state for a bug move
    """
    if move is None:
      return
    from_point = move["from"]
    to_point = move["to"]
    from_cell = self.get_cell(from_point.x, from_point.y)
    to_cell = self.get_cell(to_point.x, to_point.y)
    bug = move["bug"]
    del from_cell.bugs[bug.id]
    if len(from_cell.bugs) == 0:
      del self._bug_cells[from_cell.id]
    to_cell.bugs[bug.id] = bug
    if len(to_cell.bugs) == 1:
      self._bug_cells[to_cell.id] = to_cell
    self._update_bug(bug)

  def _update_bug(self, bug):
    for idx, d in enumerate(bug.get_dirs()):
      p = bug.point.add(d)
      bug.set_vision(idx, self._get_field(p, 'smell'))
    bug.is_on_food = self.get_cell(bug.point.x, bug.point.y).food is not None

  def _update_fields(self, life):
    if not hasattr(life, 'fields'):
      return
    for key, value in life.fields.items():
      self._update_field(key, value)

  def _update_field(self, field_name, field_value):
    if not field_name in self._fields:
      self._fields[field_name] = np.zeros(self._config['dim'])
    self._fields[field_name] += field_value

  def _clear_fields(self):
    self._fields = {}

  def _get_field(self, point, field_name='smell'):
    if not field_name in self._fields:
      return 0
    return self._fields[field_name][point.x][point.y]

  def get_cell(self, x, y):
    # TODO: raise exception if out of range.
    return self._cells[x][y]

  def _point_or_random(self, options):
    if 'point' in options:
      point = Point(options['point'][0], options['point'][1], self._config['dim'])
    else:
      point = Point.random(self._config['dim'])
    return point

  def _size_or_default(self, options):
    if 'size' in options:
      size = options['size']
    else:
      size = self._config['default_bug_size']
    return size
