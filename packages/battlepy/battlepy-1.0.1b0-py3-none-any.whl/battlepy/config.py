"""
Config class for getting config about stats, items, etc.
"""
import json
from pathlib import Path
import pandas as pd


class Config:
    def __init__(self):
        """
        Default location for config csv files
        """
        self.__base_dir = Path(__file__).parent
        self.__dir = (self.__base_dir / 'config').resolve()
        self.__file = (self.__dir / 'config.json').resolve()
        self.__options = self.load_config(self.__file)
        self.__csv_files = {k: v for elem in self.options['config']['csv_files'] for k, v in elem.items()}

    @property
    def options(self):
        return self.__options

    def load_config(self, file=None):
        if file is not None:
            f = file
        else:
            f = self.__file
        try:
            with open(f) as config_file:
                return json.load(config_file)
        except IOError as e:
            raise Exception(f"Check if {f} exist, can be read or valid JSON.\n{e}")

    def get_table(self, csv_file):
        """
            Load csv into a dataframe.

            :return: Dataframe from csv file
            """
        try:
            return pd.read_csv((self.dir / csv_file).resolve())
        except IOError as error:
            raise Exception(f"Check if file {csv_file}.csv can be open, read or exist.\n"
                            f"Check if file is a valid csv format.\n"
                            f"{error}")

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, path):
        try:
            if Path.exists(path):
                self.__dir = path
        except IOError as e:
            raise Exception(f"Check if path {path} exist, readable or have permission.\n{e}")

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, path):
        try:
            if Path.exists(path):
                self.__file = path
        except IOError as e:
            raise Exception(f"Check if path {path} exist, readable or have permission.\n{e}")

    @property
    def csv_files(self):
        """ Return dictionary {'file_name' : PATH}"""
        return self.__csv_files

#    @csv_files.setter
    def ass(self, d):
        """ Update/Add csv files to load into dataframes"""
        if (d is not None) & (isinstance(d, list)):
            if not isinstance(self.__csv_files, dict) & (self.__csv_files is None):
                self.__csv_files = {}
            self.__csv_files.update(d)
