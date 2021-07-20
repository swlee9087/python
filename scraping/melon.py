from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artists = 0
        n_titles = 0
        artists = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})  # artist
        titles = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})  # title
        print(f'\nlist size is {len(artists)}')

        for artist in artists:
            n_artists += 1
            print("Rank " + str(n_artists) + "Artists : " + artist.find('a').text)
        for title in titles:
            n_titles += 1
            print("Rank " + str(n_titles) + "Title : " + title.find('a').text)


def main():
    Melon(f'https://www.melon.com/chart/index.htm?'
          f'dayTime={"2021072017"}').scrap()


if __name__ == '__main__':
    main()
