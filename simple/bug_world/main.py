from bug import Bug
from world import World, Food

def main():
  world = World()
  food = Food()
  food2 = Food(5)
  world.place_food(food)
  world.place_food(food2)
  world.show()

if __name__ == '__main__':
  main()
