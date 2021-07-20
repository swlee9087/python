import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

"""지원 parser종류
html.parser - 빠르나 유연하지 못한. 그래서 단순 html에만.
lxml - 매우 빠르고 유연함.
xml - xml파일에만.
html5lib - 복잡구조의 html에 대해 사용.
"""


class Bugsmusic(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')  # BS constrc 안에 urlopen() 함수
        n_artists = 0
        n_title = 0
        ls = soup.find_all(name='p', attrs={'class': 'artist'})
        ls2 = soup.find_all(name='p', attrs={'class': 'title'})
        print(f'list size is {len(ls)}')

        for i in ls:  # for문으로 한줄
            n_artists += 1
            print("Rank " + str(n_artists) + " Artists : " + i.find('a').text)
            n_title += 1
            print("Rank " + str(n_title) + " Title : " + ls2[n_title].find('a').text)


def main():
    # 20210720
    # 16
    # Bugsmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
    # f'chartdate={input("Date : ")}&charthour={input("Hour : ")}').scrap()
    Bugsmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
              f'chartdate={"20210720"}&charthour={"16"}').scrap()


if __name__ == '__main__':
    main()
