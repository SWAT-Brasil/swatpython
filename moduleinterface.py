import inspect
from abc import ABC, abstractmethod
from typing import Tuple
import pandas as pd


class ModuleInterface(ABC):
    """
    Interface for swat modules. Use this as a parent class for your modules. You must implement the abstractmethods,
    while the others are optional.
    """

    @abstractmethod
    def get_version(self) -> str:
        """
        Returns the module version
        """
        pass


    @abstractmethod
    def set_custom_swat(self, path):
        """
        Set custom swat executable if required
        :param path: to the executable
        :return: None
        """
        pass

    @abstractmethod
    def run(self, path):
        """
        runs the swat program inside path
        :param path: where to run swat
        :return: return code
        """
        pass

    @abstractmethod
    def async_run(self, path):
        """
        runs swat in async mode
        :param path:
        :return: the process object
        """
        pass

    def read_file_cio(self, filename):
        """
        read the file.cio and return a dictionary
        :param filename: path to the file to be read
        :return: dictionary
        """
        self._not_implemented_error()


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

