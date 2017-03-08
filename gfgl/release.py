import click


@click.group()
def release():
    """Manage your release branches."""
    pass


@click.command()
@click.argument('name')
def start(name):
    click.echo('starting release branch %s' % name)


@click.command()
@click.argument('name')
def finish(name):
    click.echo('finish release branch %s' % name)


@click.command()
@click.argument('name')
def publish(name):
    click.echo('publish release branch %s' % name)


release.add_command(start)
release.add_command(finish)
release.add_command(publish)
