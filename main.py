from container.sugar import SugarWorld
from life.cell import Cell

if __name__ == '__main__':
  world = SugarWorld()
  cell = Cell()
  world.add(cell)
  world.start()
