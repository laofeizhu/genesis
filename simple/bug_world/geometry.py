import numpy as np

class Point(object):

  def __init__(self, x, y, dim=None):
    """
    Point should always be created from world since the dimension
    is an attribute of the world.
    """
    self.x = x
    self.y = y
    self.dim = dim

  @classmethod
  def random(cls, dim):
    return Point(np.random.randint(low=0, high=dim[0]-1),
                 np.random.randint(low=0, high=dim[1]-1))

  def distance_to(self, p):
    v = Vector.from_points(self, p)
    return v.length()

  def __eq__(self, other):
    if self is None or other is None:
      return True if self is None and other is None else False
    return self.x == other.x and self.y == other.y and self.dim == other.dim

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

  def length(self):
    return np.sqrt(self.x * self.x + self.y * self.y)
