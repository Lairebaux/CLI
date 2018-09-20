import click
from urllib.request import urlopen

import re


def get_page_url(url):
    return urlopen(f"http://{url}").read().decode("utf-8")

def extract_links(page):
    img_regex = re.compile("<img[^>]+src=['\"](.*?)['\"]",
                           re.IGNORECASE)
    return img_regex.findall(page)


@click.command()
@click.argument("url")
def run(url):
    target = get_page_url(url)
    links = extract_links(target)
    for link in links:
        print(link)

if __name__ == '__main__':
    run()

