import logging


class Controller(object):
  """Controller is the world controller.

  Controller communicates with map, lives and food generator.
  """
  def __init__(self, option=None):
    logging.info("Initializing controller")
    option = {
      "autostart": False
    }

    # create map
    self._create_map()

    # create food generator
    self._create_food_generator()

    # create http server to receive bug request
    self._start_http_server()

    # start controller
    if option["autostart"]:
      self._start()

  def _create_map(self, option=None):
    logging.info("Creating map with options %s", option)

  def _create_bug(self, option=None):
    logging.info("Creating bug with options %s", option)

  def _create_food_generator(self, option=None):
    logging.info("Creating food generator with options %s", option)

  def _start_http_server(self):
    logging.info("Starting http server and listening to port: ")

  def _start(self):
    logging.info("Starting controller")
    