from config import CONFIG

import numpy as np

class Point(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @classmethod
  def random(cls):
    return Point(np.random.randint(low=0, high=CONFIG['width']-1),
                 np.random.randint(low=0, high=CONFIG['height']-1))

  def distance_to(self, p):
    v = Vector.from_points(self, p)
    return v.length()


class Vector(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @classmethod
  def from_points(cls, p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    # using modulo will be simpler
    dx = dx if np.absolute(dx) < CONFIG['width'] / 2 else p2.x - np.sign(dx) * CONFIG['width'] - p1.x
    dy = dy if np.absolute(dy) < CONFIG['height'] / 2 else p2.y - np.sign(dy) * CONFIG['height'] - p1.y
    return Vector(dx, dy)

  def length(self):
    return np.sqrt(self.x * self.x + self.y * self.y)
