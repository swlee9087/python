from bs4 import BeautifulSoup
import pandas as pd
import requests
from urllib.request import urlopen
from urllib.request import Request

from common.menu import print_menu
from scraping.bugsmusic import Bugsmusic
from scraping.melon import Melon
from scraping.models.dataset import Dataset
from scraping.models.service import Service
from scraping.views import view


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
    bugs = Bugsmusic()
    melon = Melon()


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

    def insert_dict(self):
        # for i in range(0, len(self.tag_name)):
        #    self.dict[self.titles[i]] = self.artists[i]
        # for i, j in zip(self.titles, self.artists):
        #    self.dict[i] = j
        for i, j in enumerate(self.titles):
            self.dict[j] = self.artists[i]
        print(dict)

    def dict_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)

    def df_to_csv(self):
        path = f'./data/{self.fname}.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN')  # not typo


def main():
    mr = MusicRanking()
    while 1:
        n_ = 0
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'Output',
                           'Print Dict', 'Dict to Df', 'Df to CSV', 'Read from CSV'])
        if menu == 0:
            break
        elif menu == 1:  # bugs url to html
            mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
            mr.query_string = 'chartdate=20210721&charthour=14'
            mr.set_html()

        elif menu == 2:  # melon url to html
            mr.domain = 'https://www.melon.com/chart/index.htm?dayTime='
            mr.query_string = '2021072114'
            mr.set_html()

        elif menu == 3:  # crawling output

            for i, j in zip(, melon):
                if mr.tag_name = 'p'
                mr.class_name.append('artist')
                mr.class_name.append('title')

                mr.tag_name = 'div'
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
                mr.get_ranking()

        elif menu == 4:  # print dict
            mr.insert_dict()

        elif menu == 5:  # dc to df
            mr.dict_to_dataframe()

        elif menu == 6:  # df to csv
            mr.df_to_csv()

        elif menu == 7:  # read from csv
            view.modeling('','')


if __name__ == '__main__':
    main()
