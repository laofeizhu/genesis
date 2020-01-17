"""
Cell class with properties:
    cell grows and eats more food
    if food is not sufficient, cell shrinks
    cell reproduces as it reaches some size
    reproduction generates a new cell with small size
    reproduction reduces mother cell's size
    cell growth has a limit in size
    cell growth has a limit in cycles, insufficient food will also reduce life
    dead cell will get no size and free the space
    food supply per cycle is limited, cells will share with some strategy when food is insufficient (proportional to size for now).
"""
    
import numpy as np

class Cell(object):

    size = 1
    _AGE_LIMIT= 20
    _REPRODUCE_SIZE = 10
    age = 0

    def size_change(self, food, size):
        """ calculates the size change based on food supply and current size, by default one unit of size needs one unit of food to maintain. The additional food will help grow at certain rate"""
        if food > size:
            return np.minimum((food-size)/10, 1)
        if food < size:
            return np.maximum((food-size)/10, -1)

    def is_live(self):
        """check if cell is too old and dead"""
        return self.age <= self._AGE_LIMIT

    def maybe_reproduce(self):
        if self.size > self._REPRODUCE_SIZE:
            self.size -= 2
            return Cell()
        return None

    def grow(self, food):
        """
        the cell grows in one cycle with the amout of food
        If the cell can reproduce, it reproduces a new cell and return the new cell. Otherwise return None.
        """
        self.age += 1
        self.size += self.size_change(food, self.size)
        return self.maybe_reproduce()


        

