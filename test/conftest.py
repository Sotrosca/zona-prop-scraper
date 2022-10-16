import codecs

import pandas as pd
import pytest


@pytest.fixture
def html_page():
    # 'utf-8' codec can't decode byte 0xed in position 19806: invalid continuation byte
    with codecs.open('test\\mock\\html_page.html', 'r', encoding='latin-1') as f:
        return f.read()

@pytest.fixture
def df_estates():
    return pd.read_csv('test\\mock\\df_estates.csv')
