# -*- coding: utf-8 -*-
from subprocess import Popen, STDOUT, PIPE
import configparser
import os
import click

# Raise an exception if current folder is not versioned in git
command = Popen(
    ['git', 'rev-parse', '--show-toplevel'], stdout=PIPE, stderr=STDOUT
)
stdout, nothing = command.communicate()
if stdout.decode().startswith('fatal'):
    raise click.exceptions.ClickException(
        "Git not found in current directory. (%s)" % os.getcwd()
    )

# Get git base root folder
GIT_ROOT_DIR = stdout.decode().replace('\n', '')
# Configuration
GFGL_CONFIG = None
conf_file = os.path.join(GIT_ROOT_DIR, '.git', 'gfgl.ini')
if os.path.exists(conf_file):
    GFGL_CONFIG = configparser.ConfigParser()
    GFGL_CONFIG.read(conf_file)
