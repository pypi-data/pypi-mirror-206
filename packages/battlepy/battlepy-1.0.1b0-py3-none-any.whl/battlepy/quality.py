import pandas as pd

from src.battlepy.config import Config


class Quality:

    def __init__(self, n_battles=None):
        self.__n_battles = n_battles
        self.__cfg = Config()
        self.__csv_name = self.__cfg.csv_files['quality']
        self.__dataframe = self.__cfg.get_table(self.__csv_name)
        self.__dataframe = self.__dataframe.set_index('quality')

    @property
    def stats_csv(self):
        return self.__csv_name

    @stats_csv.setter
    def stats_csv(self, name):
        self.__csv_name = name

    @property
    def __df(self):
        return self.__dataframe

    def get_random_quality_mod(self, n):
        df = pd.DataFrame(self.__df.sample(n=n, replace=True), columns=["mod"])
        df.reset_index(drop=True, inplace=True)
        return df
