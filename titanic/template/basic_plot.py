import matplotlib.pyplot as plt

from common.menu import print_menu

"""
y-axis = list val
x = 0~1 auto incr
"""


def plot_show():
    plt.title("plotting")
    plt.plot([10, 20, 30, 40])  # hence create at least two lists for reference
    plt.show()


"""
x-axis = 1st list
y = 2nd list
"""


def plot_two_list_show():
    plt.plot([1, 2, 3, 4], [12, 43, 25, 15])
    plt.show()

def plot_two_list_show2():
    plt.title('legend')
    plt.plot([10,20,30,40], label='asc')
    plt.plot([40,30,20,10], label='desc')
    plt.legend()
    plt.show()

def plot_two_list_show3():
    plt.title('color')
    plt.plot([10,20,30,40], color='skyblue', label='skyblue')
    plt.plot([40,30,20,10], 'pink', label='pink')
    plt.legend()
    plt.show()

def plot_two_list_show4():
    plt.title('linestyle')
    plt.plot([10,20,30,40], color='r', linestyle='--', label='dashed')
    plt.plot([40,30,20,10], color='g', ls=':', label='dotted')
    plt.legend()
    plt.show()

def plot_marker_show():
    plt.title('marker')
    plt.plot([10,20,30,40], 'r.', label='circle')
    plt.plot([40,30,20,10], 'g^', label='triangle up')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    while 1:
        menu = print_menu(['exit', 'plot show', 'plot 2lists show', 'p2ls2', 'p2ls3', 'p2ls4', 'plot marker'])
        if menu == 0:
            break
        elif menu == 1:
            plot_show()
        elif menu == 2:
            plot_two_list_show()
        elif menu == 3:
            plot_two_list_show2()
        elif menu == 4:
            plot_two_list_show3()
        elif menu == 5:
            plot_two_list_show4()
        elif menu == 6:
            plot_marker_show()


