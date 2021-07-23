from bs4 import BeautifulSoup
import requests
import pandas as pd
# 주현씨

class Music(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    tag_name = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        #print(f'Crawling HTML : {self.html}')

    def get_ranking(self):
        _ = 0
        soup = BeautifulSoup(self.html, 'lxml')
        all1 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[0]})
        all2 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[1]})

        for i, j in zip(all1, all2):
            _+=1
            print(f'{self.fname} : {_}위. {i.find("a").text}  - {j.find("a").text}')
            self.artists.append(i.find("a").text)
            self.titles.append(j.find("a").text)

    def insert_dict(self):
        '''
        #방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        #방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i]= j
        #방법 3
        for i,j in enumerate(self.titles):
            self.dict[j] = self.artists[i]
        '''

        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        print(self.dict)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        print(self.df)


    def df_to_csv(self):
        path = f'./data/{self.fname}_chart.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN', encoding="utf-8-sig")


def print_menu(ls):
    t = ''
    for i, j in enumerate(ls):
        t += str(i) + '. ' + j + '\t'
    return int(input(t))




def main():
    mr = Music()
    while 1:
        menu = print_menu(['Exit', 'Input time', 'Output', 'Print dict', 'dict to Dataframe', 'Df to csv'])
        if menu == 0:
            break
        elif menu == 1:  # input
            m1 = print_menu(['melon', 'bugs'])
            if m1 == 0:
                mr.fname = 'Melon'
                mr.domain = 'https://www.melon.com/chart/index.htm?dayTime='
                mr.query_string = '2021072015'
            elif m1 == 1:
                mr.fname = 'Bugs'
                mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
                mr.query_string = 'chartdate=20210721&charthour=10'
            mr.set_html()
        elif menu == 2:  # out
            if m1 == 0:
                mr.tag_name = 'div'
                mr.class_name.append('ellipsis rank02')
                mr.class_name.append('ellipsis rank01')
            elif m1 == 1:
                mr.tag_name = 'p'
                mr.class_name.append('artist')
                mr.class_name.append('title')
            mr.get_ranking()
        elif menu == 3:  # print
            mr.insert_dict()
        elif menu == 4:  # dict to df
            mr.dic_to_dataframe()
        elif menu == 5:  # df to csv
            mr.df_to_csv()


if __name__ == '__main__':
    main()