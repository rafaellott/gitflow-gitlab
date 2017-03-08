# -*- coding: utf-8 -*-
import os
from subprocess import Popen, STDOUT, PIPE

# Raise an exception if current folder is not versioned in git
command = Popen(
    ['git', 'rev-parse', '--show-toplevel'], stdout=PIPE, stderr=STDOUT
)
stdout, nothing = command.communicate()
if stdout.decode().startswith('fatal'):
    raise Exception("Git not found in current directory. (%s)" % os.getcwd())

# Get git base root folder
GIT_ROOT_DIR = stdout.decode().replace('\n', '')
