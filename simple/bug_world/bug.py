"""A bug that eats moves and reproduces.

    Bug consumes food keeps size similar as cell
    Bugs has gender, only female bugs reproduces. There's equal chance of
    generating a male or a female bug. (think about how to do mix and generate
    new feature here, maybe start with changing parameters first)
    Think about how to make some noise for bugs to communicate.
    Bugs move in a 2d map to search for food. Food generates smell and bug has
    instinct to get the direction of food.
    Food can be consumed but new food generates at certain rate.
"""
import numpy as np
import uuid

from enum import Enum
from geometry import Point, Vector


class Gender(Enum):
  MALE = 1
  FEMALE = 2


class Bug(object):
  """The bug class"""

  def __init__(self, size=None, point=None, age=None):
    # growth rate based on extra food / food deficiency
    self._GROWTH_RATE = 0.1
    # maintanence multiplier to size
    self._MAINTANENCE_RATE = 0.1
    # max food multiplier to size
    self._MAX_FOOD_RATE = 1
    # number of cycles that the bug can live
    self._AGE_LIMIT = 100
    # if current_size / age < MIN_SIZE_RATIO, bug will
    # die because it's too thin.
    self._MIN_SIZE_RATIO = 0.4
    # each bug will have a random uuid
    self.id = uuid.uuid4()
    # initialize bug status
    self.size = size if size else 0
    self.point = point if point else Point.random()
    self.age = age if age else 0

    self.DIRS = [
        Vector(v[0], v[1]) for v in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1),
                                     (-1, -1), (-1, 0), (-1, 1))
    ]
    self._vision = [0] * 8
    self.dir = self.DIRS[0]
    self.is_on_food = False
    self.food_supply = 0

  def is_too_thin(self):
    """ bug will die if it's too think """
    return self.size / self.age < self._MIN_SIZE_RATIO

  def maybe_move(self):
    # maybe move the bug and return a dict indicating the move
    if not self._should_move():
      return None
    d = self.choose_direction()
    move = {
        "from": self.point,
        "to": self.point.add(d),
        "bug": self,
    }

    self.point = move["to"]
    return move

  def _should_move(self):
    """ this is a super simple logic for now """
    return not self.is_on_food

  def get_dirs(self):
    return self.DIRS

  def set_vision(self, idx, v):
    self._vision[idx] = v

  def _calc_maintain(self):
    MT_SIZE_RATIO = 1
    MT_AGE_RATIO = 0.1
    return self.size * MT_SIZE_RATIO + self.age * MT_AGE_RATIO

  def _calc_max_food(self):
    MF_SIZE_RATIO = 2
    MF_AGE_RATIO = 0.2
    return self.size * MF_SIZE_RATIO + self.age * MF_AGE_RATIO

  def _calc_growth(self, food_consumption, food_maintain):
    GROWTH_RATE = 0.1
    return (food_consumption - food_maintain) * GROWTH_RATE
  
  def grow(self):
    """
        calculates the growth of the bug based on food supply
        the growth is controlled by growth rate, maintanence rate and maximum
        food.
        Return:
            consumed food
    """
    food_maintain = self._calc_maintain()
    food_max = self._calc_max_food()
    consumed = min(food_max, self.food_supply)
    growth = self._calc_growth(consumed, food_maintain)
    self.size += growth
    self.age += 1
    self.food_supply = 0
    return {
        "consumed_food": consumed,
        "is_live": self.age < self._AGE_LIMIT and not self.is_too_thin,
        "bug": self,
    }

  def choose_direction(self):
    """
        if the current spot is not the food spot, bug will move towards
        the food.
        Bug knows the food potential in all four directions.
        """
    max = -1
    dir = [0, 1]
    for idx, d in enumerate(self.DIRS):
      if self._vision[idx] > max:
        max = self._vision[idx]
        dir = d
    return dir
