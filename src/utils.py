import datetime
import re


def remove_host_from_url(url):
    host_regex = r'(^https?://)(.*/)'
    return re.sub(host_regex, '', url)

def get_filename_from_datetime(base_url, extension):
    base_url_without_host = remove_host_from_url(base_url)
    return f'data/{base_url_without_host}-{datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}.{extension}'

def save_df_to_csv(df, filename):
    df.to_csv(filename, index=False)

def parse_zonaprop_url(url):
    return url.replace('.html', '')
