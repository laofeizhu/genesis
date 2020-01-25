from bug import Bug
from world import World, Food
from geometry import Point

def main():
  world = World()
  food = Food(5, Point(20,20))
  food2 = Food(15, Point(40,40))
  # bug = Bug(1, Point(10,10))
  world.place_food(food)
  world.place_food(food2)
  # world.place_bug(bug)  #TODO merge place_food and place_bug to place()
  world.show()

if __name__ == '__main__':
  main()
