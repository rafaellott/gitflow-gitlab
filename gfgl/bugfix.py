import click


@click.group()
def bugfix():
    """Manage your bugfix branches."""
    pass


@click.command()
@click.argument('name')
def start(name):
    click.echo('starting bugfix branch %s' % name)


@click.command()
@click.argument('name')
def finish(name):
    click.echo('finish bugfix branch %s' % name)


@click.command()
@click.argument('name')
def publish(name):
    click.echo('publish bugfix branch %s' % name)


bugfix.add_command(start)
bugfix.add_command(finish)
bugfix.add_command(publish)
