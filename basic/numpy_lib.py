import matplotlib.pyplot as plt
import numpy as np


def show_numpy():
    t = np.arange(0., 5., 0.2)
    plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')
    plt.show()


def numpy_choice():
    dice = np.random.choice(6, 1000000, p=[0.1, .2, .3, .2, .1, .1])
    plt.hist(dice, bins=6)
    plt.show()


def numpy_bubble_chart():  # doesn't need for-in loop
    x = np.random.randint(low=10, high=100, size=200)  # low-high = range; size=amt of random data
    y = np.random.randint(10, 100, 200)
    # size = np.random.random_integers(100) * 100
    size = np.random.randint(100) * 100
    plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=0.7)
    plt.colorbar()
    plt.show()


def indexing_slicing():
    a = np.array([1, 2, 3, 4])
    print(f'list -> array: {a}')
    print(f'indexing a[1]: {a[1]}, a[-1]: {a[-1]}')  # indexing
    print(f'slicing: {a[1:]}')  # slicing


def array_one_type():
    a = np.array([1, 2, '3', 4])
    print(f'int -> str : {a}')


def np_repeat_list():
    print(np.zeros(10))
    print(np.ones(10))
    print(np.eye(10))


def np_arange():
    print(f'[0 1 2] : {np.arange(3)}')
    print(f'[3 4 5 6] : {np.arange(start=3, stop=7)}')
    print(f'[3 5] : {np.arange(3, 7, step=2)}')
    print(f'[1.  1.2 1.4 1.6 1.8] : {np.arange(start=1, stop=2, step=.2)}')


def np_linspace():
    print(f'[1.  1.1 1.2 1.3 1.4 1.5 1.6 1.7 1.8 1.9 2. ] : {np.linspace(1, 2, 11)}')
    print(f'2) {np.sqrt(np.linspace(1, 2, 11))}')
    a = np.arange(-np.pi, np.pi, np.pi / 100)
    plt.plot(a, np.sin(a))
    plt.show()


def np_mask():
    a = np.arange(-5, 5)
    print(f'mask [-5 -4 -3 -2 -1] : {a[a < 0]}')
    mask1 = abs(a) > 3
    print(f'mask1 : {a[mask1]}')
    mask2 = abs(a) % 2 == 0
    print(f'mask2 : {a[mask2]}')
    print(f'mask1 + mask2 : {a[mask1 + mask2]}')
    print(f'mask1 * mask2 : {a[mask1 * mask2]}')


def np_bubble_chart():
    x = np.random.randint(-100, 100, 1000)
    y = np.random.randint(-100, 100, 1000)
    size = np.random.randint(100) * 100
    mask1 = abs(x) > 50
    mask2 = abs(y) > 50
    x = x[mask1 + mask2]
    y = y[mask1 + mask2]
    plt.scatter(x, y, s=size, c=x, cmap='jet', alpha=.7)
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    #    show_numpy()
    #    numpy_choice()
    #    numpy_bubble_chart()
    #    indexing_slicing()
    #    np_repeat_list()
    #    np_arange()
    #    np_linspace()
    #    np_mask()
    np_bubble_chart()
