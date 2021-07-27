import matplotlib.pyplot as plt
import random

from modu.template import TemperatureChangesOnMyBirthday

"""def hist_show():
    ls = []
    plt.hist(ls, 'b')
    plt.show()
"""


def show_dice(count):
    """ls2 = [random.randint(1, 6)]
    print(ls2)"""
    ls = []
    [ls.append(random.randint(1, 6)) for i in range(count)]
    return ls


def dice_hist(ls):
    plt.hist(ls, bins=6)
    plt.show()


def show_hist_max_temps(month: str):
    birth = TemperatureChangesOnMyBirthday()
    birth.read_data()
    # [print(i) for i in birth.data]

    arr = []
#    jan = []

    [arr.append(float(i[-1])) for i in birth.data if i[-1] != '' and i[0].split('-')[1] == month]
#    [jan.append(float(i[-1])) for i in birth.data if i[-1] != '' and i[0].split('-')[1] == '01']

    plt.hist(arr, bins=1000, color='r', label=f'{month} Month')
#    plt.hist(jan, bins=100, color='b', label='Jan')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # hist_show()
    """ls = show_dice(1000000)
    print(ls)
    dice_hist(ls)"""
    show_hist_max_temps('12')
