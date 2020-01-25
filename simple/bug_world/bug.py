"""
A bug that eats moves and reproduces.
    Bug consumes food keeps size similar as cell
    Bugs has gender, only female bugs reproduces. There's equal chance of generating a male or a female bug. (think about how to do mix and generate new feature here, maybe start with changing parameters first)
    Think about how to make some noise for bugs to communicate.
    Bugs move in a 2d map to search for food. Food generates smell and bug has instinct to get the direction of food.
    Food can be consumed but new food generates at certain rate.
"""

from enum import Enum

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
        self._DIRS = [[0,1],[0,-1],[-1,0],[1,0]]
        # number of cycles that the bug can live
        self._AGE_LIMIT = 100
        if point == None:
          self.point = Point.random()
        else:
          self.point = point
        self.size = size

    def grow(self, food):
        """
        calculates the growth of the bug based on food supply
        the growth is controlled by growth rate, maintanence rate and maximum food.
        Return:
            consumed food
        """
        consumed_food = np.minimum(food, self._size * self._MAX_FOOD_RATE)
        size_change = (consumed_food - self._size * self._MAINTANENCE_RATE) * self._GROWTH_RATE
        return consumed_food

    def update_direction(self, smells):
        """
        if the current spot is not the food spot, bug will move towards
        the food.
        Bug knows the food potential in all four directions.
        """
        max = -1
        dir = [0, 1]
        for i in range(4):
            if self._food_potential[i] > max:
                max = self._food_potential[i]
                dir = self.DIRS[i]
        return dir



