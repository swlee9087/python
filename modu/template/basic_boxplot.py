import matplotlib.pyplot as plt
import random
import histo
from modu.template import TemperatureChangesOnMyBirthday


def sorted_random_arr() -> []:
    arr = []
    [arr.append(random.randint(1, 1000)) for i in range(13)]
    return arr


def show_boxplot(arr: []):
    plt.boxplot(arr)
    plt.show()


def show_boxplot_month(month: str):
    plt.boxplot(histo.max_temps(month))
    plt.show()


def show_boxplot_all_months():
    birth = TemperatureChangesOnMyBirthday()
    birth.read_data()
    arr = birth.data
    month = [[], [], [], [], [], [], [], [], [], [], [], []]
    #    [month.append((float(i[-1])) for i in arr if i[-1] != '' and i[0].split('-')[1] - 1)]

    # for i in arr:
    #     if i[-1] != '':
    #         month[int(i[0].split('-')[1])-1].append(float(i[-1]))
    [month[int(i[0].split('-')[1]) - 1].append(float(i[-1])) for i in arr if i[-1] != '']


def show_boxplot_per_date(month: str):
    birth = TemperatureChangesOnMyBirthday()
    birth.read_data()
    day = []
    '''for i in range(31):
        day.append([])'''
    [day.append([]) for i in range(31)]
    [day[int(i[0].split('-')[2]) - 1].append(float(i[-1]))
     for i in birth.data
     if i[-1] != ''
     and i[0].split('-')[1] == month]

    #    [day.append(float(j[-1]) for i in arr if j[-1] != '' and j[0].split('-')[1] == '08' and int(j[0].split('-')[2]) - 1]
    plt.style.use('ggplot')
    plt.figure(figsize=(10, 5), dpi=300)
    plt.boxplot(day, showfliers=False)
    plt.show()


if __name__ == '__main__':
    #    show_boxplot(sorted_random_arr())
    #    show_boxplot_month('08')
#    show_boxplot_all_months()
    show_boxplot_per_date('03')
