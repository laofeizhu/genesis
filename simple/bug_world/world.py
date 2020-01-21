"""
The world class.
The world is a 2d plane in a donut shape.
The world has food points in it. The food coordinates are always
integers.
Food has smells, which is inverse proportional to the distance,
the distance at the food will be 1 to avoid dividing by 0.
The smell is also proportional to the food quantity.
Distance is defined as the closest distance to the food.
"""

class World(object):

    def __init__(self):
        self._WIDTH = 10
        self._HEIGHT = 10
        self._foods = []
        self._bugs = []
        self._smells = np.zeros((self._WIDTH, self._HEIGHT))

    def place_food(self, food, point):
        self._foods.append(food)
        self.update_smells(food, point)
