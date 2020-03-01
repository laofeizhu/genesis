import logging

from controller import Controller


if __name__ == "__main__":
  logging.getLogger().setLevel(logging.INFO)

  # only run for 10 rounds
  controller = Controller(option)
  # map option specifies map size
  controller.create_map(map_option)
  # bug creation is ideally provided as http request
  controller._create_bug(bug_option)
  # food generator can be included in controller options
  controller._create_food_generator(food_generator_option)
  controller._start()