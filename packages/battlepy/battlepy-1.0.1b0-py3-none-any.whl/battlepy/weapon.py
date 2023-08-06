from src.battlepy.config import Config
from src.battlepy.quality import Quality

import pandas as pd


class Weapon:
    def __init__(self, n_battles=None, characters=None):
        self.__cfg = Config()
        self.__quality = Quality()
        self.__csv_name = self.__cfg.csv_files['weapon']
        self.__dataframe = self.__cfg.get_table(self.__csv_name)
        self.__dataframe.set_index('class', inplace=True)
        self.__column_names = self.__cfg.options['weapon']['column_names']
        self.__n_battles = n_battles
        self.__characters = characters
        self.__player_dataframe = None
        self.__enemy_dataframe = None
        self.__dataframes = {}
        self.__classes = self.__cfg.options['class']['classes']
        self.__dataframe_quality = self.__quality.get_random_quality_mod(self.__n_battles)
        self.__dataframe_stats = None

    def _dataset(self):
        if self.__characters['player'] is True:
            self.__player_dataframe = self.create_weapon_dataset(prefix='player')
        if self.__characters['enemy'] is True:
            self.__enemy_dataframe = self.create_weapon_dataset(prefix='enemy')
        self.__dataframes.update({'player': self.__player_dataframe, 'enemy': self.__enemy_dataframe})

    def get_weapon_dataset(self, n_battles=None, dataframe=None):
        self.__n_battles = n_battles
        if (self.__characters is None) | (self.__player_dataframe is None) | (self.__enemy_dataframe is None):
            self.__dataframe_stats = dataframe
            self._dataset()
        return self.__dataframes

    def create_weapon_dataset(self, prefix=''):
        """
        Generate weapon, quality and calculates total damage.

        :param prefix: if dataframe will be for player or enemy
        :return: dataframe white all weapon data
        """

        dataframe = pd.DataFrame(columns=self.__column_names)
        dataframe['total_damage'] = [0] * self.__n_battles

        for cls in self.__classes:
            index_weapon = self.__dataframe_stats[prefix].index[
                self.__dataframe_stats[prefix][prefix + '_class'] == cls].tolist()
            df_w = self.__dataframe[self.__dataframe.index == cls].sample(
                n=len(index_weapon), replace=True).reset_index()
            df_q = self.__dataframe_quality.sample(n=len(index_weapon),
                                                   replace=True).reset_index()

            df_w_q = pd.concat([df_w, df_q], axis=1)
            df_w_q['idx'] = index_weapon
            df_w_q.set_index('idx', inplace=True)
            dataframe.update(df_w_q['weapon'])
            dataframe['weapon_mod'].update(pd.Series(df_w_q['mod']))
            dataframe['weapon'].update(df_w_q['weapon'])
            dataframe['total_damage'].update(
                df_w_q['base_dmg'] * df_w_q['mod'])

        dataframe = dataframe.add_prefix(prefix + '_')
        return dataframe
