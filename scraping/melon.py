from urllib.request import Request

from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}
        n_ = 0

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers=self.headers)), 'lxml')# 한줄로 줄임
        _ = 1
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})  # artist
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})  # title
        print(f'\nlist size is {len(artists)}')

        for i, j in enumerate(artists):
            print(f"* Rank {str(_)} Artists : {j.find('a').text} | Title : {titles[i].find('a').text}")
            _ += 1


def main():
    Melon(f'https://www.melon.com/chart/index.htm?dayTime=2021072109').scrap()


if __name__ == '__main__':
    main()
