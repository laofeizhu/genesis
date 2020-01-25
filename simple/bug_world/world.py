"""The world class. The world is a 2d plane in a donut shape. The world has food points in it. The food coordinates are always integers. Food has smells, which is inverse proportional to the distance, the distance at the food will be 1 to avoid dividing by 0. The smell is also proportional to the food quantity.

Distance is defined as the closest distance to the food.
"""

from mpl_toolkits import mplot3d

from bug import Bug
from config import CONFIG
from geometry import Point, Vector
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

class World(object):
  def __init__(self, config=CONFIG):
    self._foods = []
    self._bugs = []
    self._fields = {}
    self._config = config

  def _point_or_random(self, options):
    if 'point' in options:
      point = options['point']
    else:
      point = Point.random(self._config['dim'])
    return point

  def _size_or_default(self, options):
    if 'size' in options:
      size = options['size']
    else:
      size = self._config['default_size']
    return size

  def create_bug(self, options={}):
    bug = Bug(point=self._point_or_random(options),
              size=self._size_or_default(options))
    self._bugs.append(bug)

  def create_food(self, options={}):
    food = Food(size=self._size_or_default(options),
                point=self._point_or_random(options))
    self._foods.append(food)
    self._update_fields(food)

  def _update_fields(self, life):
    if not hasattr(life, 'fields'):
      return
    for key, value in life.fields:
      self._update_field(key, value)

  def _update_field(self, field_name, field_value):
    if not field_name in self.fields:
      self.fields['field_name'] = np.zeros(self._config.dim)
    self.fields['field_name'] += field_value

  def show(self, field_name):
    fig = plt.figure()
    ax = plt.axes()
    Y = np.arange(0,self._config.dim[0],1)
    X = np.arange(0,self._config.dim[1],1)
    X, Y = np.meshgrid(X, Y)
    surf = ax.pcolormesh(X, Y, np.log(self.fields['field_name']))
    fig.colorbar(surf)
    for bug in self._bugs:
      ax.plot(bug.pos.x, bug.pos.y, 'o', ms=10, color='r')
    plt.show()


class Food(object):

  def __init__(self, size=10, point=None):
    assert point != None
    self.point = point
    self.size = size

  def set_random_point(self):
    self.point = Point.random()

  # TODO: This should be inside World
  def update_smell_map(self):
    for x in range(CONFIG['width']):
      for y in range(CONFIG['height']):
        dist = self.point.distance_to(Point(x, y))  # optimize to use a cached map instead of creating the point each time.
        self.smells.map[x][y] = self.size / (dist + .1) / (dist + .1)  # plus .1 to avoid singularity.

# All objects is actually a field. The world is a superposition of fields.
class Field(object):
  def __init__(self):
    self.map = np.zeros((CONFIG.width, CONFIG.height))

  def get_smell(self, point):
    return self.map[point.x % CONFIG.width][point.y % CONFIG.height]
