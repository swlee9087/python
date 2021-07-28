import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Population(object):
    data: [] = list()
    home: [] = list()
    away: object = None
    result_name: str = ''

    def read_data(self):
        df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands=',', index_col=0)
        df.to_csv('./data/202106_202106_연령별인구현황_월간_wo_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간_wo_comma.csv', 'rt', encoding='UTF-8'))
        next(data)
        self.data = list(data)  # 복병ㅋㅋㅋ

    # print([i for i in data])
    # data.div(data['총인구수'], axis=0)
    # del data['총인구수'], data['연령구간인구수']
    # print(self.data)

    def pop_per_dong(self, dong: str) -> []:
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        print([i for i in arr])
        return arr

    """def find_by_dong(self, name: str) -> []:
        home = []
        for i in self.df:
            if name in i[0]:
                home = np.array(i[3:], dtype=str)
        # [home.append(str(j)) for i in self.data if name in i[0] for j in i[3:]]
        # [home(np.array(i[3:], dtype=str) for i in self.data if name in i[0]]
        print(home)

    def find_dong_pd(self):
        name = input('알고 싶은 지역 (읍면동) 입력: ')
        a = self.data.index.str.contains(name)
        df2 = self.data[a]
        # data2.T.plot()

    def find_similar_dong_pd(self, data, data2):
        x = data.sub(data2.iloc[0], axis=1)
        y = np.power(x, 2)
        z = y.sum(axis=1)
        i = z.sort_values().index[:5]
        data.loc[i].T.plot()

    def show_plot(self, name):
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.rc('font', family='Malgun Gothic')
        plt.title(f'{name} 지역의 인구 구조')
        plt.plot()
        plt.show()"""

    def find_home(self, name: str) -> []:  # 인트 바꾸지 마시오
        home = []
        [home.append(int(j)) for i in self.data if name in i[0] for j in i[3:]]
        self.home = home

    def array_to_list(self, arr) -> []:
        return arr.to_list()

    def list_to_array(self, ls: []) -> object:
        return np.array(ls)

    def show_plot_home(self, arr: object, name: str):
        plt.title(f'{name} 지역의 인구구조')
        plt.plot(arr)
        plt.show()

    def find_similar_area(self, name: str):
        mn = 1  # 최소값
        result = 0
        home = []  # 정의되었던 self.home 을 local variable home 으로 변경해야
        for i in self.data:
            if name in i[0]:
                home = np.array(i[3:], dtype=int) / int(i[2])
                # np.array(i[3:], dtype=int)/int(i[2]) 식은 전체 연령별 인구수의 합에서 각 연령층의 비율
        self.home = home  # 기존의 홈지역만 출력하는 것이 아니라, 유사도가 있는 두 지역을 출력

        for i in self.data:
            away = np.array(i[3:], dtype=int) / int(i[2])
            s = np.sum((home - away) ** 2)  # x self.home
            if s < mn and name not in i[0]:  # s < 1
                mn = s
                self.result_name = i[0]
                result = away
        self.away = result

    def show_plot_similar_two_cities(self, name: str, home: [], away: []):
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title(f'{name} 지역과 가장 비슷한 인구 구조를 가진 지역')
        plt.plot(home, label=name)
        plt.plot(away, label=self.result_name)
        plt.legend()
        plt.show()


if __name__ == '__main__':
    pop = Population()
    pop.read_data()
    # name = input('조사 대상 지역 (읍면동) 입력: ')
    # pop.pop_per_dong()
    # pop.find_by_dong(input(f'알고 싶은 지역 (읍면동) 입력: '))
    # pop.show_plot(pop.pop_per_dong('역삼1동'))
    # pop.show_plot(pop.find_by_dong(input(f'알고 싶은 지역 (읍면동) 입력: ')))
    # pop.find_dong_pd()
    # pop.show_plot(pop.find_dong_pd())
    # pop.find_similar_dong_pd(pop.find_dong_pd())
    pop.find_home('구래동')
    pop.home = pop.list_to_array(pop.home)
    # pop.home = arr_home
    # print(f' pop.home : \n{pop.home}')
    #    pop.show_plot_home(arr_home, '보광동')
    pop.find_similar_area('구래동')
    pop.show_plot_similar_two_cities('구래동', pop.home, pop.away)
