import csv

import matplotlib.pyplot as plt
import numpy as np


class Population(object):
    data: [] = list()
    home: [] = list()

    def read_data(self):
        data = csv.reader(open('./data/202106_202106_연령별인구현황_월간.csv', 'rt', encoding='UTF-8'))
        next(data)
        # print([i for i in data])
        self.data = data

    def pop_per_dong(self, dong: str) -> []:
        self.read_data()
        arr = []
        [arr.append(int(j)) for i in self.data if dong in i[0] for j in i[3:]]
        # print([i for i in arr])
        print(arr)

    def find_by_dong(self, name: str) -> []:
        self.read_data()
        home = []
        for i in self.data:
            if name in i[0]:
                home = np.array(i[3:], dtype=str)
        # [home.append(str(j)) for i in self.data if name in i[0] for j in i[3:]]
        # [home(np.array(i[3:], dtype=str) for i in self.data if name in i[0]]
        print(home)

    def show_plot(self, name, home):
        self.read_data()
        """plt.style.use('ggplot')
        plt.plot(arr)"""
        plt.rc('font', family='Malgun Gothic')
        plt.title(f'{name} 지역의 인구 구조')
        plt.plot(home)
        plt.show()


if __name__ == '__main__':
    # read_data()
    pop = Population()
    # pop.pop_per_dong()
    # pop.find_by_dong(input(f'알고 싶은 지역 (읍면동) 입력: '))
    # pop.show_plot(pop.pop_per_dong('역삼1동'))
    pop.show_plot(pop.find_by_dong(input(f'알고 싶은 지역 (읍면동) 입력: ')))
