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
        n_ = 0

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')  # BS constrc 안에 urlopen() 함수
        _ = 1
        artists = soup.find_all(name='p', attrs={'class': 'artist'})
        titles = soup.find_all(name='p', attrs={'class': 'title'})
        print(f'list size is {len(artists)}')

        for i, j in enumerate(artists):  # for문으로 한줄
            print(f"* Rank {str(_)}  Artist : {j.find('a').text} | Title : {titles[i].find('a').text}")
            _ += 1


def main():
    # 20210720
    # 16
    Bugsmusic(f'https://music.bugs.co.kr/chart/track/realtime/total?'
              f'chartdate={"20210721"}&charthour={"09"}').scrap()


if __name__ == '__main__':
    main()
