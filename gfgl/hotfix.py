import click


@click.group()
def hotfix():
    """Manage your hotfix branches."""
    pass


@click.command()
@click.argument('name')
def start(name):
    click.echo('starting hotfix branch %s' % name)


@click.command()
@click.argument('name')
def finish(name):
    click.echo('finish hotfix branch %s' % name)


@click.command()
@click.argument('name')
def publish(name):
    click.echo('publish hotfix branch %s' % name)


hotfix.add_command(start)
hotfix.add_command(finish)
hotfix.add_command(publish)
