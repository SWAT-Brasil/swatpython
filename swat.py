import os
import logging
import shutil
import subprocess
import platform
from swatpython.operationalsystem import OperationalSystem
from swatpython.swatversion import SWATVersion
from swatpython.swat2012rev670.swat2012rev670 import SWAT2012rev670

logger = logging.getLogger(__name__)


class SWAT(object):
    """
    Swat is a python interface for SWAT. It is based in modules, so each SWAT version has a different
    module. Using modules allows the interface to be used with different swat versions.

    ...

    Attributes
    ----------
    says_str : str
        a formatted string to print out what the animal says
    name : str
        the name of the animal
    sound : str
        the sound that the animal makes
    num_legs : int
        the number of legs the animal has (default 4)

    Methods
    -------
    says(sound=None)
        Prints the animals name and what sound it makes
    """

    def __init__(self, version):
        """ Initialize SWAT class. Use SWAT.SWATVersion and SWAT.OS enuns.

        Parameters
        ----------
        version : SWATVersion enun
            SWAT version to use
        operational_system : OS enun
            Operational System (WINDOWS or LINUX)
        """
        self.version = version
        self.operational_system = platform.system()
        self.architecture = platform.architecture()[0]
        self.current_path = os.path.dirname(os.path.abspath(__file__))
        self.working_folder_path = None
        self.project_path = None
        self.executable_path = None
        self.wrapper = None
        self.executable_filename = None
        self.project_folder_path = None
        self.async_process = None

        # Select the right class for the swat version
        logger.info("Detected OS: " + self.operational_system + " " + self.architecture)
        if version == SWATVersion.SWAT2012REV670:
            if self.operational_system == OperationalSystem.LINUX.value:
                self.wrapper = SWAT2012rev670(OperationalSystem.LINUX)
            elif self.operational_system == OperationalSystem.WINDOWS.value:
                self.wrapper = SWAT2012rev670(OperationalSystem.WINDOWS)

        logger.info("Using SWATPython module: " + self.wrapper.get_version())

        # try to find the correct swat executable
        if self.architecture == "64bit":
            self.set_executable(self.wrapper.get_linux_64bits())
        else:
            logger.error("Executable for architecture not found: " + self.architecture)
            raise ValueError("Executable for architecture not found: " + self.architecture)

    def set_executable(self, path):
        """ set the path to the SWAT executable. 

        Usually this is called internally, but if you have some custom SWAT executable
        you should set it here.

        Parameters
        ----------
        path : path to SWAT executable
        """
        if not os.path.isfile(path):
            logger.error("SWAT executable nof found: " + path)
            raise ValueError("SWAT executable file not found: " + path)
        self.executable_path = path
        self.executable_filename = os.path.basename(path)
        logger.debug("SWAT executable found: " + path)

    def set_project_folder(self, path):
        """ Set the project folder

        Parameters
        ----------
        path : path to folder that should be already created
        """
        if not os.path.isdir(path):
            logger.error("Project folder nof found: " + path)
            raise ValueError("Project folder not found: " + path)
        self.project_folder_path = path
        logger.info("Project folder found: " + path)

    def load_project(self, path):
        """ Loads project

        Parameters
        ----------
        path : path to project
        """
        if not os.path.isdir(path):
            logger.error("Project folder nof found: " + path)
            raise ValueError("Project folder not found: " + path)
        self.project_path = path
        logger.debug("Project folder found: " + path)

        # temp folder should already be defined
        if self.working_folder_path is None:
            logger.error("Working folder not defined.You should set temp folder first")
            raise ValueError("Working folder not defined. You should set temp folder first")

        # copying project to temp folder
        src_files = os.listdir(self.project_path)
        logger.debug("Copying files to temp folder: " + self.project_path)
        for file_name in src_files:
            full_file_name = os.path.join(self.project_path, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, self.working_folder_path)

        # copying SWAT executable
        if os.path.isfile(self.executable_path):
            logger.debug("Copying SWAT executable to temp folder: " + self.executable_path)
            shutil.copy(self.executable_path, self.working_folder_path)
        else:
            logger.error("SWAT executable not found: " + self.executable_path)
            raise ValueError("SWAT executable not found." + self.executable_path)

    def set_working_folder(self, path):
        """ Define the temp folder

        Parameters
        ----------
        path : path to folder that should be already created
        """
        if not os.path.isdir(path):
            logger.error("Working folder nof found: " + path)
            raise ValueError("Working folder not found: " + path)
        self.working_folder_path = path
        logger.debug("Working folder found: " + path)

    def write(self, file, field, value):
        """ escreve em arquivo do swat """

    def run(self):
        """ executa o swat """
        logger.debug("Running SWAT in folder: " + self.project_folder_path)
        self.wrapper.run(self.project_folder_path)

    def async_run(self):
        """ executa o swat """
        logger.debug("Running SWAT in folder: " + self.project_folder_path)
        self.async_process = self.wrapper.async_run(self.project_folder_path)

    def async_is_running(self) -> bool:
        if self.async_process is None:
            return False
        elif self.async_process.poll() is None:
            return True
        else:
            return False

    def async_return_code(self) -> int:
        return self.async_process.poll()

    def sufi2_run_async_kill(self):
        if self.sufi2_async_is_running():
            logger.debug("Found a async process running. Killing it!")
            self.async_process.kill()

    def sufi2_async_wait(self):
        logger.debug("Waiting async")
        self.async_process.wait()

        # run executable + self.ex
#        if self.operational_system == OperationalSystem.LINUX.value:
#            logger.debug("Running SWAT in linux " + self.executable_filename + " in " + self.working_folder_path)
#            process = subprocess.Popen(os.path.join(self.working_folder_path, self.executable_filename),
#                                       cwd=self.working_folder_path)
#            # show output
#            process.communicate()[0]
#            swat_return_code = process.returncode
#        elif self.operational_system == OperationalSystem.WINDOWS.value:
#            logger.error("run method not implement in WINDOWS")
#            raise ValueError("run method not implement in WINDOWS")
#        else:
#            logger.error("Unknown operational system" + self.operational_system)
#            raise ValueError("Unknown operational system" + self.operational_system)

    def read_precipitation_daily(self, filename):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        path = os.path.join(self.project_folder_path, filename)
        logger.debug("Reading file: " + path)
        return self.wrapper.read_precipitation_daily(path)

    def write_precipitation_daily(self, filename, info, dataframe):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        path = os.path.join(self.project_folder_path, filename)
        logger.debug("Writing file: " + path)
        return self.wrapper.write_precipitation_daily(path,info,dataframe)

    def read_precipitation_sub_daily(self, filename):
        """Prints what the animals name is and what sound it makes.

        If the argument `sound` isn't passed in, the default Animal
        sound is used.

        Parameters
        ----------
        sound : str, optional
            The sound the animal makes (default is None)

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
        path = os.path.join(self.project_folder_path, filename)
        logger.debug("Reading file: " + path)
        return self.wrapper.read_precipitation_sub_daily(path)

    def write_precipitation_sub_daily(self, filename, info, dataframe):
        path = os.path.join(self.project_folder_path, filename)
        logger.debug("Writing file: " + path)
        return self.wrapper.write_precipitation_sub_daily(path,info,dataframe)

    def read_output_rch(self, filename):
        path = os.path.join(self.project_folder_path, filename)
        logger.debug("Reading file: " + path)
        return self.wrapper.read_output_rch(path)
