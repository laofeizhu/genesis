"""The world class. The world is a 2d plane in a donut shape. The world has food points in it. The food coordinates are always integers. Food has smells, which is inverse proportional to the distance, the distance at the food will be 1 to avoid dividing by 0. The smell is also proportional to the food quantity.

Distance is defined as the closest distance to the food.
"""

from mpl_toolkits import mplot3d

from config import CONFIG
from geometry import Point, Vector
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import cm

class World(object):

  def __init__(self):
    self._foods = []
    self._bugs = []
    self._smells = np.zeros((CONFIG['width'], CONFIG['height']))

  def place_bug(self, bug):
    self._bugs.append(bug)

  def place_food(self, food):
    self._foods.append(food)
    self.update_smells(food)

  def update():
    pass

  def update_smells(self, food):
    # TODO: use a function to avoid repetetion of the map iteration.
    for x in range(CONFIG['width']):
      for y in range(CONFIG['height']):
        self._smells[x][y] += food.smell_map[x][y]

  def show(self):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    Y = np.arange(0,CONFIG['width'],1)
    X = np.arange(0,CONFIG['height'],1)
    X, Y = np.meshgrid(X, Y)
    surf = ax.plot_surface(X, Y, np.log(self._smells), cmap=cm.coolwarm, antialiased=False)
    fig.colorbar(surf)
    plt.show()




class Food(object):

  def __init__(self, size=10, point=None):
    if point == None:
      self.set_random_point()
    else:
      self.point = point
    self.size = size
    self.smell_map = np.zeros((CONFIG['width'], CONFIG['height']))
    self.update_smell_map()

  def set_random_point(self):
    self.point = Point.random()

  def update_smell_map(self):
    for x in range(CONFIG['width']):
      for y in range(CONFIG['height']):
        dist = self.point.distance_to(Point(x, y))  # optimize to use a cached map instead of creating the point each time.
        self.smell_map[x][y] = self.size / (dist + .1) / (dist + .1)  # plus .1 to avoid singularity.


