import click


@click.group()
def support():
    """Manage your support branches."""
    pass


@click.command()
@click.argument('name')
def start(name):
    click.echo('starting support branch %s' % name)


@click.command()
@click.argument('name')
def finish(name):
    click.echo('finish support branch %s' % name)


@click.command()
@click.argument('name')
def publish(name):
    click.echo('publish support branch %s' % name)


support.add_command(start)
support.add_command(finish)
support.add_command(publish)
