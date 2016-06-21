from __future__ import absolute_import
import pkg_resources
import logging

from .machine import Machine
from machine import configs

try:
    __version__ = pkg_resources.require("python-docker-machine")[0].version
except pkg_resources.DistributionNotFound:
    __version__ = "devel"

# ### ---- logger
# 1. logger
logger = logging.getLogger("machine")
logger.setLevel(logging.INFO)

# 2. Add handler
steam_handler = logging.StreamHandler()
steam_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s :: %(levelname)s :: %(message)s')
steam_handler.setFormatter(formatter)
logger.addHandler(steam_handler)
