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
        artists = soup.find_all(name=self.tag_name, attrs={'class': })  # artist
        titles = soup.find_all(name=self.tag_name, attrs={'class': })  # title

        for i, j in zip(artists, titles):
            print(f"* Rank {str(_)} Artists : {j.find('a').text} | Title : {titles[i].find('a').text}")
            _ += 1


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
        menu = print_menu(['exit', 'Bugs URL', 'Melon URL', 'output',
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
        elif menu == 3:  # crawling output
            menu1 = print_menu(['Bugsmusic','Melon'])
            if menu1 ==0:
                mr.tag_name = 'p'
                mr.class_name.append('artist')
                mr.class_name.append('title')
            elif menu1 ==1:
                mr.tag_name = 'div'
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
            mr.get_ranking()

            '''for i,j in artists:
                print(i)
                for j in'''
            # pass
        elif menu == 4:  # print dict
            mr.insert_dict()

        elif menu == 5:  # dc to df
            mr.dict_to_dataframe()

        elif menu == 6:  # df to csv
            mr.df_to_csv()


if __name__ == '__main__':
    main()
