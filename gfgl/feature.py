from .utils import load_config
import click


@click.group()
def feature():
    """Manage your feature branches."""
    pass


@click.command()
@click.argument('name')
def start(name):
    config = load_config()
    click.echo("Switched to a new branch 'feature/%s'" % name)
    click.echo()
    click.echo("Summary of actions:")
    click.echo(
        "- A new branch 'feature/%s' was created, based on '%s'" %
        (name, config['branch']['develop'])
    )
    click.echo("- You are now on branch 'feature/%s'" % name)
    click.echo()
    click.echo('Now, start committing on your feature. When done, use:')
    click.echo()
    click.echo("     gfgl feature finish %s" % name)


@click.command()
@click.argument('name')
def finish(name):
    click.echo('finish feature branch %s' % name)


@click.command()
@click.argument('name')
def publish(name):
    click.echo('publish feature branch %s' % name)


feature.add_command(start)
feature.add_command(finish)
feature.add_command(publish)
