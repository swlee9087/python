import matplotlib.pyplot as plt
import random
import histo
from modu.template import TemperatureChangesOnMyBirthday

def sorted_random_arr() -> []:
    arr = []
    [arr.append(random.randint(1,1000)) for i in range(13)]
    return arr

def show_boxplot(arr: []):
    plt.boxplot(arr)
    plt.show()

def show_boxplot_all_months():
    pass

def show_boxplot_per_date(month: str):
    pass



if __name__ == '__main__':
    show_boxplot(sorted_random_arr())
