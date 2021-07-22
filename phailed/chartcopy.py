from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen
from urllib.request import Request


class MusicRanking(object):
    domain = ''  # string
    query_string = ''
    html = ''  # url 분리
    headers = {'User-Agent': 'Mozilla/5.0'}  # doesn't change
    tag_name = ''
    fname = ''  # file name
    class_name = []  # variety of class names possible
    artists = []
    titles = []
    dict = {}
    df = None  # matrix

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        print(f'crawling html : {self.html}')

    def get_ranking(self):
        soup = BeautifulSoup(self.html, 'lxml')
        _ = 0
        l1 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[0]})  # artist
        l2 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[1]})  # title

        for i, j in zip(l1, l2):
            _ += 1
            print(f"{self.fname} Rank {_} Artists : {i.find('a').text} | Title : {j.find('a').text}")
            self.artists.append(i.find('a').text)
            self.titles.append(j.find('a').text)


def print_menu(ls):
    t = ''
    for i, j in enumerate(ls):
        t += str(i) + '-' + j + '\t'
    return int(input(t))


def main():
    mr = MusicRanking()
    while 1:
        '''print('0-exit 1-input 2-output 3-print dict 4-dict to Df 5-Df to csv')
        menu = input('Choose one: ')'''
        n_ = 0
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Bugs output', 'Melon output',
                           'Print Dict', 'Dict to Df', 'Df to CSV'])
        if menu == 0:
            break
        elif menu == 1:  # bugs url
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=14'
            mr.set_html()

        elif menu == 2:  # melon url
            mr.domain = 'https://www.melon.com/chart/index.htm?dayTime='
            mr.query_string = '2021072114'
            mr.set_html()

        elif menu == 3:  # crawling output bugs
            mr.tag_name = 'p'
            mr.class_name.append('artist')
            mr.class_name.append('title')
            mr.get_ranking()

        elif menu == 4:  # output melon
            mr.tag_name = 'div'
            mr.class_name.append('ellipsis rank02')
            mr.class_name.append('ellipsis rank01')
            mr.get_ranking()

            '''for i,j in artists:
                print(i)
                for j in'''
            # pass


if __name__ == '__main__':
    main()
