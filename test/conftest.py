import codecs

import pytest


@pytest.fixture
def html_page():
    # 'utf-8' codec can't decode byte 0xed in position 19806: invalid continuation byte
    with codecs.open('test\\html_page.html', 'r', encoding='latin-1') as f:
        return f.read()
