# -*- coding: utf-8 -*-
from . import GIT_ROOT_DIR
from .feature import feature as feature_cmd
from .hotfix import hotfix as hotfix_cmd
from .bugfix import bugfix as bugfix_cmd
from .support import support as support_cmd
from .release import release as release_cmd
import configparser
import click
import os


@click.group()
def gfgl():
    pass


@click.command()
def init():
    """Initialize a new git repo with support for the branching model."""
    # check_ini_file()
    conf_file = open(os.path.join(GIT_ROOT_DIR, '.git', 'gfgl.ini'), 'w')
    GFGL_CONFIG = configparser.ConfigParser()
    ask_branch(GFGL_CONFIG)
    click.echo()
    ask_feature(GFGL_CONFIG)
    GFGL_CONFIG.write(conf_file)
    print('Your value is', GFGL_CONFIG)


def check_ini_file():
    # Check if current .git folder contains the gfgl configuration file
    if os.path.exists(os.path.join(GIT_ROOT_DIR, '.git', 'gfgl.ini')):
        # Loads configurations
        return True
    else:
        # Raise an exception and inform how to start gfgl
        raise Exception(
            "GitFlowGitLab not initialize. Run 'gfgl init' to start."
        )


def ask_branch(GFGL_CONFIG):
    # BRANCH
    click.echo(
        'Which branch should be used for bringing forth production releases?'
    )
    click.echo('    - develop')
    click.echo('    - master')
    # PRODUCTION
    master = click.prompt(
        'Branch name for production releases:',
        type=str, default='master'
    )
    click.echo()
    # DEVELOP
    click.echo(
        'Which branch should be used for integration of the "next release"?'
    )
    click.echo('    - develop')
    develop = click.prompt(
        'Branch name for "next release" development:',
        type=str, default='develop'
    )
    # configparser
    GFGL_CONFIG.add_section('branch')
    GFGL_CONFIG.set('branch', 'master', master)
    GFGL_CONFIG.set('branch', 'develop', develop)

    return GFGL_CONFIG


def ask_feature(GFGL_CONFIG):
    click.echo('How to name your supporting branch prefixes?')
    feature = click.prompt('Feature branches?', default='feature/', type=str)
    bugfix = click.prompt('Bugfix branches?', default='bugfix/', type=str)
    release = click.prompt('Release branches?', default='release/', type=str)
    hotfix = click.prompt('Hotfix branches?', default='hotfix/', type=str)
    support = click.prompt('Support branches?', default='support/', type=str)
    versiontag = click.prompt('Version tag prefix?', default='', type=str)

    # configparser
    GFGL_CONFIG.add_section('prefix')
    GFGL_CONFIG.set('prefix', 'feature', feature)
    GFGL_CONFIG.set('prefix', 'bugfix', bugfix)
    GFGL_CONFIG.set('prefix', 'release', release)
    GFGL_CONFIG.set('prefix', 'hotfix', hotfix)
    GFGL_CONFIG.set('prefix', 'support', support)
    GFGL_CONFIG.set('prefix', 'versiontag', versiontag)
    return GFGL_CONFIG


gfgl.add_command(init)
gfgl.add_command(feature_cmd)
gfgl.add_command(hotfix_cmd)
gfgl.add_command(bugfix_cmd)
gfgl.add_command(support_cmd)
gfgl.add_command(release_cmd)


if __name__ == '__main__':
    gfgl()
