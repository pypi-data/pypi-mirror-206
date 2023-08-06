"""
basecharacter.py
Base class for character type classes
"""

from src.battlepy.stats import Stats


class Character:
    def __init__(self, n_battles=None, characters=None):
        self.__n_battles = n_battles
        self.__characters = characters
        self.__class_name = None
        self.__typeid = None
        self.__description = None
        self.__player_dataframe = None
        self.__enemy_dataframe = None
        self.__dataframes = {}
        self.__stats = Stats(n_battles=self.__n_battles, characters=self.__characters)

    def _dataset(self):
        if self.__characters['player'] is True:
            self.__player_dataframe = self.__stats.create_stats_dataset(prefix='player')
        if self.__characters['enemy'] is True:
            self.__enemy_dataframe = self.__stats.create_stats_dataset(prefix='enemy')
        self.__dataframes.update({'player': self.__player_dataframe, 'enemy': self.__enemy_dataframe})

    def get_character_dataset(self, n_battles):
        self.__n_battles = n_battles
        if (self.__characters is None) | (self.__player_dataframe is None) | (self.__enemy_dataframe is None):
            self._dataset()
        return self.__dataframes
