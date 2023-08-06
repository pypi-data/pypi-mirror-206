import numpy as np
import pandas as pd
from src.battlepy.config import Config
from src.battlepy.quality import Quality


class Armor:

    def __init__(self, n_battles=None, characters=None):
        self.__cfg = Config()
        self.__quality = Quality()
        self.__csv_name = self.__cfg.csv_files['armor']
        self.__dataframe = self.__cfg.get_table(self.__csv_name)
        self.__column_names = self.__cfg.options['armor']['column_names']
        self.__n_battles = n_battles
        self.__characters = characters
        self.__player_dataframe = None
        self.__enemy_dataframe = None
        self.__dataframes = {}

    @property
    def csv_file(self):
        return self.__csv_name

    @csv_file.setter
    def csv_file(self, filename):
        self.__csv_name = filename

    def __create_armor_dataset(self, prefix=''):
        dataframe = pd.DataFrame(self.__dataframe.sample(n=self.__n_battles, replace=True),
                                 columns=self.__column_names)
        df_sample_quality = self.__quality.get_random_quality_mod(self.__n_battles)

        dataframe.reset_index(drop=True, inplace=True)
        dataframe['total_armor'] = [0] * self.__n_battles
        for col in self.__column_names:
            if col == "total_armor":
                continue
            dataframe[col] = df_sample_quality['mod'].values * dataframe[col]
            dataframe[col + '_mod'] = df_sample_quality
            dataframe['total_armor'] += dataframe[col]

        dataframe = dataframe.add_prefix(prefix+'_')
        return dataframe

    def __dataset(self):
        if self.__characters['player'] is True:
            self.__player_dataframe = self.__create_armor_dataset(prefix='player')
        if self.__characters['enemy'] is True:
            self.__enemy_dataframe = self.__create_armor_dataset(prefix='enemy')
        self.__dataframes.update({'player': self.__player_dataframe, 'enemy': self.__enemy_dataframe})

    def get_armor_dataset(self, n_battles=None):
        self.__n_battles = n_battles
        if (self.__characters is None) | (self.__player_dataframe is None) | (self.__enemy_dataframe is None):
            self.__dataset()
        return self.__dataframes
