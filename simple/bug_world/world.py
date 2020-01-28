"""The world class. The world is a 2d plane in a donut shape. The world has food points in it. The food coordinates are always integers. Food has smells, which is inverse proportional to the distance, the distance at the food will be 1 to avoid dividing by 0. The smell is also proportional to the food quantity.

Distance is defined as the closest distance to the food.
"""

import numpy as np

from bug import Bug
from config import CONFIG
from food import Food
from geometry import Point, Vector
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits import mplot3d

class World(object):
  def __init__(self, config=CONFIG):
    self._foods = []
    self._bugs = []
    self._fields = {}
    self._config = config

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

  def create_bug(self, options={}):
    bug = Bug(point=self._point_or_random(options),
              size=self._size_or_default(options))
    self._bugs.append(bug)

  def create_food(self, options={}):
    food = Food(size=self._size_or_default(options),
                point=self._point_or_random(options))
    food.update_smell_field(self._config['dim'])
    self._foods.append(food)
    self._update_fields(food)

  def _update_fields(self, life):
    if not hasattr(life, 'fields'):
      return
    for key, value in life.fields.items():
      self._update_field(key, value)

  def _update_field(self, field_name, field_value):
    if not field_name in self._fields:
      self._fields[field_name] = np.zeros(self._config['dim'])
    self._fields[field_name] += field_value

  def show_field(self, field_name, block=True):
    fig = plt.figure()
    ax = plt.axes()
    X = np.arange(0,self._config['dim'][0],1)
    Y = np.arange(0,self._config['dim'][1],1)
    X, Y = np.meshgrid(X, Y)
    surf = ax.pcolormesh(X, Y, np.log(self._fields[field_name].T))
    fig.colorbar(surf)
    for bug in self._bugs:
      ax.plot(bug.point.x, bug.point.y, 'o', ms=10, color='r')
    plt.show(block=block)


# All objects is actually a field. The world is a superposition of fields.
class Field(object):
  def __init__(self):
    self.map = np.zeros((CONFIG.width, CONFIG.height))

  def get_smell(self, point):
    return self.map[point.x % CONFIG.width][point.y % CONFIG.height]
