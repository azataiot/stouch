# plugins/slugify.py

from stouch.base import BasePlugin

try:
    from slugify import slugify
except ImportError:
    raise ImportError(
        "The 'python-slugify' package is required to use the SlugifyPlugin. Please install it using 'poetry install "
        "--extras \"slugify\"' or 'pip install stouch[slugify]'.")


class SlugifyPlugin(BasePlugin):
    """
    Plugin to slugify filenames.
    """

    def process(self, input_data: str) -> str:
        """
        Slugify the input filename.

        Args:
            input_data (str): The input filename to be slugified.

        Returns:
            str: The slugified filename.
        """
        return slugify(input_data, separator='-')
