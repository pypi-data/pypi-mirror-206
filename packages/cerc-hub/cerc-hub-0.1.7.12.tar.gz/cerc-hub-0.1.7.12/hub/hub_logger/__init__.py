import logging as logger
from pathlib import Path
import os
import logging
import sys


def get_logger(file_logger=False):
  """
  Returns a logging object
  :param file_logger: a boolean to indicate the kind of logging
  object to return, true (default) means a file logger is required
  :return:
  """
  log_format = "%(asctime)s:%(levelname)s:{%(pathname)s:%(funcName)s:%(lineno)d} - %(message)s"
  if file_logger:
    log_dir = (Path(__file__).parent.parent / 'logs').resolve()
    log_file = (log_dir / 'hub.log').resolve()
    try:
      if not os.path.isfile(log_file):
        if not os.path.exists(log_dir):
          os.mkdir(log_dir)
        with open(log_file, 'x'):
          pass
      logger.basicConfig(filename=log_file, format=log_format, level=logger.DEBUG)
      return logger
    except IOError as err:
      print(f'I/O exception: {err}')
  else:
    logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
    logging.getLogger().setLevel(logging.DEBUG)
    return logger.getLogger()

