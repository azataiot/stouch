# stouch

An extensible touch command with plugin support, allowing for enhanced file creation capabilities.

## Description

`stouch` is a modern take on the classic `touch` command, designed to be extensible with plugins. Whether you want to slugify filenames, add timestamps, or any other custom behavior, `stouch` has got you covered.

## Features

- **Extensible**: Easily add new functionalities with plugins.
- **Built-in Plugins**: Comes with a slugify plugin out of the box.
- **Easy to Use**: Simple CLI interface powered by Typer.

## Installation

Using poetry:

```bash
poetry install stouch
```

To install with the slugify plugin:

```bash
poetry install stouch[slugify]
```

## Usage

Basic usage:

```bash
stouch filename.txt
```

Using the slugify plugin:

```bash
stouch "My New File.txt" --plugin=slugify
```

## Developing Plugins

Check out our [plugin development guide](LINK_TO_PLUGIN_GUIDE) to learn how to create your own plugins for `stouch`.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read our [contributing guidelines](LINK_TO_CONTRIBUTING_GUIDE) to get started.

## Acknowledgements

- [Typer](https://typer.tiangolo.com/) for the CLI framework.
- [python-slugify](https://pypi.org/project/python-slugify/) for the slugification utility.
```
