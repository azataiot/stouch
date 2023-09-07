# cli.py

import os
from importlib import import_module

import typer

from stouch.base import BasePlugin

app = typer.Typer()


def load_plugins():
    """
    Dynamically load all plugins from the plugins directory.
    """
    plugins = {}
    plugins_dir = os.path.join(os.path.dirname(__file__), "..", "plugins")
    for filename in os.listdir(plugins_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]  # Remove .py extension
            module = import_module(f"plugins.{module_name}")
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if (
                    isinstance(attr, type)
                    and issubclass(attr, BasePlugin)
                    and attr != BasePlugin
                ):
                    plugins[module_name] = attr()
    return plugins


@app.command()
def touch(filename: str, plugin: str = typer.Option(None, help="Plugin to use")):
    """
    Create a new file. If a plugin is specified, process the filename using the plugin.
    """
    plugins = load_plugins()
    if plugin and plugin in plugins:
        filename = plugins[plugin].process(filename)

    # Create the file
    with open(filename, "w") as f:
        f.write("")  # Create an empty file

    typer.echo(f"File '{filename}' stouched!")


if __name__ == "__main__":
    app()
