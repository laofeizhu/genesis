from bug import Bug
from world import World, Food
from geometry import Point

def main():
  world = World()
  world.create_food(options={'point': [1, 1]})
  world.create_bug()
  # world.place_bug(bug)  #TODO merge place_food and place_bug to place()
  world.show_field('smell')

if __name__ == '__main__':
  main()
