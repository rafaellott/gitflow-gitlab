# -*- coding: utf-8 -*-
from . import GIT_ROOT_DIR, GFGL_CONFIG
from git import Repo
import configparser
import os
import click


def check_before_commands():
    # Ini file exists?
    check_ini_file()
    # Base branches (master/develop) exists?
    check_base_branches_exists()
    # Is working directory is clean?
    if Repo(GIT_ROOT_DIR).is_dirty():
        raise click.exceptions.ClickException(
            "Your working directory is not clean. Please commit your changes."
        )


def check_base_branches_exists():
    if GFGL_CONFIG:
        repo = Repo(GIT_ROOT_DIR)
        git = repo.git
        # Loop base branches, 'master' and 'develop'
        for base_branch in GFGL_CONFIG['branch'].values():
            # print('checking local branches-', base_branch)
            # Check if those brances are in local repository
            if base_branch not in repo.branches:
                # print('local branch not found-', base_branch)
                # if not them need to check if they are in remote's
                rm = repo.remote()
                found_branch = False
                for remote_branch in rm.refs:
                    # if base branch is in remote, then need to checkout it
                    branch_name = rm.name + '/' + base_branch
                    # print('checking remote branches-', branch_name)
                    if branch_name == remote_branch.name:
                        found_branch = True
                        # print('remote branch found-', branch_name)
                        remote_branch.checkout()
                        # git.checkout(branch_name)
                        # print('checkout to local branches-', branch_name)
                        # print('achei no remoto')
                if not found_branch:
                    raise click.exceptions.ClickException(
                        "One of the base branch wasn't found either in local "
                        "repositry neither in remote repositry"
                    )
                # print('NOT IN')
            # else:
                # print('IN')
    else:
        raise click.exceptions.ClickException("CONFIG NOT FOUND")


def check_ini_file():
    # Check if current .git folder contains the gfgl configuration file
    if not os.path.exists(os.path.join(GIT_ROOT_DIR, '.git', 'gfgl.ini')):
        # Raise an exception and inform how to start gfgl
        raise click.exceptions.ClickException(
            "GitFlowGitLab not initialize. Run 'gfgl init' to start."
        )


def load_config():
    conf_file = os.path.join(GIT_ROOT_DIR, '.git', 'gfgl.ini')
    config = configparser.ConfigParser()
    config.read(conf_file)
    return config
