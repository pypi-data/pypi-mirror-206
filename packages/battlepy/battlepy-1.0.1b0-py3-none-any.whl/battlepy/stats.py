"""
This Class load and generate random class/stats for enemy/player
"""

import pandas as pd
from numpy import random as np_random

from src.battlepy.config import Config


class Stats:
    __cfg = Config()

    def __init__(self, n_battles=None, characters=None):
        self.__dir = self.__cfg.dir
        self.__csv_name = self.__cfg.csv_files['stats']
        self.__dataframe = self.__cfg.get_table(self.__csv_name)
        self.__columns_name = self.__cfg.options['stats']['column_names']
        self.__n_battles = n_battles
        self.__characters = characters

    def get_stats_by_class(self, cls, attribute=None):
        if cls not in list(self.__dataframe.index):
            raise Exception(f"Class not found in csv stats file.\nClass:{cls}")

        if (attribute is not None) & (attribute not in list(self.__dataframe.columns.values)):
            raise Exception(f"Attribute not found in csv stats file.\nAttribute: {attribute}")

        if attribute is not None:
            return self.__dataframe.loc[cls][attribute]
        else:
            return self.__dataframe.loc[cls]

    @property
    def get_all_columns(self):
        return self.__columns_name

    @property
    def stats_csv(self):
        return self.__csv_name

    @stats_csv.setter
    def stats_csv(self, name):
        self.__csv_name = name

    @property
    def stats_dir(self):
        return self.__dir

    @stats_dir.setter
    def stats_dir(self, folder):
        self.__dir = folder

    @property
    def df(self):
        return self.__dataframe

    def get_random_class(self, n):
        return pd.DataFrame(self.df.sample(n=n, replace=True), columns=list(self.get_all_columns))

    def get_random_level(self):
        return np_random.randint(1, 101, size=self.__n_battles)

    def create_stats_dataset(self, prefix=''):
        """
        Generate random class/stats for player/enemy.

        :param prefix: if dataframe will be generated for player or enemy
        :return: dataframe
        """

        dataframe = self.get_random_class(self.__n_battles)
        dataframe['level'] = self.get_random_level()
        dataframe.reset_index(drop=True, inplace=True)
        dataframe["str"] = dataframe['str'] * dataframe["level"]
        dataframe["agi"] = dataframe["agi"] * dataframe["level"]
        dataframe["int"] = dataframe["int"] * dataframe["level"]
        dataframe["con"] = dataframe["con"] * dataframe["level"]
        dataframe["hp"] = dataframe['level'] * dataframe["con"]
        dataframe["current_hp"] = dataframe['hp']
        dataframe = dataframe.add_prefix(prefix+'_')
        return dataframe
