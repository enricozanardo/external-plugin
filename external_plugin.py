import click

@click.command()
def new_plugin_command():
    """Nuovo plugin."""
    click.echo("Questo è un nuovo plugin!")

if __name__ == '__main__':
    new_plugin_command()

