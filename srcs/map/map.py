import logging

from config import CONFIG
from utils.geometry import Point

class Cell(Point):
  def __init__(self, x, y, dim):
    super(Cell, self).__init__(x, y, dim)
    self.lives = {}
    self.food = None
    self.field = {}
    self.id = uuid.uuid4()

  def add_life(self, life):
    self.lives[life.id] = life

  def remove_life(self, life):
    self.lives.pop(life.id)
    del life

class Map(object):
  def __init__(self, config=CONFIG):
    self._config = config
    self._cells = [[Cell(i, j) for i in range(self._config['dim'][1])] for j in range(self._config['dim'][0])]
    self._life_cells = {} # a dict from cell id to cell
    self._food_cells = {} # a dict from cell id to cell
    self._step_count = 0

  def add_life(self, life=None):
    if life is None:
      logging.warn("Adding life=None")
      return
    cell = self.get_cell(life.point.x, life.point.y)
    cell.add_life(life)
    self._life_cells[life.id] = cell

  def remove_life(self, life=None):
    if life is None:
      logging.warn("Removing life=None")
      return
    cell = self.get_cell(life.point.x, life.point.y)
    cell.remove_life(life)
    if len(cell.lives) == 0:
      self.life_cells.pop(cell.id)

  def add_food(self, food):
    if food is None:
      return
    cell = self.get_cell(food.point.x, food.point.y)
    cell.food = food
    self._food_cells[cell.id] = cell
  
  def maybe_remove_food(self, food):
    if food.size > 0.001:
      return
    cell = self.get_cell(food.point.x, food.point.y)
    cell.food = None
    self._foods.pop(food.id)
    self._food_cells.pop(cell.id)

  def update(self):
    """ After setting down the lives and foods, do an update for the whole map """
    # only cells near lives are necessary to get updated
    cells_to_update = self._get_cells_to_update()
    self._clear_fields(cells_to_update)
    # update fields in the cells to update
    for _, food_cell in self._food_cells.items():
      self._update_fields(food_cell.food, cells_to_update)
    # update vision for all the lives
    for _, life_cell in self._life_cells.items():
      for _, life in life_cell.items():
        self._update_vision(life)

  def _get_cells_to_update(self):
    cells = {}
    for _, life_cell in self._life_cells.items():
      for _, life in life_cell.items():
        for _, d in enumerate(life.get_dirs()):
          p = life.point.add(d)
          new_cell = self.get_cell(p.x, p.y)
          cells[new_cell.id] = new_cell
    return cells

  def _clear_fields(self, cells):
    for _, cell in cells.items():
      cell.field = {"smell": 0}

  def _update_fields(self, food, cells):
    for _, cell in cells.items():
      cell.field["smell"] += food.field_at(cell.point)

  def _update_vision(self, life):
    for idx, d in enumerate(life.get_dirs()):
      p = life.point.add(d)
      life.set_vision(idx, self.get_cell(p.x, p.y).field["smell"])



      
    
