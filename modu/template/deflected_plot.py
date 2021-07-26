import csv

from matplotlib import pyplot as plt

"""
row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)] max = -1
data : [] = list() 는 list type data 를 list()로 초기화하는, but 한 메서드내 사용하면 로컬에서 초기화. 
    ie. data : [] = None
    def save_max_temps(self):
        data=list()
but if used in various methods then will be init in field. 
    ie. data : [] = list()
"""


class TemperatureChangesOnMyBirthday(object):
    data: [] = list()
    max_temps: [] = list()

    #    min_temps: [] = list()

    def processing(self):  # hooking method order
        self.read_data()
        self.max_temps_birthday()

    #        self.visualize_data()
    #        self.extract_date_data()

    def read_data(self):
        data = csv.reader(open('./data/unit05_seoul.csv', 'rt', encoding='UTF-8'))
        next(data)
        self.data = data

    """def show_max_temps(self):
        return [i[-1] for i in self.data]

    def save_max_temps(self):
        self.max_temps.append(float(i[-1]) for i in self.data if i[-1] != '')
        #        [self.min_temps.append([float(i[-2] for i in self.data if i[-1] != '')])]

    #        print(f'Min temperatures : total {len(self.min_temps)} recordings found')
    #        max_temp: [i[-1] for i in data if i[-1] != '' and i[0].split('-')[0] <= 1990]
    #        min_temp: [i[-2] for i in data if i[-1] != '' and i[0].split('-')[0] <= 1990]

    def visualize_max_temps(self):
        #        plt.title('Temp changes on my birthday')
        plt.plot(self.max_temps, 'r')
        #        plt.plot(self.min_temps, 'b', label='min temp')
        plt.figure(figsize=(20, 2))
        #        plt.legend()
        plt.show()"""

    def max_temps_birthday(self):
        high = []
        low = []
        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1990 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1] == '08' and i[0].split('-')[2] == '07':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))

        plt.plot(high, 'pink', label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show()

    def extract_date_data(self):
        pass


if __name__ == '__main__':
    this = TemperatureChangesOnMyBirthday()
    this.read_data()
#    this.show_max_temps()
#    this.visualize_max_temps()
    this.read_data()
    this.max_temps_birthday()
#    this.extract_date_data()
