import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager, rc
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/H2GTRE.ttf').get_name())


class Population(object):
    data: [] = list()
    home: [] = list()

    def read_data(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        df = pd.read_csv('./data/202106_202106_연령별인구현황_월간.csv', encoding='UTF-8', thousands=',', index_col=0)
        df.to_csv('./data/202106_202106_연령별인구현황_월간_wo_comma.csv', sep=',', na_rep='NaN')
        next(data)
        # print([i for i in data])
        # data.div(data['총인구수'], axis=0)
        # del data['총인구수'], data['연령구간인구수']
        # print(self.data)
        self.data = data

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
        # name = input('조사 대상 지역 (읍면동) 입력: ')
        [home.append(int(j)) for i in self.data if name in i[0] for j in i[3:]]
        self.home = home
        print(home)

    def array_to_list(self, arr) -> []:
        return arr.to_list()

    def list_to_array(self, ls: []) -> object:
        return np.array(ls)

    def show_plot_home(self, arr: object, name: str):
        plt.title(f'{name} 지역의 인구구조')
        plt.plot(arr)
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
    pop.find_home('보광동')
    arr_home = pop.list_to_array(pop.home)
    pop.show_plot_home(arr_home, '보광동')
