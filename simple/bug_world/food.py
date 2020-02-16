import numpy as np
import uuid

from geometry import Point

class Food(object):

  def __init__(self, size=10, point=None):
    assert point != None
    self.point = point
    self.size = size
    self.fields = {'smell': None}
    self.id = uuid.uuid4()

  def get_data_dict(self, step):
    return {
        "id": self.id,
        "size": self.size,
        "point": (self.point.x, self.point.y),
        "step": step,
        }

  def set_random_point(self):
    self.point = Point.random()

  def update_smell_field(self, dim=None):
    assert dim != None
    if self.fields['smell'] == None:
      self.fields['smell'] = np.zeros(dim)
    for x in range(dim[0]):
      for y in range(dim[1]):
        dist = self.point.distance_to(Point(x, y, self.point.dim), 'rect')  # optimize to use a cached map instead of creating the point each time.
        self.fields['smell'][x][y] = self.size / (dist + .1) / (dist + .1)  # plus .1 to avoid singularity.
