import logging
import subprocess
import sys
from abc import ABC

import numpy
import pandas as pd
import re
import os
from swatpython.moduleinterface import ModuleInterface
from swatpython.operationalsystem import OperationalSystem

logger = logging.getLogger(__name__)


class SWAT2012rev670(ModuleInterface):
    """ Classe com funcoes especificas para o SWAT2012rev670.
        Isso foi separado pois cada versão pode ter alguma formatacao diferente uma do outra,
        por isso precisa de uma classe espefica. Isso é transparente no uso, pois a classe
        correta é escolhida automaticamente quanto é criado o swatpython. Pelo menos é a ideia

    """

    def __init__(self, operational_system):
        self.operational_system = operational_system
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.custom_swat_path = None

    def get_version(self):
        return "swat2012rev670"

    def get_linux_64bits(self):
        """
        Returns the linux 64bits executable path
        Returns
        -------
        path: to executable
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_path, "swat2012_rev670_linux")
        return path

    def get_windows_64bits(self):
        """
        Returns the windows 64bits executable path
        Returns
        -------
        path: to executable
        """
        current_path = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(current_path, "swat2012_rev670_windows")
        return path

    def get_version(self) -> str:
        return "SWAT2012rev670"

    def windows(self) -> bool:
        return self.operational_system == OperationalSystem.WINDOWS

    def linux(self) -> bool:
        return self.operational_system == OperationalSystem.LINUX

    def set_custom_swat(self, path):
        self.custom_swat_path = path;

    def run(self, path):
        if self.linux():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path , "swat2012_rev670_linux")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            #return subprocess.call([cmd], cwd=path, shell=True)
            process = subprocess.Popen(cmd, cwd=path, stdout=subprocess.PIPE, universal_newlines=True)
            for line in process.stdout:
                sys.stdout.write(line)
            return process.returncode
        if self.windows():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path, "swat2012_rev670_windows.exe")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            return subprocess.call(cmd, cwd=path, creationflags=subprocess.CREATE_NEW_CONSOLE)

    def async_run(self, path):
        logger.debug("Runnning sufi2_async_run")
        if self.linux():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path , "swat2012_rev670_linux")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            return subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.DEVNULL)
        if self.windows():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path, "swat2012_rev670_windows.exe")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            return subprocess.Popen([cmd], cwd=path, creationflags=subprocess.CREATE_NEW_CONSOLE)

    def read_precipitation_daily(self, filename):
        """

        Parameters
        ----------
        filename : file name

        Returns
        -------
        info, df : informacao e dados em dataframe pandas

        """
        # Abre arquivo
        fo = open(filename, "r")
        # Abre arquivo
        #fo = open("./temp/pcp1.pcp", "r")
        # Le informações do arquivo e separa informacoes por espaco e virgula e outras coisinhas mais
        title = re.findall(r"[^\s\,!?:;'\"]+", fo.readline())
        # Calcula o numero de variaveis do arquivo
        param_count = len(title) - 1
        data_widths = [7] + [5] * param_count
        latitude = pd.read_fwf(fo, widths=data_widths, header=None, index_col=None, nrows=3)
        # Dataframe de informacao
        info = pd.concat([pd.DataFrame([title]), latitude])
        data_widths = [4, 3] + [5] * param_count
        df = pd.read_fwf(fo, widths=data_widths, header=None, index_col=None)
        df.columns = ['year', 'day'] + title[1:]
        fo.close()

        return info, df

    def write_precipitation_daily(self, filename, info, dataframe):
        """
        Salva dados para arquivo pcp. Note que ele vai sobre escrever o arquivo existente

        Parameters
        ----------
        filename : file name with path
        info : dataframe with information
        data : dataframe with variable values
        """
        info_numpy = info.to_numpy()
        title = info_numpy[0]
        param_count = len(title) - 1
        latitude = info_numpy[1]
        longitude = info_numpy[2]
        elevation = info_numpy[3]
        fo = open(filename, "w")
        numpy.savetxt(fo, [title], fmt="%-9s" + "%s," * param_count)
        numpy.savetxt(fo, [latitude], fmt="%-7s" + "%5.1f" * param_count)
        numpy.savetxt(fo, [longitude], fmt="%-7s" + "%5.1f" * param_count)
        numpy.savetxt(fo, [elevation], fmt="%-7s" + "%5i" * param_count)
        dataframe_numpy = dataframe.to_numpy()
        numpy.savetxt(fo, dataframe_numpy, fmt="%4i%03i" + "%05.1f" * param_count)
        fo.close()

    def read_output_rch(self, filename):
        fo = open(filename, "r")
        # Numero total de parametros nesse arquivo. Deve ser fixo para uma determinada versao.
        param_count = 47
        data_widths = [7, 4, 9, 6] + [12] * param_count
        dataframe = pd.read_fwf(fo, widths=data_widths, header=8, index_col=None)
        fo.close()
        return dataframe



