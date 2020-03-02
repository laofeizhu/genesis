import logging

from controller.controller import Controller


if __name__ == "__main__":
  logging.getLogger().setLevel(logging.INFO)

  # only run for 10 rounds
  controller = Controller()
  # bug creation is ideally provided as http request
  controller._create_bug()
  controller._start()