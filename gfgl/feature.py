from .utils import load_config
import click


@click.group()
@click.pass_context
def feature(ctx):
    """Manage your feature branches."""
    pass


@click.command()
@click.argument('name')
@click.pass_context
def start(ctx, name):
    config = load_config()
    develop_branch = config['branch']['develop']
    feature_branch = config['prefix']['feature'] + name

    # Comandos
    git = ctx.obj.git
    git.checkout(develop_branch, b=feature_branch)

    click.echo("Switched to a new branch '%s'" % feature_branch)
    click.echo()
    click.echo("Summary of actions:")
    click.echo(
        "- A new branch '%s' was created, based on '%s'" %
        (feature_branch, develop_branch)
    )
    click.echo("- You are now on branch '%s'" % feature_branch)
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
