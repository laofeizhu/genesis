from bug import Bug
from world import World, Food

def main():
  world = World()
  food = Food()
  bug = Bug()
  world.place_bug(bug)
  world.place_food(food)

  for i in range(100):
    world.update()

if __name__ == '__main__':
  main()
