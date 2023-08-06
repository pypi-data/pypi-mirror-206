"""
 Battle Class
"""
import pandas as pd
import numpy as np

import src.battlepy.functions as functions
from src.battlepy.character import Character
from src.battlepy.config import Config
from src.battlepy.armor import Armor
from src.battlepy.weapon import Weapon


class Battle:

    def __init__(self):
        self.__cfg = Config()
        self.__characters = {'player': True, 'enemy': True}
        self.__battle_type = 0
        self.__n_battles = self.__cfg.options['battle']['n_battles']
        self.__character = Character(n_battles=self.__n_battles, characters=self.__characters)
        self.__armor = Armor(n_battles=self.__n_battles, characters=self.__characters)
        self.__weapon = Weapon(n_battles=self.__n_battles, characters=self.__characters)
        self.__dataframes = []
        self.__zip = False

    @property
    def zip_dataframe(self):
        return self.__zip

    @zip_dataframe.setter
    def zip_dataframe(self, b):
        if not isinstance(b, bool):
            raise Exception(f"zip_dataframe need to be boolean, not{type(b)}")
        self.__zip = b

    @property
    def player(self):
        return self.__characters['player']

    @player.setter
    def player(self, b):
        if not isinstance(b, bool):
            raise Exception(f"Incorrect type setting player: Need to be bool not '{b}' - {type(b)}")
        self.__characters['player'] = b

    @property
    def enemy(self):
        return self.__characters['enemy']

    @enemy.setter
    def enemy(self, b):
        if not isinstance(b, bool):
            raise Exception(f"Incorrect type setting enemy: Need to be bool not '{b}' - {type(b)}")
        self.__characters['enemy'] = b

    @property
    def n_battles(self):
        return self.__n_battles

    @n_battles.setter
    def n_battles(self, n):
        if functions.check_positive_number(n):
            self.__n_battles = n
            self.__character = Character(n_battles=self.__n_battles, characters=self.__characters)
            self.__armor = Armor(n_battles=self.__n_battles, characters=self.__characters)

    def __concat_all_df(self):
        dataframe = None
        for df in self.__dataframes:
            dataframe = pd.concat([dataframe, df['player'], df['enemy']], axis=1)
        return dataframe

    def start(self):
        self.__dataframes.append(self.__character.get_character_dataset(self.__n_battles))
        self.__dataframes.append(self.__armor.get_armor_dataset(self.__n_battles))
        self.__dataframes.append(self.__weapon.get_weapon_dataset(self.__n_battles, dataframe=self.__dataframes[0]))
        df = self.__do_battle(self.__concat_all_df())
        filename = functions.create_output_file()

        if self.__zip:
            df.to_csv(filename['archive_name'] + '.zip', sep=";", index=False,
                      compression={'method': "zip"})
        else:

            df.to_csv(filename['archive_name'], sep=";", index=False)

        print(f"Number of battles: {self.n_battles}\n"
              f"Player: {self.player}\n"
              f"Enemy: {self.enemy}\n"
              )

    def __do_battle(self, dataframe):
        """
        Main method to calculates the battle results for player/enemy
        :param dataframe: dataframe with all data (player /enemy)
        :return: dataframe with all results from battles
        """
        dataframe['player_effective_dmg'] = \
            dataframe['player_total_damage'] - dataframe['enemy_total_armor']

        dataframe['enemy_effective_dmg'] = \
            dataframe['enemy_total_damage'] - dataframe['player_total_armor']

        dataframe.loc[dataframe['player_effective_dmg'] < 0, 'player_effective_dmg'] = 0
        dataframe.loc[dataframe['enemy_effective_dmg'] < 0, 'enemy_effective_dmg'] = 0

        dataframe.loc[
            (dataframe['enemy_effective_dmg'] == 0)
            & (dataframe['player_effective_dmg'] > 0),
            'enemy_current_hp'] = 0

        dataframe.loc[(dataframe['player_effective_dmg'] == 0)
                      & (dataframe['enemy_effective_dmg'] > 0),
                      'player_current_hp'] = 0

        dataframe.loc[
            (dataframe['enemy_effective_dmg'] > 0)
            & (dataframe['player_effective_dmg'] > 0),
            'player_round'] = \
            np.ceil(dataframe['player_current_hp'] / dataframe['enemy_effective_dmg'])

        dataframe.loc[(dataframe['enemy_effective_dmg'] > 0)
                      & (dataframe['player_effective_dmg'] > 0),
                      'enemy_round'] = \
            np.ceil(dataframe['enemy_current_hp']
                    / dataframe['player_effective_dmg'])

        dataframe = dataframe.fillna(0)

        dataframe[['player_round', 'enemy_round']].astype('int32')

        dataframe['round'] = dataframe[['player_round', 'enemy_round']].min(axis=1)

        dataframe.loc[
            (dataframe['enemy_round'] == dataframe['round'])
            & (dataframe['round'] > 0), 'enemy_current_hp'] = 0

        dataframe.loc[
            (dataframe['enemy_round'] == dataframe['round'])
            & (dataframe['round'] > 0), 'player_current_hp'] = \
            dataframe['player_current_hp'] \
            - (dataframe['enemy_effective_dmg'] * dataframe['round']) \
            + dataframe['enemy_effective_dmg']

        dataframe.loc[(dataframe['player_round'] == dataframe['round'])
                      & (dataframe['round'] > 0), 'player_current_hp'] = 0

        dataframe.loc[(dataframe['player_round'] == dataframe['round'])
                      & (dataframe['round'] > 0),
                      'enemy_current_hp'] = \
            dataframe['enemy_current_hp'] - \
            (dataframe['player_effective_dmg'] * dataframe['round']) \
            + dataframe['player_effective_dmg']

        return dataframe
