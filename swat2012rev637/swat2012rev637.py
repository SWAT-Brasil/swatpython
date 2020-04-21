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


class SWAT2012rev637(ModuleInterface):
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
        return "swat2012rev637"

    def windows(self) -> bool:
        return self.operational_system == OperationalSystem.WINDOWS

    def linux(self) -> bool:
        return self.operational_system == OperationalSystem.LINUX

    def set_custom_swat(self, path):
        self.custom_swat_path = path;

    def run(self, path):
        """
        Runs swat and shows output.
        :param path: to project
        :return: return code
        """
        if self.linux():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path, "swat2012_rev637_linux")
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
            cmd = os.path.join(self.current_path, "swat2012_rev637_windows.exe")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            #return subprocess.call([cmd], cwd=path, creationflags=subprocess.CREATE_NEW_CONSOLE)
            #return subprocess.call([cmd], cwd=path)
            process = subprocess.Popen(cmd, cwd=path, stdout=subprocess.PIPE, universal_newlines=True)
            for line in process.stdout:
                sys.stdout.write(line)
            return process.returncode

    def async_run(self, path):
        logger.debug("Running swat_async_run")
        if self.linux():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path , "swat2012_rev637_linux")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            return subprocess.Popen(cmd, cwd=path, shell=True, stdout=subprocess.DEVNULL)
        if self.windows():
            #cmd = os.path.join(path, "swat.exe")
            cmd = os.path.join(self.current_path, "swat2012_rev637_windows.exe")
            if self.custom_swat_path is not None:
                cmd = self.custom_swat_path
                logger.debug("Using custom SWAT : " + self.custom_swat_path)
            #return subprocess.Popen([cmd], cwd=path, creationflags=subprocess.CREATE_NEW_CONSOLE)
            return subprocess.Popen([cmd], cwd=path, stdout=subprocess.DEVNULL)

    def read_file_cio(self, filename):
        fo = open(filename, "r")
        # Le
        fo.readline()
        fo.readline()
        fo.readline()
        fo.readline()
        fo.readline()
        fo.readline()
        filecio = {'FIGFILE': re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0]}
        filecio.update({'NBYR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IYR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IDAF': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IDAL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        fo.readline()
        filecio.update({'IGEN': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'PCPSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IDT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IDIST': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'REXP': float(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NRGAGE': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NRTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NRGFIL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'TMPSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NTGAGE': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NTTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NTGFIL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'SLRSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NSTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'RHSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NHTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'WNDSIM': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NWTOT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'FCSTYR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'FCSDAY': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'FCSTCYCLES': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        fo.readline()
        line = fo.readline()
        files = []
        for i in range(0, len(line), 13):
            name = line[i:13].strip()
            if name != '':
                files.append(name)
        filecio.update({'RFILE1_6': files})
        line = fo.readline()
        files = []
        for i in range(0, len(line), 13):
            name = line[i:13].strip()
            if name != '':
                files.append(name)
        filecio.update({'RFILE7_12': files})
        line = fo.readline()
        files = []
        for i in range(0, len(line), 13):
            name = line[i:13].strip()
            if name != '':
                files.append(name)
        filecio.update({'RFILE13_18': files})
        fo.readline()
        line = fo.readline()
        files = []
        for i in range(0, len(line), 13):
            name = line[i:13].strip()
            if name != '':
                files.append(name)
        filecio.update({'TFILE1_6': files})
        line = fo.readline()
        files = []
        for i in range(0, len(line), 13):
            name = line[i:13].strip()
            if name != '':
                files.append(name)
        filecio.update({'TFILE7_12': files})
        line = fo.readline()
        files = []
        for i in range(0, len(line), 13):
            name = line[i:13].strip()
            if name != '':
                files.append(name)
        filecio.update({'TFILE13_18': files})

        filecio.update({'SLRFILE': fo.readline()[0:12].strip()})
        filecio.update({'RHFILE': fo.readline()[0:12].strip()})
        filecio.update({'WNDFILE': fo.readline()[0:12].strip()})
        filecio.update({'FCSTFILE': fo.readline()[0:12].strip()})
        fo.readline()
        filecio.update({'BSNFILE': fo.readline()[0:12].strip()})
        fo.readline()
        filecio.update({'PLANTDB': fo.readline()[0:12].strip()})
        filecio.update({'TILLDB': fo.readline()[0:12].strip()})
        filecio.update({'PESTDB': fo.readline()[0:12].strip()})
        filecio.update({'FERTDB': fo.readline()[0:12].strip()})
        filecio.update({'URBAMDB': fo.readline()[0:12].strip()})
        fo.readline()
        filecio.update({'ISPROJ': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ICLB': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'CALFILE': fo.readline()[0:12].strip()})
        fo.readline()
        filecio.update({'IPRINT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'NYSKIP': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ILOG': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IPRP': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        # filecio.update({'IPRS': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        fo.readline()
        fo.readline()
        results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
        results = [int(i) for i in results]
        filecio.update({'IPDVAR': results})
        fo.readline()
        results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
        results = [int(i) for i in results]
        filecio.update({'IPDVAB': results})
        fo.readline()
        results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
        results = [int(i) for i in results]
        filecio.update({'IPDVAS': results})
        fo.readline()
        results = (re.findall(r"[^\s\,!?;'\"]+", fo.readline()))
        results = [int(i) for i in results]
        filecio.update({'IPDHRU': results})
        fo.readline()
        filecio.update({'ATMOFILE': fo.readline()[0:12].strip()})
        filecio.update({'IPHR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ISTO': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ISOL': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'I_SUBW': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'SEPTDB': fo.readline()[0:12].strip()})
        filecio.update({'IA_B': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IHUMUS': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ITEMP': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ISNOW': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IMGT': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'IWTR': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        filecio.update({'ICALEN': int(re.findall(r"[^\s\,!?;'\"]+", fo.readline())[0])})
        return filecio


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



