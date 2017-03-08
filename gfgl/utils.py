# -*- coding: utf-8 -*-
from . import GIT_ROOT_DIR
import configparser
import os


def load_config():
    conf_file = os.path.join(GIT_ROOT_DIR, '.git', 'gfgl.ini')
    config = configparser.ConfigParser()
    config.read(conf_file)
    return config
