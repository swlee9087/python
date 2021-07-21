from bs4 import BeautifulSoup
from urllib.request import urlopen


class Melon(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')

        ls = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})  # artist
        ls2 = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})  # title
        n_artists = 0
        n_title = 0
        print(f'\nlist size is {len(ls)}')

        for i in ls:
            n_artists += 1
            print("* Rank " + str(n_artists) + "Artists : " + i.find('a').text)
            print("Title : " + ls2[n_title].find('a').text)
            n_title += 1

def main():
    Melon(f'https://www.melon.com/chart/index.htm?dayTime=2021072109').scrap()


if __name__ == '__main__':
    main()
