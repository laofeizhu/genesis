import numpy as np
import uuid

from utils.geometry import Point

class Food(object):

  def __init__(self, size=10, point=None):
    assert point != None
    self.point = point
    self.size = size
    self.field = {'smell': None}
    self.id = uuid.uuid4()

  def field_at(self, p):
    dist = self.point.distance_to(p, 'rect')
    return self.size / (dist + .1) / (dist + .1)

  def get_data_dict(self, step):
    return {
        "id": self.id,
        "size": self.size,
        "point": (self.point.x, self.point.y),
        "step": step,
        }
