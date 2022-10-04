from src.utils import remove_host_from_url


def test_remove_host_from_url():
    url = 'https://www.google.com/test'
    assert remove_host_from_url(url) == 'test'
