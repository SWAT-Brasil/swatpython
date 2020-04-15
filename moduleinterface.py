import inspect
from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd


class ModuleInterface(ABC):
    """
    Interface for swat modules. Use this as a parent class for your modules. You mus timplement the abstractmethods,
    while the others are optional.
    """

    @abstractmethod
    def get_version(self) -> str:
        """
        Returns the module version
        """
        pass

    @abstractmethod
    def get_linux_64bits(self) -> str:
        """
        Returns the path tho swat executable in linux
        """
        pass

    @abstractmethod
    def get_windows_64bits(self) -> str:
        """
        Returns the path to swat executable in windows
        """
        pass

    def read_precipitation_daily(self, filename: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Reads the pcp files
        Parameters
        ----------
        filename
        """
        self._not_implemented_error()

    def write_precipitation_daily(self, filename: str, info: pd.DataFrame, dataframe: pd.DataFrame) -> None:
        """
        Write to a pcp file
        Parameters
        ----------
        filename
        info
        dataframe
        """
        self._not_implemented_error()

    def read_precipitation_sub_daily(self, filename: str) -> Tuple[pd.DataFrame, pd.DataFrame]:
        """
        Reads a sub daily pcp file
        Parameters
        ----------
        filename
        """
        self._not_implemented_error()

    def write_precipitation_sub_daily(self, filename: str, info: pd.DataFrame, dataframe: pd.DataFrame) -> None:
        """
        Write a sub daily pcp file
        Parameters
        ----------
        filename
        info
        dataframe
        """
        self._not_implemented_error()

    def read_output_rch(self, filename: str) -> pd.DataFrame:
        """
        Reads the file output.rch
        Parameters
        ----------
        filename
        dataframe
        """
        self._not_implemented_error()

    def _not_implemented_error(self):
        """
        Raises exception when method is not implemented
        """
        raise Exception("Method '" + inspect.stack()[1].function + "' not implemented. Check module.")

