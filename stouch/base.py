# base.py

from abc import ABC, abstractmethod


class BasePlugin(ABC):
    """
    Abstract base class for all stouch plugins.
    """

    @abstractmethod
    def process(self, input_data: str) -> str:
        """
        Process the input data and return the modified data.

        Args:
            input_data (str): The input data to be processed.

        Returns:
            str: The processed data.
        """
        pass

    def setup(self) -> None:
        """
        Optional setup method for the plugin. Can be used for initialization tasks.
        By default, it does nothing but can be overridden by specific plugins.
        """
        pass

    def teardown(self) -> None:
        """
        Optional teardown method for the plugin. Can be used for cleanup tasks.
        By default, it does nothing but can be overridden by specific plugins.
        """
        pass
