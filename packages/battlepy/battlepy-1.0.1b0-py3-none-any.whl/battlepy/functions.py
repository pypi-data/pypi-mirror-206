"""
 General functions, helpers, etc.
"""
import os
import uuid
import datetime
import sys

import pandas as pd

from src.battlepy.config import Config


def little_hash():
    """
    Return as little hash like 'C263978A'. This hash will be in the last part
    of file name before extension (csv).
    Example: battle-2023-03-24-C263978A.csv

    :return: HASH UUID4
    """
    string_length = 8
    random_string = uuid.uuid4().hex
    random_string = random_string.upper()[0:string_length]
    return random_string


def exist(folder):
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except IOError as e:
            print(f"Error creating directory: {folder}\n Exception: {e}")


def check_df_isvalid(df):
    if not isinstance(df, pd.DataFrame):
        raise Exception(f"Invalid Dataframe:{df}")
    return True


def filter_df_by_column(df, column_value):
    for c, v in column_value.items():
        if v in df[c].values:
            return df.loc[df[c] == v]


def get_sample(size, dataframe, column_filter=None):
    """ Return sample from dataframe.

        :param size: Size of sample (replace=True).
        :param dataframe: Dataframe to sample.
        :param column_filter: Column to filter. Default None.
    """
    check_df_isvalid(dataframe)
    check_positive_number(size)
    df = pd.DataFrame()
    if column_filter is not None:
        for x, y in column_filter.items():
            df = filter_df_by_column(dataframe, {x: y})
            if df is None:
                df = dataframe
    return df.sample(n=size, replace=True)


def check_class_name(self, name):
    if not isinstance(name, str) or name not in self._class_table['class_name'].tolist():
        print(f"Class {name} not valid!")
        exit(0)


def check_positive_number(n):
    if not isinstance(n, int) or n < 1:
        raise Exception(f"Value not valid or below 1. Value:{n}")
    return True


def create_output_file(output_file=None, compression=None):
    """
    This method creates a file for output the dataframe in csv format.

    :param output_file: Name of the filename
    :param compression: Set the output compression of the csv file
    :return: name file if successful
    """
    cfg = Config()

    if not os.path.exists(cfg.options['config']['output_dir']):
        os.makedirs(cfg.options['config']['output_dir'])

    if output_file is None:
        date_obj = datetime.datetime.now()
        output_file = '{}battle-{}-{}.csv'\
            .format(cfg.options['config']['output_dir'], date_obj.strftime('%Y%m%d%H%M%S'),
                    little_hash())
    else:
        output_file = cfg.options['config']['output_dir'] + cfg.options['config']['output_dir'] + output_file
    try:
        # Let's try to write the file in output directory...
        dataframe = pd.DataFrame()
        dataframe.to_csv(output_file, sep=";")
        os.remove(output_file)
    except IOError as error:
        sys.exit('{}'.format(error))
    return dict(method=compression, archive_name=output_file)
