import os
import shutil

from src.utils import remove_host_from_url, save_df_to_csv


def teardown_function(function):
    if os.path.exists('data'):
        shutil.rmtree('data')

def test_remove_host_from_url():
    url = 'https://www.google.com/test'
    assert remove_host_from_url(url) == 'test'


def test_save_df_to_csv(df_estates):
    filename = 'data/test.csv'
    save_df_to_csv(df_estates, filename)
    assert os.path.exists(filename)
