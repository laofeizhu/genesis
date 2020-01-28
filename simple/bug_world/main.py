from bug import Bug
from world import World, Food
from geometry import Point

def main():
  config = {
      'dim': [20, 30],
      'default_bug_size': 5,
  }
  world = World(config=config)
  world.create_food(options={'point': [1, 1]})
  world.create_bug(options={'point': [10, 10]})
  world.show_field('smell')

if __name__ == '__main__':
  main()
