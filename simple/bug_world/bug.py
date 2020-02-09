"""
A bug that eats moves and reproduces.
    Bug consumes food keeps size similar as cell
    Bugs has gender, only female bugs reproduces. There's equal chance of generating a male or a female bug. (think about how to do mix and generate new feature here, maybe start with changing parameters first)
    Think about how to make some noise for bugs to communicate.
    Bugs move in a 2d map to search for food. Food generates smell and bug has instinct to get the direction of food.
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

    def __init__(self, size=None, point=None):
        # growth rate based on extra food / food deficiency
        self._GROWTH_RATE = 0.1
        # maintanence multiplier to size
        self._MAINTANENCE_RATE = 0.1
        # max food multiplier to size
        self._MAX_FOOD_RATE = 1
        # number of cycles that the bug can live
        self._AGE_LIMIT = 100
        self.age = 0
        self.id = uuid.uuid4()
        if point == None:
            self.point = Point.random()
        else:
            self.point = point
        self._size = size
        self.DIRS = [Vector(v[0], v[1]) for v in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1))]
        self._vision = [0] * 8
        self.dir = self.DIRS[0]
        self.is_on_food=False

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

    def grow(self, food):
        """
        calculates the growth of the bug based on food supply
        the growth is controlled by growth rate, maintanence rate and maximum food.
        Return:
            consumed food
        """
        if food is None:
            return None
        consumed_food=np.minimum(food, self._size * self._MAX_FOOD_RATE)
        size_change=(consumed_food - self._size *
                       self._MAINTANENCE_RATE) * self._GROWTH_RATE
        self.age += 1
        return {
            "consumed_food": consumed_food,
            "is_live": self.age > self._AGE_LIMIT,
            "bug": self,
        }

    def choose_direction(self):
        """
        if the current spot is not the food spot, bug will move towards
        the food.
        Bug knows the food potential in all four directions.
        """
        max=-1
        dir=[0, 1]
        for idx, d in enumerate(self.DIRS):
            if self._vision[idx] > max:
                max = self._vision[idx]
                dir = d
        return dir
