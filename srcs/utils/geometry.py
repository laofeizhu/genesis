import numpy as np

from config import CONFIG

DEFAULT_DIM = CONFIG["dim"]

class Point(object):

  def __init__(self, p, dim=DEFAULT_DIM):
    """
    Point should always be created from world since the dimension
    is an attribute of the world.
    """
    self.x = x
    self.y = y
    self.dim = dim

  @classmethod
  def random(cls, dim=DEFAULT_DIM):
    return Point(np.random.randint(low=0, high=dim[0]-1),
                 np.random.randint(low=0, high=dim[1]-1),
                 dim=dim)

  def distance_to(self, p, dist_type='eculid'):
    v = Vector.from_points(self, p)
    return v.length(dist_type=dist_type)

  def add(self, v):
    return Point((self.x + v.x) % self.dim[0], (self.y + v.y) % self.dim[1], self.dim)

  def __eq__(self, other):
    if self is None or other is None:
      return True if self is None and other is None else False
    return self.x == other.x and self.y == other.y and self.dim == other.dim

  def __str__(self):
    d = {
      'x': self.x,
      'y': self.y,
      'dim': self.dim
    }
    return str(d)

class Vector(object):

  def __init__(self, x, y):
    self.x = x
    self.y = y

  @classmethod
  def from_points(cls, p1, p2):
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    width, height = p1.dim
    # using modulo will be simpler
    dx = dx if np.absolute(dx) < width / 2 else p2.x - np.sign(dx) * width - p1.x
    dy = dy if np.absolute(dy) < height / 2 else p2.y - np.sign(dy) * height - p1.y
    return Vector(dx, dy)

  def length(self, dist_type='eculid'):
    if dist_type == 'eculid':
      return np.sqrt(self.x * self.x + self.y * self.y)
    elif dist_type == 'rect':
      return np.absolute(self.x) + np.absolute(self.y)
